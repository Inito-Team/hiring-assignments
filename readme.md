# In-Memory FileSystem

A object oriented implementation of a file system using the `Directory` and `File` classes. The file system supports basic operations such as creating directories, navigating through the file system, listing directories, creating and copying files, and more.
This program uses python str, dictionaries and lists to implement the Directory class and file class

## Implementation Details

### Directory Class
The `Directory` class represents a directory in the file system. It uses name: str, subdirs: Dictionaries, files: Dictionaries

### FileSystem Class
The `FileSystem` class serves as an interface for the file system and provides methods to interact with it. It includes methods such as `mkdir`, `cd`, `ls`, `cp`, `mv`, `rm`, `touch`, `cat`, and `echo`.

### File Class
The `File` class represents a text file with a name and content. It has a `clone` method to create a deep copy of the file.

## Usage
1. Ensure you have Python installed on your system.

2. Run the `main.py` file to start the file system interface.

3. Use commands like `mkdir`, `cd`, `ls`, `cp`, `mv`, `rm`, `touch`, `cat`, and `echo` to interact with the file system.

4. Optionally, use the `save_state` and `load_state` commands to save and load the file system state.

## Example Usage
```bash
# if you don't want to load prev state and save curr state
python main.py '{"save_state": true, "load_state":false, "path": "data.json"}'
# if you want to load prev state an d save curr state
python main.py '{"save_state": true, "load_state":true, "path": "data.json"}'
# if you want to load prev state
python main.py '{"save_state": true, "load_state":true, "path": "data.json"}'
# if you don't want to save prev state and don't want to load prev state
python main.py
```

```cmd
python main.py "{\"save_state\": true, \"load_state\":true,  \"path\": \"data.json\"}"
```

## Example
1. Creating a new directory:

   ```bash
   mkdir new_dir
   ```

2. Changing directory:

   ```bash
   cd new_dir
   ```

3. Listing directories:

   ```bash
   ls
   ```

4. Copying a directory:

   ```bash
   cp src_dir target_dir
   ```

5. Moving a file:

   ```bash
   mv src_file.txt target_dir
   ```

6. Removing a directory:

   ```bash
   rm dir_to_remove
   ```

7. Adding a new text file:

   ```bash
   touch new_file.txt
   ```

8. Reading the content of a text file:

   ```bash
   cat existing_file.txt
   ```

9. Writing content to a text file:

   ```bash
   echo existing_file.txt
   Input: "Hello World"
   ```

10. Exiting the file system:

    ```bash
    exit
    ```