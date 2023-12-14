from fileSystem import FileSystem
import json
import sys

if __name__=="__main__":

    file_system=FileSystem()
    walked_path=file_system.root_dir.name

    script=json.loads(sys.argv[1])

    if script['save_state']:
        file_system.save_state(script['path'])

    elif script['load_state']:
        file_system.load_state(script['path'])

    while True:
        command=input(f"curr dir:  {walked_path}>  ").split()
        action=command[0]
        
        if len(command)==2:
            path=command[1].split("/")
        # elif len(command)>1: 
        #     rest=command[1:]
        #     rest_data=""
        #     for ele in rest: rest_data+=ele
        #     ip=rest_data.split(" > ")
        #     path=ip[1]
        #     text=ip[0]
            
        if len(command)==3:
            src=command[1].split("/")
            target=command[2].split("/")
        
        match action:
            case 'exit':
                file_system.save_state()
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
            case 'mv':
                file_system.mv(src, target)
            case 'cp':
                file_system.cp(src, target)
            case "touch":
                file_system.touch(path)
            case 'cat':
                file_system.cat(path)
            case 'echo':
                text=input("enter txt: ")
                file_system.echo(text, path)
                # print("text written")
            case _:
                print("The command is not recognized. Please use these commands {mkdir, cd, ls, grep, mv, cp, rm, cat, touch, echo}")