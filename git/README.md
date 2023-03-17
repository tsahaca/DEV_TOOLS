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
  
