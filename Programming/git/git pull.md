
to merge your current computer with github

1. there are no changes on the computer you're currently on so you don't have to merge:

`git checkout HEAD^ file/to/overwrite`
this will move the file back to the state it had at the last commit/pull
useful for config files like .obsidian/core-plugins.json that seem to update when the program is opened

`git pull`

Example:

```sh
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git pull   
Updating 81aafe1..38cd87b
error: Your local changes to the following files would be overwritten by merge:
        .obsidian/core-plugins.json
Please commit your changes or stash them before you merge.
Aborting
                                                                                                               
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git pull -f
Updating 81aafe1..38cd87b
error: Your local changes to the following files would be overwritten by merge:
        .obsidian/core-plugins.json
Please commit your changes or stash them before you merge.
Aborting
                                                                                                               
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git merge  
Updating 81aafe1..38cd87b
error: Your local changes to the following files would be overwritten by merge:
        .obsidian/core-plugins.json
Please commit your changes or stash them before you merge.
Aborting
                                                                                                               
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git checkout HEAD^ .obsidian/core-plugins.json
Updated 1 path from b22cd18
                                                                                                               
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git pull                                      
Updating 81aafe1..38cd87b
Updating files: 100% (2320/2320), done.
Fast-forward
 .obsidian/app.json                                                     |     6 +-
 .obsidian/appearance.json                                              |     6 +-
 .obsidian/community-plugins.json                                       |     5 +-
 .obsidian/core-plugins-migration.json                                  |    12 +-
 .obsidian/core-plugins.json                                            |    51 +-
...
```


```sh
┌──(fixit㉿asusx555b)-[~/ObsidianPublic]
└─$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

2. to totally delete all changes on the local machine

```sh
git stash
git stash drop
git pull
```

3. there are files that are newer on your machine and files that are newer on github

assuming - to test
```
git add .
git commit -m "changes on computer 2"
git pull ??? or maybe merge this is a test to see if thil will be merged
```

