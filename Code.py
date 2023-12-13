import json
import os
class InMemoryFileSystem:
    def _init_(self):
        self.root = {'name': '/', 'type': 'dir', 'contents': {}}
        self.current_dir = self.root

    def mkdir(self, dir_name):
        new_dir = {'name': dir_name, 'type': 'dir', 'contents': {}}
        self.current_dir['contents'][dir_name] = new_dir


    def cd(self, path):
        if path == '/':
            self.current_dir = self.root
        elif path == '..':
            if self.current_dir['name'] != '/':
                self.current_dir = self._get_parent_directory(self.current_dir)
        else:
            target_dir = self._get_directory_by_path(path)
            if target_dir:
                self.current_dir = target_dir
            else:
                print(f"cd: {path}: No such directory")


    def ls1(self, path='.'):
        target_dir = self._get_directory_by_path(path)
        if target_dir:
            contents = [item['name'] for item in target_dir['contents'].values()]
            print("\n".join(contents))
        else:
            print(f"ls: {path}: No such directory")

    def ls(self, path='.'):
        # List the contents of the specified directory
        directory = self._get_directory_by_path(path)
        if directory:
            contents = [item['name'] for item in directory['contents'].values()]
            print(list(directory['contents'].keys()))
        else:
            return None


    def touch(self, file_name):
        new_file = {'name': file_name, 'type': 'file', 'content': ''}
        self.current_dir['contents'][file_name] = new_file



    def cat(self, file_name):
        file = self.current_dir['contents'].get(file_name)
        if file and file['type'] == 'file':
            print(file['content'])
        else:
            print(f"cat: {file_name}: No such file")

    def echo(self, text, file_name):
        file = self.current_dir['contents'].get(file_name)
        if file and file['type'] == 'file':
            file['content'] = text
        else:
            print(f"echo: {file_name}: No such file")

    def grep(self, pattern, file_path):
        # Search for a specified pattern in a file
        file = self._get_file_by_path(file_path)
        if file and file['type'] == 'file':
            content = file['content']
            lines = content.split('\n')
            matching_lines = [line for line in lines if pattern in line]
            return matching_lines
        else:
            return None
    
    def mv(self, source_path, destination_path):
        source = self._get_directory_by_path(source_path)
        destination_parent = self._get_directory_by_path(os.path.dirname(destination_path))

        if source and destination_parent:
            source_name = os.path.basename(source_path)
            destination_name = os.path.basename(destination_path)
            destination_parent['contents'][destination_name] = source
            del source_parent['contents'][source_name]
        else:
            print(f"mv: {source_path}: No such file or directory")

    def cp(self, source_path, destination_path):
        source = self._get_directory_by_path(source_path)
        destination_parent = self._get_directory_by_path(os.path.dirname(destination_path))

        if source and destination_parent:
            source_name = os.path.basename(source_path)
            destination_name = os.path.basename(destination_path)
            destination_parent['contents'][destination_name] = self._deep_copy(source)
        else:
            print(f"cp: {source_path}: No such file or directory")

    def rm(self, file_path):
        try:
            # Check if the file exists before removing
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' removed successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def _get_directory_by_path(self, path):
        if path == '/':
            return self.root

        if not path.startswith('/'):
            path = os.path.join(self.current_dir['name'], path)

        components = path.split('/')
        current = self.root
        for component in components[1:]:
            if component in current['contents'] and current['contents'][component]['type'] == 'dir':
                current = current['contents'][component]
            else:
                return None

        return current

    def _get_parent_directory(self, directory):
        path = directory['name']
        parent_path = os.path.dirname(path)
        return self._get_directory_by_path(parent_path)

    def _deep_copy(self, obj):
        if isinstance(obj, dict):
            return {k: self._deep_copy(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._deep_copy(item) for item in obj]
        else:
            return obj

    def save_state(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.root, file)

    def load_state(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.root = json.load(file)
                self.current_dir = self.root
        else:
            print(f"load_state: {file_path}: File not found")

# Command-line interface
def run_file_system():
    file_system = InMemoryFileSystem()

    while True:
        user_input = input(f"{file_system.current_dir['name']} $ ")
        if user_input.lower() == 'exit':
            break

        command_tokens = user_input.split(' ', 1)
        command = command_tokens[0]
        print(command)
        arguments = command_tokens[1] if len(command_tokens) > 1 else ''

        if command == 'mkdir':
            file_system.mkdir(arguments)
        elif command == 'cd':
            file_system.cd(arguments)
        elif command == 'ls':
            file_system.ls(arguments)
        elif command == 'touch':
            file_system.touch(arguments)
        elif command == 'cat':
            file_system.cat(arguments)
        elif command == 'echo':
            text, file_name = arguments.split(' ', 1)
            file_system.echo(file_name, text)
        elif command == 'mv':
            source, destination = arguments.split(' ', 1)
            file_system.mv(source, destination)
        elif command == 'cp':
            source, destination = arguments.split(' ', 1)
            file_system.cp(source, destination)
        elif command == 'rm':
            file_system.rm(arguments)
        elif command == 'save_state':
            save_path = arguments.split(' ', 1)
            file_system.save_state(save_path)
            print(f"File system state saved to {save_path}")
        elif command == 'load_state':
            load_path = arguments.split(' ', 1)
            file_system.load_state(load_path)
            print(f"File system state loaded from {load_path}")
        else:
            print(f"Unsupported command: {command}")

    if _name_ == "_main_":
        file_system.mkdir(arguments)
run_file_system()
