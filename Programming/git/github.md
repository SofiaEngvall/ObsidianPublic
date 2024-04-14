
### **Quick setup** — if you’ve done this kind of thing before

**or**

Get started by [creating a new file](https://github.com/SofiaEngvall/Obsidian/new/main) or [uploading an existing file](https://github.com/SofiaEngvall/Obsidian/upload). We recommend every repository include a [README](https://github.com/SofiaEngvall/Obsidian/new/main?readme=1), [LICENSE](https://github.com/SofiaEngvall/Obsidian/new/main?filename=LICENSE.md), and [.gitignore](https://github.com/SofiaEngvall/Obsidian/new/main?filename=.gitignore).

### …or create a new repository on the command line

echo "# Obsidian" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SofiaEngvall/Obsidian.git
git push -u origin main

### …or push an existing repository from the command line

git remote add origin https://github.com/SofiaEngvall/Obsidian.git
git branch -M main
git push -u origin main

### …or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.




Example:
C:\Users\sofia>cd C:\Obsidian

C:\Obsidian>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .gitignore
        new file:   .obsidian/app.json
        new file:   .obsidian/appearance.json
        ...
        new file:   Obsidian/Obsidian.md
        new file:   Obsidian/embedded.png
        new file:   Obsidian/link.md
        new file:   readme.md


C:\Obsidian>git commit -m "Initial commit of my new obsidian notes repo"
[master (root-commit) c29072a] Initial commit of my new obsidian notes repo
 268 files changed, 6929 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 .obsidian/app.json
 create mode 100644 .obsidian/appearance.json
 ...
 create mode 100644 Obsidian/Obsidian.md
 create mode 100644 Obsidian/embedded.png
 create mode 100644 Obsidian/link.md
 create mode 100644 readme.md

C:\Obsidian>git status
On branch master
nothing to commit, working tree clean

C:\Obsidian>git remote add Obsidian https://github.com/SofiaEngvall/Obsidian.git

C:\Obsidian>git branch -M main

C:\Obsidian>git push -u Obsidian main
Enumerating objects: 314, done.
Counting objects: 100% (314/314), done.
Delta compression using up to 8 threads
Compressing objects: 100% (273/273), done.
Writing objects: 100% (314/314), 44.67 MiB | 5.14 MiB/s, done.
Total 314 (delta 16), reused 0 (delta 0)
remote: Resolving deltas: 100% (16/16), done.
To https://github.com/SofiaEngvall/Obsidian.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'Obsidian'.


C:\Obsidian>git push
Enumerating objects: 1374, done.
Counting objects: 100% (1374/1374), done.
Delta compression using up to 8 threads
Compressing objects: 100% (1257/1257), done.
Writing objects: 100% (1373/1373), 62.91 MiB | 6.56 MiB/s, done.
Total 1373 (delta 48), reused 0 (delta 0)
remote: Resolving deltas: 100% (48/48), done.
To https://github.com/SofiaEngvall/Obsidian.git
   c29072a..2a96892  main -> main
