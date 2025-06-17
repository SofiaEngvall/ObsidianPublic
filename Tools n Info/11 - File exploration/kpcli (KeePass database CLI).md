
`kpcli --kdb=passcodes.kdbx`
will ask for the password

| Command              | Action                                                              |
| -------------------- | ------------------------------------------------------------------- |
| `ls`                 | List groups/entries in current folder                               |
| `cd /`               | Go to root folder                                                   |
| `cd GroupName`       | Enter a subgroup (e.g., `cd Network`)                               |
| `find .`             | Recursively search **all** entries                                  |
| `show -f EntryName`  | Show details of a specific entry (title, username, password, notes) |
| `export -f dump.txt` | Export **all** entries to a text file                               |

### Help

```sh
┌──(kali㉿proxli)-[~/boxes/htb/keeper]
└─$ kpcli --help
Usage: kpcli [--kdb=<file.kdb>] [--key=<file.key>]

  --kdb=s        Optional KeePass database file to open (must exist).
  --key=s        Optional KeePass key file (must exist).
  --pwfile=s     Read master password from file instead of console.
  --histfile=s   Specify your history file (or perhaps /dev/null).
  --readonly     Run in read-only mode; no changes will be allowed.
  --timeout=i    Lock interface after i seconds of inactivity.
  --command=s    Run a command and exit (no interactive session).
                 Multiple --command parameters can be used.
  --no-recycle   Don´t store entry changes in /Backup or "/Recycle Bin".
  --pwwords=s    File of words for building word-based passwords.
  --pwsplchars=s The special characters used in password generation.
  --pwlen=i      Length of generated passwords (default is 20).
  --pwscmin=i    Min number of special chars in generated passwords.
  --pwscmax=i    Max number of special chars in generated passwords.
  --nopwstars    Don´t show star characters (*) for password input.
  --nopwprint    Don´t print the pw red on red in the show command.
  --xpxsecs=i    Seconds to wait until clearing the clipboard for xpx.
  --xclipsel=s   X11 clipboard to use; "--xclipsel help" for choices.
  --kpxcexe=s    Path to a KeePassXC binary, used to import KDBX4 files.
  --help         This message.

Run kpcli with no options and type 'help' at its command prompt to learn
about kpcli´s commands.
```

### Help show

```sh
kpcli:/passcodes/Network> help show
show: Show an entry: show [-f] [-a] <entry path|entry number>

The show command tries to intelligently determine
what you want to see and to make it easy to display.
Show can take a path to an entry as its argument or
an entry number as shown by the ls command.

When using entry numbers, they will refer to the last
path when an ls was performed or pwd if ls has not
yet been run.

By default, passwords are "hidden" by being displayed as
"red on red" where they can be copied to the clip board
but not seen. Provide the -f option to show passwords.
Use the -a option to see create and modified times, and
the index of the icon set for the entry.
```