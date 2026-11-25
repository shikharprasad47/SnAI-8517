Task 6.1

Check repository status - Shows which branch I am on and lists modified, staged, or untracked files in the working directory. (git status)

Stage selected changes - Adds specific file changes to the staging area (index) so they are queued for the next commit. (git add FILE-NAME) or can use (git add .) to add all the files at once

Create a commit - Saves a permanent snapshot of all staged changes to the local repository history with a descriptive message. (git commit -m "...")

View commit history - Displays past commits in chronological order, showing each commit's unique hash ID, author/date, and message. (git log)

Staging means selecting a file that has had some changes and commiting means showing it that file or files have got changed with some message of the user's choice

Task 6.3

A branch is an independent line of development that lets you make and test changes without affecting the main codebase (master/main). 

A Pull Request (PR) is a GitHub feature used to propose merging changes from one branch into another, allowing teammates to review diffs, leave feedback, and verify changes before they become part of the main project.

Task 6.4

Initialise a repository (git init): Starts git in the folder so it can keep track of the folder

Check status (git status): Displays the active branch and shows which files are modified, staged, or untracked.

Stage changes (git add): Moves selected file changes into the staging area to prepare them for the next commit.

Commit changes (git commit): Saves a permanent snapshot of staged changes in local Git history with a descriptive message.

View history (git log): Lists previous commits along with their unique commit IDs, timestamps, and commit messages.

Create or list branches (git branch): Lists existing local branches or creates a new branch pointer without switching to it.

Switch branches (git checkout): Moves your working directory from the current branch onto another branch.

Publish changes (git push): Uploads local commits and branches to a remote repository on GitHub.

Retrieve remote changes (git pull): Downloads and merges the latest commits from the remote GitHub repository into your local branch.