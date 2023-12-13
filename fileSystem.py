from directory import Directory
    
class FileSystem:
    def __init__(self) -> None:
        self.root_dir=Directory("\\")

    ###################################################DirectoryImplementation#######################################################   
    def resolve_path(self, path):
        pass
    
    def mkdir(self, path):
        self.root_dir.add_directory(path)

    def cd(self, path):
        temp=self.root_dir
        self.root_dir=self.root_dir.change_directory(path)
        # print(self.root_dir!=temp)
        return self.root_dir!=temp

    def ls(self, new_dir_name="."):
        self.root_dir.list_directories()

    def rm(self, path):
        self.root_dir.remove_directory(path)

    def mv(self, dir_name, target_dir):
        pass

    def cp(self, dir_name, target_dir):
        pass
    ###################################################################################################################################

    def touch(self, path):
        curr_dir=self.root_dir
        curr_dir.add_file(path)

    def echo(self, input):
        pass


        