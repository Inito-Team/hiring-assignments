from directory import Directory
import json

class FileSystem:
    def __init__(self) -> None:
        self.root_dir=Directory("\\")

    ###################################################DirectoryImplementation#######################################################   
        
    def mkdir(self, path):
        self.root_dir.add_directory(path)

    def cd(self, path):
        new_dir=self.root_dir.change_directory(path)
        # print(self.root_dir!=temp)
        return self.root_dir!=new_dir

    def ls(self, new_dir_name="."):
        self.root_dir.list_directories()

    def rm(self, path):
        self.root_dir.remove(path)

    def mv(self, src, target):
        self.root_dir.move(src, target)

    def cp(self, src, target):
        self.root_dir.copy(src, target)
    ###################################################################################################################################

    def touch(self, path):
        curr_dir=self.root_dir
        curr_dir.add_file(path)

    def cat(self, path):
        curr_dir=self.root_dir
        curr_dir.read_content(path)

    def echo(self, text, path):
        curr_dir=self.root_dir
        curr_dir.write_content(text, path)

    ####################################################################save state and load state##########################################

    def save_state(self, file_path="data.json"):
        saved_data=self.root_dir.serialize()

        with open(file_path, 'w') as f:
            json.dump(saved_data, f)

    def load_state(self, file_path="data.json"):
        with open(file_path, 'r') as f:
            load_state_data = json.load(f)

        self.root_dir = Directory.deserialize(load_state_data)