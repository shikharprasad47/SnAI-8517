Task 2.1

To get started with, to know where we are, (This shows the very place we are in the system)

    pwd

To list what all are there in the directory we are in,

    ls

To get a detailed listing of everything we can use,

    ls -l

To change the directory we can use,

    cd (DIRECTORY NAME)
    cd ..
Use cd .. to get one step back from the current file

To create a directory we can use,

    mkdir (DIRECTORY NAME)

To create an empty file,

    touch (FILE NAME)

To copy a file,

    cp (FILE-NAME/ADDRESS) (FILE-NAME/NEW-ADDRESS)

To move or rename a file,

    mv (CURRENT-FILE-NAME) (NEW-FILE-NAME)
    mv (CURRENT-FILE-LOCATION) (NEW-FILE-LOCATION)
But one thing to keep in mind is that when we change the name we must be in the same directory or place and when we move it we can change the directory and location so it moves around

To display file content,

    cat (FILE-NAME)

Task 2.3

"ls" is used to list the normal directory

"ls -a" uses to see hidden files
"ls -h" converts raw bytes to human-understandable language

"|" is used so that the output of one command trasnfer to the second command (on the right hand side) as its input

Task 2.4

To check brew's version just use 
    
    brew --version

To see what all its managing just use

    brew list

A package manager automates finding, installing, updating, and removing software tools directly from the command line. It automatically resolves and installs required dependencies so programs work without manual configuration, while keeping all installed tools updated and organized in one place.

Mission 2 - Become comfortable with the Terminal

1. Task / objective
Use the macOS command-line interface (Terminal) to inspect directories, create, copy, move, and view practice files safely inside a temporary folder, explore command flags and pipes, and check Homebrew package manager information without installing or uninstalling software.

2. Work completed
- Completed Task 2.1 by practicing nine core navigation and file-management commands ("pwd", "ls", "ls -l", "cd", "mkdir", "touch", "cp", "mv", and "cat") and recording observations in a reference table.
- Completed Task 2.2 by creating a "terminal-practice" folder inside the repository, writing and appending text lines using ">" and ">>", creating and renaming a backup file, and answering the file-operation questions.
- Completed Task 2.3 by comparing normal "ls" output against "ls -lah" and piping "ls -l" into "head -n 5" to inspect how flags and pipes filter output.
- Completed Task 2.4 by running read-only Homebrew version and package-list checks and explaining why package managers are useful, then cleaned up the temporary practice folder before committing.

3. Commands / tools used
- "pwd", "ls", "ls -l", "ls -lah", and "cd" — Checked current directory paths, listed visible and hidden files with human-readable metadata, and navigated folders.
- "mkdir", "touch", "cp", "mv", "cat", and "rm -rf" — Created directories and files, copied and renamed backups, displayed file contents, and cleaned up the temporary practice folder.
- ">" (redirect), ">>" (append), and "|" (pipe) — Overwrote or appended lines to text files and passed command output directly into "head -n 5".
- "brew --version" and "brew list" — Checked the installed Homebrew version and listed managed packages on macOS.

4. My understanding
The Terminal gives direct, precise control over files and workflows without needing a graphical interface. Command flags modify how tools behave (such as revealing hidden dotfiles and readable sizes with "-lah"), while pipes ("|") connect small utilities together so the output of one command becomes the input of another. Package managers like Homebrew simplify software maintenance by handling installations, dependencies, and updates cleanly from the command line.

5. Difficulties faced
No major difficulties.

6. How I resolved them
Not applicable.

7. Evidence / files
- "mission-02-terminal/README.md" (containing the Task 2.1 command reference table, Task 2.2 answers, Task 2.3 flags and pipes comparison, and Task 2.4 package manager notes)

8. Commit details
Committed with message "Complete Terminal and file management mission" and pushed to "master" on GitHub.