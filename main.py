from fileSystem import FileSystem

if __name__=="__main__":

    file_system=FileSystem()
    walked_path=file_system.root_dir.name

    while True:
        command=input(f"curr dir:  {walked_path}>  ").split()
        action=command[0]
        
        if len(command)==2: 
            path=command[1].split("/")
        
        match action:
            case 'exit':
                break
            case 'mkdir':
                file_system.mkdir(path)
            case 'cd':
                temp=path
                if file_system.cd(path):
                    for ele in temp:
                        if ele=="..":
                            walked_path="\\".join(walked_path.split("\\")[:-1])
                            if walked_path=="": walked_path+="\\"
                        else:
                            walked_path+="\\" if walked_path!="\\" else ""
                            walked_path+=ele
            case 'ls':
                file_system.ls()
            case 'rm':
                file_system.rm(path)
            case "touch":
                file_system.touch(path)
            case _:
                print("The command is not recognized. Please use these commands {mkdir, cd, ls, grep, mv, cp, rm, cat, touch, echo}")