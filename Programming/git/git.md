
### Quick ref

echo "# logPublicIP" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SofiaEngvall/logPublicIP.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/SofiaEngvall/logPublicIP.git
git branch -M main
git push -u origin main

## Git

A version control system
Made by Linus Thorwalds
GitHub - Microsoft
GitLab - GitLab Inc
GifLab has more features, DevOps..

repository a tree of files synchronized using a version control system
commit a checkpoint in the version control system
staging area a list of files that will be committed when the commit command is run
branch a separately tracked version of the repository

To install Git run:
`sudo apt update`
`sudo apt install git`
`git --version`

Add used info:  
`git config --global user.name "Sofia Engvall"`
`git config --global user.email "sofia@fixit42.com"`
`git config --list`
`nano ~/.gitconfig`


Go to your new project directory and run `git init` to start a new repository = start syncing the directory. This creates a hidden .git subdir where info about the repository is stored.

Run `git status` to get info on changes to the directory. New and updated files that have not been committed, a list of files in the staging area = the files that would be committed if you ran commit now.

When new files have been made, run `git add <filename/s>` to add files to the staging area. `git add .` adds all changes that were listed by git status.  

Remove files from the staging area with `git rm --cached <file>...`.

When files have been added, you can create a commit, a checkpoint in the version control system:  
`git commit -m "Commit log message"`

when we commit, [[diff]] files (listing the difference between the files) are created for the files in the staging area
this means that the difference between the old version of the file and the new version of a file is saved in the .git directory

you may set an editor using
`git config --global core.editor`

commit message format
Fixes issue #3 by updating \<filename\> to include/do...
- Modified: \<filename\>
- Fix: issue #3

We can sync our local git repository to a remote site... or to several sites
first `git branch -M main`
first add a project/repo on the remote site/s
then add the remote/s with: `git remote add <name> <url>` where `<name>` is usually origin
to push this the first time to the remote, use `git push -u origin main`

Another way to set up the connection is to clone an existing repo: `git clone <url>` (don't do `git init`...)
when doing this the project url is automatically set up as a remote

git remote remove
git remote branch

`git push` pushes the local repository (all new commits) to our cloud repository - syncs local to remote

`git pull` pulls from the remote to out local repo (all new commits in ONE branch) and merges with it - syncs & merges __automatically__ remote to local

`git fetch` pull but without merge, you can see how a merge would affect your local files, update them and then merge all or some commits at a later stage - more control
`git merge`



To get a log of previous commits, run: `git log`. This information includes the hash-codes for each commit.  

To go back to a previously committed version, run `git checkout <commit-hash>`
This takes you off the master branch
To save this as a separate branch to make changes in, run `git checkout -b <new-branch name>`

To get back to the master branch, run `git checkout master`

To list all branches, run `git branch`

To make a new branch at any time, run `git branch <new-branch name>`. Observe that this does not switch to the branch but makes a copy of the current branch with a new name. (Same as `git checkout -b <new-branch name>` but without checking the branch out)

You might use a branch to test new things. When these are tested, to merge them to the master branch, run `git merge <branch-name>`


Remove all from staging area `git reset HEAD --`
File: `git reset HEAD -- <file>`
Dir: `git reset HEAD -- <directoryName>`


[How To Install Git on Debian 10 | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-debian-10#setting-up-git)
[How To Use Git Effectively | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-git-effectively)
[How To Use Git Branches | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-git-branches)

[Introduction to Git](https://www.notion.so/zarkom/Introduction-to-Git-ac396a0697704709a12b6a0e545db049)

### Command  line help

```sh
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```