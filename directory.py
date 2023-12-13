from file import File

class Directory:
    def __init__(self, name, parent=None) -> None:
        self.name=name
        self.parent=parent
        self.subdirs={}
        self.files={}

    def add_directory(self, path):
        curr_dir=self

        for new_dir_name in path:
            new_dir=Directory(new_dir_name, parent=curr_dir)
            curr_dir.subdirs[new_dir_name]=new_dir
            print(f"new directory {new_dir_name} added to {curr_dir.name}")
            curr_dir=new_dir
        # print(f"new directory {new_dir_name} added to {curr_dir.name}")

    def get_directory(self, dir_name):
        if dir_name in self.subdirs:
            # print(f"changed to directory {dir_name}")
            return self.subdirs[dir_name]
        else:
            # print(f"Cannot navigate to {dir_name} because it does not exist.")
            return None

    def change_directory(self, path):
        curr_dir = self

        for dir_name in path:
            if dir_name == "..":
                if curr_dir.parent:
                    curr_dir = curr_dir.parent
                else:
                    print("Already at the root directory.")
            else:
                changed_dir = curr_dir.get_directory(dir_name)
                if changed_dir:
                    curr_dir = changed_dir
                else:
                    print(f"Directory '{dir_name}' not found in '{curr_dir.name}'.")

        return curr_dir
        
    def list_directories(self, indent=0):
        print("-"*indent + f"Dir: {self.name}")

        for subdir_name, subdir in self.subdirs.items():
            subdir.list_directories(indent+1)
        for file_name in self.files:
            print("-"*(indent+1)+f"file: {file_name}")

    def remove_directory(self, path):
        curr_dir=self

        for dir_name in path[:-1]:
            if dir_name in curr_dir.subdirs:
                # del curr_dir.subdirs[dir_name]
                curr_dir=curr_dir.subdirs[dir_name]

        if path[-1] in curr_dir.subdirs:
            del curr_dir.subdirs[path[-1]]
        else:
            print(f"Cannot delete {path[-1]} because it does not exist.")

########################################################################################################################

    def add_file(self, path):
        curr_dir=self

        for dir_name in path[:-1]:
            if dir_name in curr_dir.subdirs:
                curr_dir=curr_dir.subdirs[dir_name]
            else:
                print(f"Directory {curr_dir.name} not found")
                return

        file_name=path[-1]
        new_file=File(file_name)
        curr_dir.files[file_name]=new_file

        