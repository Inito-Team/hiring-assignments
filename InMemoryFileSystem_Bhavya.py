class InMemoryFileSystem:
    def __init__(self):
        self.root = {'type': 'dir', 'name': '/', 'content': {}}
        self.current_directory = self.root

    def mkdir(self, directory_name):
        new_dir = {'type': 'dir', 'name': directory_name, 'content': {}}
        self.current_directory['content'][directory_name] = new_dir

    def cd(self, path):
        if path == '/':
            self.current_directory = self.root
        elif path.startswith('/'):
            # Absolute path
            self.current_directory = self._get_directory_by_path(path)
        else:
            # Relative path
            new_path = f'{self.current_directory["name"]}/{path}'
            self.current_directory = self._get_directory_by_path(new_path)

    def ls(self, path='.'):
        directory = self._get_directory_by_path(path)
        contents = directory['content']
        return list(contents.keys())

    def grep(self, filename, pattern):
        file_content = self._get_file_content(filename)
        return [line for line in file_content.split('\n') if pattern in line]

    def cat(self, filename):
        file_content = self._get_file_content(filename)
        return file_content

    def touch(self, filename):
        new_file = {'type': 'file', 'name': filename, 'content': ''}
        self.current_directory['content'][filename] = new_file

    def echo(self, filename, text):
        if filename not in self.current_directory['content']:
            self.touch(filename)
        self.current_directory['content'][filename]['content'] += text + '\n'

    def mv(self, source_path, destination_path):
        source = self._get_directory_by_path(source_path)
        destination = self._get_directory_by_path(destination_path)

        filename = source['name']
        destination['content'][filename] = source
        del source['content'][filename]

    def cp(self, source_path, destination_path):
        source = self._get_directory_by_path(source_path)
        destination = self._get_directory_by_path(destination_path)

        filename = source['name']
        destination['content'][filename] = {'type': source['type'], 'name': filename, 'content': source['content']}

    def rm(self, path):
        if path == '/':
            raise Exception("Cannot remove root directory")

        parent_dir_path, dir_name = self._get_parent_directory_path(path)
        parent_dir = self._get_directory_by_path(parent_dir_path)
        del parent_dir['content'][dir_name]

    def _get_directory_by_path(self, path):
        if path == '/':
            return self.root

        path_parts = path.split('/')
        current_dir = self.current_directory

        for part in path_parts:
            if part == '..':
                current_dir = self._get_parent_directory(current_dir)
            elif part:
                current_dir = current_dir['content'][part]

        return current_dir

    def _get_parent_directory(self, directory):
        if directory['name'] == '/':
            return directory

        parent_path, _ = self._get_parent_directory_path(directory['name'])
        return self._get_directory_by_path(parent_path)

    def _get_parent_directory_path(self, path):
        parts = path.split('/')
        if len(parts) == 1:
            return '/', parts[0]
        else:
            return '/'.join(parts[:-1]), parts[-1]

    def _get_file_content(self, filename):
        return self._get_directory_by_path(filename)['content']
