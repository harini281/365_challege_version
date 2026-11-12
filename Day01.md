Git and GitHub Notes

12 November 2026


Git is a version control system that runs on your own computer. It records the history of your files, so if you change something today and break it, you can go back to an earlier working version.

GitHub is a website that stores Git repositories online. It works as a backup, and it lets many people work on the same project and share their changes.

The main commands

git init turns a folder into a local Git repository. It creates a hidden .git folder that stores the history.

.gitignore is a file where you list what Git should not track, such as node_modules/, .env files, and build folders.

git add moves your changed files into the staging area, which is the list of changes that will go into the next commit. It does not send anything to GitHub.

git commit saves a snapshot of the staged changes in your local repo, with a message describing what you changed. This also stays on your computer.

git push uploads your local commits to GitHub.

How to set it up and use it
bash
# One time setup: tell Git who you are
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Inside your project folder
git init

# Create a .gitignore file and add things like:
# node_modules/
# .env

git add .
git commit -m "Initial commit: describe what you built"



git branch -M main
git push -u origin main


bash
git add .
git commit -m "Describe the change"
git push