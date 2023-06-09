# [Cheat Sheet](cheatsheet)

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

To stop tracking a file, you need to remove it from the index. This can be achieved with this command   
```bash
git rm -f --cached <file>
```
To remove a whole folder, you need to remove all files in it recursively.
```bash
git rm -f -r --cached <folder>
```
## Required Permissions for Personal Access Tokens
1. repo
2. workflow
3. admin:org -> read:org
4. gist
5. delete_repo

## Adding a corporate (or self-signed) certificate authority to git.exe’s store
```bash
1. Extract the root certificate as a base64-encoded X.509 CER/PEM file
2. git config --get http.sslCAInfo
3. C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
4. copy "C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt" C:\Users\yourname
5. git config --global http.sslCAInfo C:/Users/yourname/ca-bundle.crt
6. Add the exported root certificate to the private copy of the store
```
[Click here for step by step](https://learn.microsoft.com/en-us/archive/blogs/phkelley/adding-a-corporate-or-self-signed-certificate-authority-to-git-exes-store)


