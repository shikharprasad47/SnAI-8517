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

Mission 6 - Git and GitHub

1. Task / objective
Practice the core Git version-control workflow, explain the difference between staging and committing changes, create a new branch ("update-about") to add a "My Learning" section to the root "README.md", open a Pull Request on GitHub, and build a nine-command Git glossary.

2. Work completed
- Completed Task 6.1 by inspecting repository status, staging and committing changes, reviewing commit history, and explaining the difference between staging ("git add") and committing ("git commit").
- Completed Task 6.2 by creating and switching to the "update-about" branch, adding the "My Learning" section to the root "README.md", committing the update, and pushing the branch to GitHub.
- Completed Task 6.3 by opening a Pull Request on GitHub comparing "update-about" into "master", documenting its current PR status (Open), switching back to "master" locally, and explaining why branches and Pull Requests are useful.
- Completed Task 6.4 by writing clear one-line explanations in my own words for nine essential Git operations.

3. Commands / tools used
- "git status", "git add", "git commit", and "git log --oneline" — Inspected repository state, staged selected files, saved commit snapshots, and reviewed commit history.
- "git checkout -b update-about" and "git checkout master" — Created the feature branch and switched back to the main local branch.
- "git push -u origin update-about" — Published the new branch to the remote GitHub repository.
- GitHub Web Interface — Used to open and review the Pull Request from "update-about" into "master".

4. My understanding
Staging ("git add") selects and prepares specific file changes for the next snapshot, while committing ("git commit") permanently records that staged snapshot in Git history. Branches allow developers to work on new updates safely without affecting the main branch ("master"), and Pull Requests provide a structured space to review diffs and discuss changes before merging them into the main project.

5. Difficulties faced
No major difficulties.

6. How I resolved them
Not applicable.

7. Evidence / files
- "mission-06-git-github/README.md" (containing the Task 6.1 Git workflow table, Task 6.2 and 6.3 branch and Pull Request explanations with PR status, and Task 6.4 Git command glossary)
- "update-about" branch and Pull Request visible on GitHub

8. Commit details
Committed with message "Complete Git and GitHub collaboration mission" and pushed to "master" on GitHub.