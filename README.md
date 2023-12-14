# In-memory-fileSystem

## Description
An in-memory file system to support various functionalities.

## Implementation/ Logic
The logic is to use object which is already there in the JavaScript world, using the key as a name and value as its content
eg; 

```javascript
{
    "/": {
        "folder1": {
            "folder-name.txt": "hello this is a folder",
            "folder2-inside-folder1": {} //empty folder
        },
        "name.txt": "Hello this is a text file"
    }
}
```
- If any key contains the {} as its value that means it is a folder.
- If any key contains the string as its value that means it is a file.


## Commands

- #### mkdir: 
    Create a new directory
    ``` mkdir <dir_name> ```
- #### cd: 
    Change directory
    ``` cd <dir_path> ```
- #### ls: 
    List contents
    ``` ls <dir_path> ```
- #### grep:
    this command will search the regex in all of the files who is children to the current directory
   ``` grep <regex_text> <file_name>```
- #### cat: 
    Display the contents of the file
      ``` cat <file_name>|<file_path> ```
- #### touch: 
    Create a new empty file
      ``` touch <file_name> ```
- #### rm: 
    Remove a file or directory
      ``` rm <file_name>|<dir_name> ```
- #### pwd:
    Print the path of the current directory from root ('/')
- #### echo: 
    write text to a file,
      ```echo 'hi my name is sarvesh' > ./file.txt``` 
- #### mv:
    Move a file,
  ``` mv /data/ice_cream/cassata.txt ./data/boring/ice_cream/mississippimudpie ```
- #### cp: 
    Copy a file to a directory,
  ```mv /data/ice_cream/cassata.txt ./data/boring/ice_cream/mississippimudpie/```

## Run Locally
#### steps
Install Node and NPM
```bash
Refer here: https://nodejs.org/en/download
```

Clone the project

```bash
  git clone https://github.com/sarveshmaurya306/in-memory-fs.git
```

Go to the project directory

```bash
  cd in-memory-fs
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  node index.js
```

#### After running this in local you will see the CLI like Interface in your terminal where you can interact there and can provide all the commands inside that

## Bonus - Save and reload the state from a file
if you want to save the state of the current in-memory-fs run the starting command as
```bash
    node ./index.js --path=<your_path/your_memory_file_name.json>
```

## Authors

- [@sarveshmaurya306](https://www.github.com/sarveshmaurya306)
