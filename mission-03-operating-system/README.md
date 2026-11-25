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

Mission 3 - Understand the operating system

1. Task / objective
Explore the macOS operating system environment, inspect active user identity, storage usage, and running processes with Process Identifiers (PIDs), compare absolute and relative file paths, inspect owner file permissions ("rwx"), and explain core operating system responsibilities.

2. Work completed
- Completed Task 3.1 by inspecting OS version, kernel/architecture details, active account identity (redacted), disk storage capacity, and a live system activity snapshot.
- Completed Task 3.2 by listing active processes while running applications, explaining what a process and PID are, and identifying two active process examples.
- Completed Task 3.3 by navigating between the root repository and mission subfolders to compare absolute and relative paths, and inspecting "ls -l" permission flags ("-rw-r--r--") for the file owner.
- Completed Task 3.4 by completing the six-row operating system responsibilities table covering process, memory, device, file, shell/UI, and security management.

3. Commands / tools used
- "sw_vers" and "uname -srm" — Displayed macOS version, "Darwin" kernel, and "arm64" architecture details.
- "whoami" and "df -h /" — Verified the active local user session (redacted as "[redacted]") and checked used versus available disk space.
- "top -l 1 | head -n 12" and "ps aux | head -n 15" — Captured a snapshot of system resource usage and running processes with their PIDs.
- "cd", "pwd", and "ls -l" — Compared absolute vs. relative paths and inspected owner read, write, and execute permission letters.

4. My understanding
The operating system acts as the resource manager between hardware and user applications, assigning each running program a unique Process Identifier (PID) so multiple apps can share CPU and RAM safely. Understanding absolute paths (starting from "/") versus relative paths (starting from the current folder) prevents navigation mistakes, while permission bits ("r", "w", "x") protect files from unauthorized reading, editing, or execution.

5. Difficulties faced
No major difficulties.

6. How I resolved them
Not applicable.

7. Evidence / files
- "mission-03-operating-system/README.md" (containing Task 3.1 privacy-safe system table, Task 3.2 process notes, Task 3.3 path and permission analysis, and Task 3.4 OS responsibilities table)

8. Commit details
Committed with message "Document operating system and file management" and pushed to "master" on GitHub.