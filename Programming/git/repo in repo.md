https://stackoverflow.com/questions/47008290/git-how-to-make-outer-repository-and-embedded-repository-work-as-common-standal/47031933#47031933

---

You can use below commands to add files from test2 repo to test repo as below:

```
# In local test repo
rm -rf test2
git clone https://github.com/eromoe/test2
git add test2/
git commit -am 'add files from test2 repo to test repo'
git push
```

**Note:**

You should use **`git add test2/`** (with slash, not `git add test2`).

`git add test2/` will treat `test2` folder and it's files as ordinary folder and file for test repo (create mode `100644`).

`git add test2` will treat `test2` folder as a submodule for test repo (create mode `160000`).

---

Probably, git reminded the repository. It helped for me:

    git rm --cached your_folder_with_repo
    git commit -m "remove cached repo"
    git add your_folder_with_repo/
    git commit -m "Add folder"
    git push

---

The solution:

`git rm -f --cached InfoSec/Making/cronenum`
`git add InfoSec/Making/cronenum/`

---

Note! This worked fine for my first one but when I later tried to reproduce it, I failed. Meanin one repo is double but the others are not included in this one.

---


log:

```sh
C:\Obsidian>git rm --cached InfoSec/Making/cronenum
error: the following file has staged content different from both the
file and the HEAD:
InfoSec/Making/cronenum
(use -f to force removal)

C:\Obsidian>git rm -f --cached InfoSec/Making/cronenum
rm 'InfoSec/Making/cronenum'

C:\Obsidian>git status
On branch main
Your branch is up to date with 'Obsidian/main'.

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: .obsidian/community-plugins.json
new file: .obsidian/plugins/obsidian-plaintext/data.json
new file: .obsidian/plugins/obsidian-plaintext/main.js
new file: .obsidian/plugins/obsidian-plaintext/manifest.json
modified: InfoSec/Making/Tools to make.md
new file: InfoSec/Making/parsepasswd/passwdcheck.py
new file: InfoSec/Making/parsepasswd/passwdcheck2.py
modified: Programming/git/git.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
InfoSec/Making/cronenum/
Programming/git/repo in repo.md

C:\Obsidian>git add InfoSec/Making/cronenum/
warning: LF will be replaced by CRLF in InfoSec/Making/cronenum/README.md.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in InfoSec/Making/cronenum/cronenum.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in InfoSec/Making/cronenum/importtest.py.
The file will have its original line endings in your working directory

C:\Obsidian>git status
On branch main
Your branch is up to date with 'Obsidian/main'.

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: .obsidian/community-plugins.json
new file: .obsidian/plugins/obsidian-plaintext/data.json
new file: .obsidian/plugins/obsidian-plaintext/main.js
new file: .obsidian/plugins/obsidian-plaintext/manifest.json
modified: InfoSec/Making/Tools to make.md
new file: InfoSec/Making/cronenum/.gitignore
new file: InfoSec/Making/cronenum/README.md
new file: InfoSec/Making/cronenum/cronenum.py
new file: InfoSec/Making/cronenum/importtest.py
new file: InfoSec/Making/parsepasswd/passwdcheck.py
new file: InfoSec/Making/parsepasswd/passwdcheck2.py
modified: Programming/git/git.md

Untracked files:
(use "git add <file>..." to include in what will be committed)
Programming/git/repo in repo.md

C:\Obsidian>git add .
warning: LF will be replaced by CRLF in Programming/git/repo in repo.md.
The file will have its original line endings in your working directory

C:\Obsidian>git status
On branch main
Your branch is up to date with 'Obsidian/main'.

Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: .obsidian/community-plugins.json
new file: .obsidian/plugins/obsidian-plaintext/data.json
new file: .obsidian/plugins/obsidian-plaintext/main.js
new file: .obsidian/plugins/obsidian-plaintext/manifest.json
modified: InfoSec/Making/Tools to make.md
new file: InfoSec/Making/cronenum/.gitignore
new file: InfoSec/Making/cronenum/README.md
new file: InfoSec/Making/cronenum/cronenum.py
new file: InfoSec/Making/cronenum/importtest.py
new file: InfoSec/Making/parsepasswd/passwdcheck.py
new file: InfoSec/Making/parsepasswd/passwdcheck2.py
modified: Programming/git/git.md
new file: Programming/git/repo in repo.md

C:\Obsidian>git commit -m "Hopefully got cronenum back into the repo"
[main 48db376] Hopefully got cronenum back into the repo
13 files changed, 2338 insertions(+), 3 deletions(-)
create mode 100644 .obsidian/plugins/obsidian-plaintext/data.json
create mode 100644 .obsidian/plugins/obsidian-plaintext/main.js
create mode 100644 .obsidian/plugins/obsidian-plaintext/manifest.json
create mode 100644 InfoSec/Making/cronenum/.gitignore
create mode 100644 InfoSec/Making/cronenum/README.md
create mode 100644 InfoSec/Making/cronenum/cronenum.py
create mode 100644 InfoSec/Making/cronenum/importtest.py
create mode 100644 InfoSec/Making/parsepasswd/passwdcheck.py
create mode 100644 InfoSec/Making/parsepasswd/passwdcheck2.py
create mode 100644 Programming/git/repo in repo.md

C:\Obsidian>git push
Enumerating objects: 32, done.
Counting objects: 100% (32/32), done.
Delta compression using up to 8 threads
Compressing objects: 100% (20/20), done.
Writing objects: 100% (23/23), 36.52 KiB | 6.09 MiB/s, done.
Total 23 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 4 local objects.
To https://github.com/SofiaEngvall/Obsidian.git
cf7cd5b..48db376 main -> main

C:\Obsidian>git status
On branch main
Your branch is up to date with 'Obsidian/main'.

nothing to commit, working tree clean

C:\Obsidian>git status
On branch main
Your branch is up to date with 'Obsidian/main'.

Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified: InfoSec/Making/cronenum/README.md
modified: InfoSec/Making/cronenum/cronenum.py

no changes added to commit (use "git add" and/or "git commit -a")

C:\Obsidian>git add .
warning: LF will be replaced by CRLF in InfoSec/Making/cronenum/README.md.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in InfoSec/Making/cronenum/cronenum.py.
The file will have its original line endings in your working directory

C:\Obsidian>
```
