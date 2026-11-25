Task 3.1

    sw_vers
    uname -srm

Shows macOS and Kernel version

    whoami

Shows current user's name

    df -h

shows total used and available storage on the main disk in GB

    ps aux | head -n 6

captures snapshot of the current running CPU

Task 3.2

Anything thats being worked infront of the screen or behind the screen at certain input or task is called process.

PID stands for Process Identifier. Its a unique number assigned by the operating system to track and manage each running process individually.

Visual Studio Code and Opera browser

Task 3.3

Absolute Path - user/desktop/SnAI-8517/mission-03-operating-system. This was obtained by "pwd" showing exactly where I am on my system

Relative path - mission-03-operating-system/README.md is where I am currently working at but it has no context where the file is located in my system

Upon using it. It shows rw-r--r-- which means that owner can read and write

Task 3.4

For the OS responsibilites,

Process Management -
                    Starts, schedules, pauses, and terminates running programs so multiple apps share CPU time smoothly. Example - Running VS Code, Terminal, and a web browser simultaneously without freezing.

Memory Management - 
                    Allocates RAM to active programs and frees up memory when apps close so programs don't overwrite each other. Example - Giving browser tabs their own memory space and reclaiming RAM when tabs close.

Device management -
                    Uses drivers to communicate with and control hardware peripherals connected to the computer. Example - Handling keyboard typing, mouse clicks, display output, and Wi-Fi adapters.

File management - 
                    Organizes data into files and folders on storage drives and tracks file metadata and locations. Example - Creating, saving, renaming, and organizing mission folders inside Finder or Terminal.

User interface -  
                    Provides a visual or text-based way for the user to interact with the operating system and launch tasks. Example - Using the macOS GUI desktop or typing commands into the `zsh` shell in Terminal.

Security and permissions - 
                    Controls user logins and restricts which users or apps can read, modify, or execute specific files. Example - Preventing standard user accounts from modifying protected system files without authorization.