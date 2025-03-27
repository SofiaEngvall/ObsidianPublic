
```sh
NAME
       unrar - extract files from rar archives

SYNOPSIS
       unrar command [-switch ...] archive [file ...] [@listfiles ...] [path ...] [path_to_extract/]

DESCRIPTION
       This manual page documents briefly the unrar command.
       This  manual page was written for the Debian GNU/Linux distribution because the original program does not have a man‐
       ual page.
       Commands and options described here are as of unrar 6.0.

USAGE
       archive
              Archive file name in RAR or other supported format.  If archive file uses RAR multiple volume format,  specify
              only first volume file name as archive file name.

       file ...
              File path name to extract.  You can specify more path names at one time.

       @listfiles ...
              If  argument  starts  with "@", unrar uses listfile as file path list file.  This list file includes file path
              list to extract from archive file.  You can use 2 or more list files at one time.
              File list uses one line for one file path.  And blank line is ignored.
              This file is used to extract many file path names in one time that your shell can´t accept.

       path_to_extract
              If last argument is ended with "/", unrar uses path_to_extract as file extraction target path.

OMMANDS
       After the program name comes a command and then optional switches with dashes before them.  A summary of commands  is
       included below.  For a complete description, run unrar without options.

       e      Extract files to current directory.

       l[t[a],b]
              List archive content [technical[all], bare].

       p      Print file to stdout.

       t      Test archive files.

       v[t[a],b]
              Verbosely list archive [technical[all], bare].

       x      Extract files with full path.

OPTIONS
       NOTE: Every switch must be separated by a whitespace.  You cannot put them together.

       -      Stop switches scanning.

       @[+]   Disable [enable] file lists.

       -ad[1,2]
              Alternate destination path

       -ag[format]
              Generate archive name using the current date.
       -ai    Ignore file attributes.

       -ap<path>
              Set path inside archive.

       -c-    Disable comments show.

       -cfg-  Disable read configuration.

       -cl    Convert names to lower case.

       -cu    Convert names to upper case.

       -dh    Open shared files.

       -ep    Exclude paths from names.

       -ep3   Expand paths to full name.

       -f     Freshen files.

       -id[c,d,n,p,q]
              Display or disable messages.

       -kb    Keep broken extracted files.

       -ierr  Send all messages to stderr.

       -inul  Disable all messages.
              -n<file>
              Additionally filter included files.

       -n@    Read additional filter masks from stdin.

       -n@<list>
              Read additional filter masks from list file.

       -o+    Overwrite existing files.

       -o-    Do not overwrite existing files.

       -ol[a] Process symbolic links as the link [absolute paths].

       -or    Rename files automatically.

       -ow    Save or restore file owner and group.

       -ppassword
              Set password.

       -p-    Do not query password.

       -r     Recurse subdirectories.

       -sc<chr>[obj]
              Specify the character set.

       -sl<size>

              Process files with size less than specified.

       -sm<size>
              Process files with size more than specified.

       -ta[mcao]<d>
              Process files modified after <d> YYYYMMDDHHMMSS date.

       -tb[mcao]<d>
              Process files modified before <d> YYYYMMDDHHMMSS date.

       -tn[mcao]<t>
              Process files newer than <t> time.

       -to[mcao]<t>
              Process files older than <t> time.

       -ts[m,c,a,p]
              Save or restore time (modification, creation, access, preserve).

       -u     Update files.

       -v     List all volumes.

       -ver[n]
              File version control.

       -vp    Pause before each volume.

       -x<file>
              Exclude specified file.

       -x@<list>
              Exclude files in specified list file.

       -x@    Read file names to exclude from stdin.

       -y     Assume Yes on all queries.

FILES
       $HOME/.rarrc

       /etc/.rarrc

       /etc/rar/.rarrc

       /usr/lib/.rarrc

       /usr/local/lib/.rarrc

       /usr/local/etc/.rarrc
              UnRAR (and RAR) configuration file.

       Syntax: (switches for all commands)
              switches=<any RAR switches separated by spaces>

       Syntax: (switches for specific command)
              switches_<command>=<any RAR switches separated by spaces>

       Example:
              switches=-m5 -s
              switches_a=-m5 -s
              switches_x=-o+

AUTHORS
       This manual page was written by Petr Cech <cech@debian.org> according to "unrar" for the Debian GNU/Linux system (but
       may be used by others).

```