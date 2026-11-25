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