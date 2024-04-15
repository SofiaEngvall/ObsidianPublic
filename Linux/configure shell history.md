https://superuser.com/questions/137438/how-to-unlimited-bash-shell-history
https://stackoverflow.com/questions/9457233/unlimited-bash-history

After many large, ugly iterations and weird edge cases over the years, I now have a concise section of [my `.bashrc`](https://github.com/fotinakis/bashrc/blob/master/init.sh#L46) dedicated to this.

First, you must comment out or **remove this section of your `.bashrc`** (default for Ubuntu). If you don't, then certain environments (like running `screen` sessions) will still truncate your history:

```bash
# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
# HISTSIZE=1000
# HISTFILESIZE=2000
```

Second, **add this** to the bottom of your .bashrc:

```bash
# Eternal bash history.
# ---------------------
# Undocumented feature which sets the size to "unlimited".
# http://stackoverflow.com/questions/9457233/unlimited-bash-history
export HISTFILESIZE=
export HISTSIZE=
export HISTTIMEFORMAT="[%F %T] "
# Change the file location because certain bash sessions truncate .bash_history file upon close.
# http://superuser.com/questions/575479/bash-history-truncated-to-500-lines-on-each-login
export HISTFILE=~/.bash_eternal_history
# Force prompt to write history after every command.
# http://superuser.com/questions/20900/bash-history-loss
PROMPT_COMMAND="history -a; $PROMPT_COMMAND"
```

**Note:** every command is written immediately after it's run, so if you accidentally paste a password you cannot just "`kill -9 %%`" to avoid the history write, you'll need to remove it manually.

Also note that each bash session will load the full history file in memory, but even if your history file grows to 10MB (which will take a _long, long_ time) you won't notice much of an effect on your bash startup time.

---

- Bash truncates the history file during start up so you _must_ comment out the default settings in .bashrc. Merely overriding the settings later in your own custom rc file will just leave you with the fruistrating situation where it looks like bash isn't respecting your changes to the history storage configuration.
    
    – [studog](https://stackoverflow.com/users/1352761/studog "1,028 reputation")
    
    [Nov 17, 2017 at 15:14](https://stackoverflow.com/questions/9457233/unlimited-bash-history#comment81659829_19533853)
    
- 10
    
    Many thanks - the fact that **setting `HISTFILESIZE` (and possibly `HISTSIZE`) will take _immediate_ effect _cannot_ be overemphasized**.
    
    – [Attie](https://stackoverflow.com/users/1347519/attie "6,869 reputation")
    
    [May 21, 2018 at 11:18](https://stackoverflow.com/questions/9457233/unlimited-bash-history#comment87908745_19533853)
