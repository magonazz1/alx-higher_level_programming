#!/usr/bin/python3

import subprocess

def make_scripts_executable():
    """
    Make all Python scripts in the current directory executable.

    This function uses the 'chmod' command to make all files with a '.py' extension executable.
    """
    subprocess.run(["chmod", "+x", "*.py"])

def auto_git():
    """
    Automate Git commands for adding, committing, and pushing changes to a Git repository.

    This function adds all changes to the staging area, prompts the user for a commit message,
    and then commits and pushes the changes to the remote repository.

    Usage:
    1. Make the script executable: chmod +x script.py
    2. Run it in the directory of your Git repository: ./script.py
    """

    # Add all changes to the staging area
    subprocess.run(["git", "add", "."])

    # Prompt the user for a commit message
    commit_mesg = input("Write your commit message: ")

    # Commit the changes with the provided message
    subprocess.run(["git", "commit", "-m", commit_mesg])

    # Push the changes to the remote repository
    subprocess.run(["git", "push"])

def main():
    choice = input("Are your Python scripts already executable? (y/n): ")

    if choice.lower() == "y":
        auto_git()
    elif choice.lower() == "n":
        make_scripts_executable()
        auto_git()
    else:
        print("Invalid choice. Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()

