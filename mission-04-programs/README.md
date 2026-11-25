Task 4.2

Point | Compiler | Interpreter

When translation / execution happens | the entire source code translates into machine code before the program runs | Reads, translates, and executes source code line by line at runtime.

Typical output | Produces a separate standalone executable binary file (such as .exe or a macOS binary) | Does not produce a standalone binary and directly executes instructions and outputs program results.

One example	| C, C++, or Rust (gcc, clang) | Python (python3) or JavaScript.

One advantage | Compiled programs run much faster because translation is already done ahead of time | Easier and faster to test and debug since code runs immediately without a separate build step

Mission 4 - How programs run

1. Task / objective
Create and run a basic Python 3 script ("hello.py") inside the mission folder, and compare how compilers and interpreters translate and execute source code using a structured comparison table and short explanation.

2. Work completed
- Completed Task 4.1 by creating "mission-04-programs/hello.py" with a one-line print statement and running it via Python 3 in Terminal to confirm it prints "Hello from Python".
- Completed Task 4.2 by filling out the four-point compiler vs. interpreter comparison table (translation timing, typical output, language example, and key advantage) and writing a concise summary explaining the differences.
- Saved all documentation in "mission-04-programs/README.md" and committed both files to GitHub.

3. Commands / tools used
- Visual Studio Code — Used to create and edit "hello.py" and "mission-04-programs/README.md".
- "python3 mission-04-programs/hello.py" — Executed the Python script from Terminal using the Python 3 interpreter.
- "git add", "git commit", and "git push" — Staged, committed, and pushed Mission 4 to GitHub.

4. My understanding
Compilers translate an entire source code file into a standalone machine-code executable before the program runs, which produces faster runtime execution. Interpreters read, translate, and execute source code line by line at runtime without generating a separate binary file, making languages like Python quicker to test and debug during development.

5. Difficulties faced
No major difficulties.

6. How I resolved them
Not applicable.

7. Evidence / files
- "mission-04-programs/hello.py"
- "mission-04-programs/README.md" (containing the Task 4.2 compiler vs. interpreter comparison table and explanation)

8. Commit details
Committed with message "Compare compilers and interpreters" and pushed to "master" on GitHub.