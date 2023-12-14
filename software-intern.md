# Assignment Question:In-Memory File System

Your task is to create an in-memory file system to support various functionalities. The file system should include the following operations:

1. `mkdir`: Create a new directory.
2. `cd`: Changes the current directory. Support navigating to the parent directory using `..`, moving to the root directory using `/`, and navigating to a specified absolute path. Basically anything that you can do in a normal terminal. Since there is no user level implementation, ~ and / should take you to root.
3. `ls`: List the contents of the current directory or a specified directory.
4. `grep`: Search for a specified pattern in a file. **PS: Its a bonus**
5. `cat`: Display the contents of a file.
6. `touch`: Create a new empty file.
7. `echo`: Write text to a file. ex - `echo 'I am "Finding" difficult to write this to file' > file.txt`
8. `mv`: Move a file or directory to another location. ex - `mv /data/ice_cream/cassata.txt ./data/boring/ice_cream/mississippimudpie/`
9. `cp`: Copy a file or directory to another location. ex - `cp /data/ice_cream/cassata.txt .` **. For current directory **
10. `rm`: Remove a file or directory.


## Instructions

Create an existing in-memory file system implementation in a language of your choice to accommodate the functionalities. This needs to run an infinite loop with an exit code. And it should implement the commands as you would in a terminal.

## Requirements

1. Build in-memory file system structure to support `mv`, `cp`, and `rm` operations.
2. Implement directory navigation functionalities (`cd`) to support relative paths like `..`, `../`, absolute paths like `/`, and navigating to a specified path.
3. **Ensure that all operations handle appropriate error cases and invalid inputs gracefully**.
4. Maintain a clear and user-friendly command-line interface (CLI) or an interactive system for executing these operations.

## Bonus - Save and reload the state

### PRO TIP - Do the bonus question

Take an input that tell if the state of the file system needs to be saved in persistent memory when the process is terminated and one that tells if it needs to be reloaded when the new process starts.

For example - let's say you wrote the the whole program in python. `python script.py "{'save_state': 'true', 'path': '/songs/guns_n_roses/november_rain.txt'}"`, should store the current state in a persistent memory so that it can be loaded when a new process starts. It need not be a .txt file, it can be JSON or whatever you feel is good enough.

### Loading a state from a file -
Taking the same python file, if you want to start where you left, when a new process starts, input could be - `python script.py "{'load_state': 'true', 'path': '/songs/guns_n_roses/november_rain.txt'}`,

You can think of a different implementation of the same as well


## Grading Criteria

Your submission will be assessed based on:

1. Correctness - Whatever is implemented needs to work 99.99% of the times. Errors must be handled 😅.
2. Completeness - All the requirements of the assignment should be complete. Every operation that is implemented has their own weightage. Complete all 10 to get the maximum marks.
3. Efficiency - O(1), O(log N) and all that jazz
4. Clarity, structure, and readability of the code - Plz Don't write everything in one file 🙏🙏🙏🙏🙏🙏🙏. Make it structured, pass context to the new class.
5. Speed - Be hacky, submit fast.
6. Unit Tests - You stand out if you write them. 🙌🙌🙌🙌
7. Docs - Write down how you implemented the system, data structures used, design decisions taken etc etc. **Assume that the dev that is going to check your code does not have their environment setup for your code to run. write a setup script or a docker file that we can run** . PS - We will not be checking your code if docs are not written

## Submission Guidelines

* Submit your code in the chosen programming language along with explanations of the implemented functionalities, improvements made to the design, and instructions on how to run and test your program.

* Create a GitHub repo, create a PR with with the changes and fill the form with the github link and other details - https://forms.gle/9p8KuuqL6gnwqWoy7.

* Along with the link, submit your resume and any other work of yours that you want us to consider.

**Note:**

Linking a few playlists that might help you out while coding -

* https://www.youtube.com/watch?v=_8qtMXyu9D8
* https://www.youtube.com/watch?v=serJjyYrEhY
* https://www.youtube.com/watch?v=Kt-tLuszKBA
