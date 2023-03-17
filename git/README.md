# How to add untracked new project to Github

1. cd to ***<project_folder>***
2. git init -b ***<branch_name>***
3. git add .
4. git config --global user.email ***"you@example.com"***
5. git config --global user.name ***"Your Name"***
6. git commit -m "First commit"
7. git remote add origin ***<repo_url>***
8. git remote -v
9. git push origin ***<branch_name>***

## To remove the SVN associtaion from a project use
```bash
  find . -iname ".svn" -print0 | xargs -0 rm -r
```  

## How to untrack a file which was already added to git index

.gitignore will prevent untracked files from being added (without an add -f) to the set of files tracked by Git, however Git will continue to track any files that are already being tracked.


.Tasks & commands
[options="header,footer"]
|=======================
|Task    |Commands
|To stop tracking a file, you need to remove it from the index. This can be achieved with this command   |git rm -f --cached <file>
|To remove a whole folder, you need to remove all files in it recursively. |git rm -f -r --cached <folder>
|=======================

