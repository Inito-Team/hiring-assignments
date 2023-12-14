from file import File
from copy import deepcopy

class Directory:
    path_traversed=[]

    def __init__(self, name) -> None:
        self.name=name
        self.subdirs={}
        self.files={}
        
    def add_directory(self, path):
        curr_dir=self

        for new_dir_name in path:
            if new_dir_name:
                new_dir=Directory(new_dir_name)
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
                if curr_dir.path_traversed:
                    curr_dir = curr_dir.path_traversed.pop()
                else:
                    print("Already at the root directory.")
            else:
                changed_dir = curr_dir.get_directory(dir_name)
                if changed_dir:
                    curr_dir.path_traversed.append(curr_dir)
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

    def clone(self):
        return deepcopy(self)

    def copy(self, src, target):
        curr_src_dir = self.find_curr_dir(src[:-1])

        if src[-1] in curr_src_dir.subdirs:
            to_cp = curr_src_dir.subdirs[src[-1]]
            curr_tar_dir = self.find_curr_dir(target)
            copied_dir = to_cp.clone()

            curr_tar_dir.subdirs[src[-1]] = copied_dir
            print(f"Dir: {src[-1]} copied from {curr_src_dir.name} to {curr_tar_dir.name}")
        elif src[-1] in curr_src_dir.files:
            to_cp=curr_src_dir.files[src[-1]]
            curr_tar_dir=self.find_curr_dir(target)
            copied_file=to_cp.clone()

            curr_tar_dir.files[src[-1]]=copied_file
            print(f"File: {src[-1]} copied from {curr_src_dir.name} to {curr_tar_dir.name}")
        else:
            print(f"Item '{src[-1]}' not found in '{curr_src_dir.name}'.")

    def move(self, src, target):
        curr_src_dir = self.find_curr_dir(src[:-1])

        if src[-1] in curr_src_dir.subdirs:
            to_cp = curr_src_dir.subdirs[src[-1]]
            del curr_src_dir.subdirs[src[-1]]
            curr_tar_dir = self.find_curr_dir(target)

            copied_dir = to_cp.clone()
            curr_tar_dir.subdirs[src[-1]] = copied_dir
            print(f"Directory '{src[-1]}' moved from '{curr_src_dir.name}' to '{curr_tar_dir.name}'.")
        elif src[-1] in curr_src_dir.files:
            to_cp=curr_src_dir.files[src[-1]]
            del curr_src_dir.files[src[-1]]
            curr_tar_dir=self.find_curr_dir(target)
            
            copied_file=to_cp.clone()
            curr_tar_dir.files[src[-1]]=copied_file
            print(f"File: {src[-1]} copied from {curr_src_dir.name} to {curr_tar_dir.name}")
        else:
            print(f"Directory '{src[-1]}' not found in '{curr_src_dir.name}'.")

    def remove(self, path):
        curr_dir=self

        for dir_name in path[:-1]:
            if dir_name in curr_dir.subdirs:
                # del curr_dir.subdirs[dir_name]
                curr_dir=curr_dir.subdirs[dir_name]

        to_del=path[-1]
        if to_del in curr_dir.subdirs:
            del curr_dir.subdirs[to_del]
            print(f"Dir: {to_del} removed from dir: {curr_dir.name}")
        elif to_del in curr_dir.files:
            del curr_dir.files[to_del]
            print(f"File: {to_del} removed from dir: {curr_dir.name}")
        else:
            print(f"Cannot delete {to_del} because it does not exist.")

########################################################################################################################

    def find_curr_dir(self, path):
        curr_dir=self
        for dir_name in path:
            if dir_name in curr_dir.subdirs:
                curr_dir=curr_dir.subdirs[dir_name]
            else:
                print(f"dir: {dir_name} not found at dir: {curr_dir.name}")
                return None
            
        return curr_dir

    def add_file(self, path):
        curr_dir=self.find_curr_dir(path[:-1])

        if curr_dir is not None: 
            file_name=path[-1]
            if file_name.endswith(".txt"):
                new_file=File(file_name)
                curr_dir.files[file_name]=new_file
                print(f"file: {new_file.name} added to dir: {curr_dir.name}")
            else: print("Cannot create file, check your file extension")
        else:
            print(f"cannot create file, directory not found")

    def read_content(self, path):
        curr_dir=self.find_curr_dir(path[:-1])

        if curr_dir is not None:
            file_name=path[-1]
            if file_name and file_name.endswith(".txt"):
                file=curr_dir.files[file_name]
                if file: print(file.content)
                else: print("Cannot read file, please check your file name again")
            else: print(f"Cannot find file: {file_name}")

    def write_content(self, text, path):
        curr_dir=self.find_curr_dir(path[:-1])

        if curr_dir is not None: 
            file_name=path[-1]
            file=curr_dir.files[file_name]
            if file and file_name.endswith(".txt"):
                file.content=text
                print(f"content written in file: {file_name} in dir: {curr_dir.name}")
            else:
                print("cannot write on file, file not found")
        else:
            print(f"cannot write on file, directory not found")

##############################################################################################################################

    def serialize(self):
        serialized_data={
            'name': self.name,
            'subdirs': {},
            'files' : {}
        }

        for subdir_name, subdir in self.subdirs.items():
            serialized_data['subdirs'][subdir_name]=subdir.serialize()

        for file_name, file in self.files.items():
            serialized_data['files'][file_name]=file

        return serialized_data
    
    def deserialize(self, data):
        dir=Directory(data['name'])

        for subdir_name, subdir_data in data['subdirs'].items():
            subdir=self.deserialize(subdir_data)
            dir.subdirs[subdir_name]=subdir

        for file_name, file_data in data['files'].items():
            file=self.deserialize(file_data)
            dir.files[file_name]=file

        return dir