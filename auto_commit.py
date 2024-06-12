# auto_commit.py

import subprocess
import sys
from config import update_file
def run_command(command):
    """Run a shell command and print its output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
        sys.exit(result.returncode)
    return result.stdout.strip()

def git_add():
    """Stage all changes."""
    print("Staging all changes...")
    run_command("git add .")

def git_commit(message):
    """Commit changes with the provided message."""
    print(f"Committing changes with message: {message}")
    run_command(f"git commit -m \"{message}\"")

def git_push():
    """Push changes to the remote repository."""
    print("Pushing changes to remote repository...")
    run_command("git push")

def main():
    """Main function to automate git add, commit, and push 50 times."""
    if len(sys.argv) != 2:
        print("Usage: python auto_commit.py <commit_message>")
        sys.exit(1)

    commit_message = sys.argv[1]
    file_path = "github.txt"

    for i in range(10):
        content = f"This is commit number {i+1}\n"
        update_file(file_path, content)
        git_add()
        git_commit(f"{commit_message} {i+1}")

    git_push()

if __name__ == "__main__":
    main()
