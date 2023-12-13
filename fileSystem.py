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
        # print(self.root_dir.name)
        # curr_dir=self
        # for dir_name in path:
        #     if dir_name=="..":
        #         if self.root_dir.parent:
        #             self.root_dir=self.root_dir.parent
        #     else:
        #         changed_dir=curr_dir.root_dir.get_directory(dir_name)
        #         if changed_dir:
        #             curr_dir.root_dir=changed_dir

    def ls(self, new_dir_name="."):
        self.root_dir.list_directories()

    def rm(self, path):
        self.root_dir.remove_directory(path)

    def mv(self, dir_name, target_dir):
        pass

    def cp(self, dir_name, target_dir):
        pass
    ###################################################################################################################################


        