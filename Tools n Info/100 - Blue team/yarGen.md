
https://github.com/Neo23x0/yarGen


`python3 yarGen.py -h`
`python3 yarGen.py --update`

ex.
`python3 yarGen.py -m /home/cmnatic/suspicious-files/file2 --excludegood -o /home/cmnatic/suspicious-files/file2.yar` 
- `-m` is the path to the files you want to generate rules for
- `--excludegood` force to exclude all goodware strings (_these are strings found in legitimate software and can increase false positives_)
- `-o` location & name you want to output the Yara rule

### Example

```sh
cmnatic@thm-yara:~/tools/yarGen$ python3 yarGen.py -m /home/cmnatic/suspicious-files/file2 --excludegood -o /home/cmnatic/suspicious-files/file2.yar
------------------------------------------------------------------------
                   _____            
    __ _____ _____/ ___/__ ___      
   / // / _ `/ __/ (_ / -_) _ \     
   \_, /\_,_/_/  \___/\__/_//_/     
  /___/  Yara Rule Generator        
         Florian Roth, July 2020, Version 0.23.3
   
  Note: Rules have to be post-processed
  See this post for details: https://medium.com/@cyb3rops/121d29322282
------------------------------------------------------------------------
[+] Using identifier 'file2'
[+] Using reference 'https://github.com/Neo23x0/yarGen'
[+] Using prefix 'file2'
[+] Processing PEStudio strings ...
[+] Reading goodware strings from database 'good-strings.db' ...
    (This could take some time and uses several Gigabytes of RAM depending on your db size)
[+] Loading ./dbs/good-imphashes-part9.db ...
[+] Total: 1 / Added 1 entries
[+] Loading ./dbs/good-exports-part6.db ...
[+] Total: 8065 / Added 8065 entries
[+] Loading ./dbs/good-imphashes-part2.db ...
[+] Total: 1056 / Added 1055 entries
[+] Loading ./dbs/good-imphashes-part7.db ...
[+] Total: 4648 / Added 3592 entries
[+] Loading ./dbs/good-imphashes-part1.db ...
[+] Total: 6227 / Added 1579 entries
[+] Loading ./dbs/good-imphashes-part6.db ...
[+] Total: 6256 / Added 29 entries
[+] Loading ./dbs/good-exports-part8.db ...
[+] Total: 22192 / Added 14127 entries
[+] Loading ./dbs/good-strings-part1.db ...
[+] Total: 1416757 / Added 1416757 entries
[+] Loading ./dbs/good-imphashes-part3.db ...
[+] Total: 10035 / Added 3779 entries
[+] Loading ./dbs/good-strings-part9.db ...
[+] Total: 1417513 / Added 756 entries
[+] Loading ./dbs/good-strings-part8.db ...
[+] Total: 1699743 / Added 282230 entries
[+] Loading ./dbs/good-strings-part5.db ...
[+] Total: 5764251 / Added 4064508 entries
[+] Loading ./dbs/good-strings-part6.db ...
[+] Total: 6382068 / Added 617817 entries
[+] Loading ./dbs/good-strings-part3.db ...
[+] Total: 9110194 / Added 2728126 entries
[+] Loading ./dbs/good-exports-part4.db ...
[+] Total: 110911 / Added 88719 entries
[+] Loading ./dbs/good-exports-part5.db ...
[+] Total: 236241 / Added 125330 entries
[+] Loading ./dbs/good-imphashes-part5.db ...
[+] Total: 17205 / Added 7170 entries
[+] Loading ./dbs/good-exports-part3.db ...
[+] Total: 279926 / Added 43685 entries
[+] Loading ./dbs/good-strings-part4.db ...
[+] Total: 10459690 / Added 1349496 entries
[+] Loading ./dbs/good-exports-part9.db ...
[+] Total: 279926 / Added 0 entries
[+] Loading ./dbs/good-exports-part2.db ...
[+] Total: 322362 / Added 42436 entries
[+] Loading ./dbs/good-strings-part2.db ...
[+] Total: 11433382 / Added 973692 entries
[+] Loading ./dbs/good-exports-part1.db ...
[+] Total: 381481 / Added 59119 entries
[+] Loading ./dbs/good-exports-part7.db ...
[+] Total: 404321 / Added 22840 entries
[+] Loading ./dbs/good-imphashes-part8.db ...
[+] Total: 17388 / Added 183 entries
[+] Loading ./dbs/good-imphashes-part4.db ...
[+] Total: 19764 / Added 2376 entries
[+] Loading ./dbs/good-strings-part7.db ...
[+] Total: 12284943 / Added 851561 entries
[+] Processing malware files ...
[+] Processing /home/cmnatic/suspicious-files/file2/1ndex.php ...
[+] Generating statistical data ...
[+] Generating Super Rules ... (a lot of foo magic)
[+] Generating Simple Rules ...
[-] Applying intelligent filters to string findings ...
[-] Filtering string set for /home/cmnatic/suspicious-files/file2/1ndex.php ...
[=] Generated 1 SIMPLE rules.
[=] All rules written to /home/cmnatic/suspicious-files/file2.yar
[+] yarGen run finished
```
### Help

```sh
cmnatic@thm-yara:~/tools/yarGen$ python3 yarGen.py -h
usage: yarGen.py [-h] [-m M] [-y min-size] [-z min-score] [-x high-scoring]
                 [-w superrule-overlap] [-s max-size] [-rc maxstrings]
                 [--excludegood] [-o output_rule_file] [-e output_dir_strings]
                 [-a author] [-r ref] [-l lic] [-p prefix] [-b identifier]
                 [--score] [--strings] [--nosimple] [--nomagic] [--nofilesize]
                 [-fm FM] [--globalrule] [--nosuper] [--update] [-g G] [-u]
                 [-c] [-i I] [--dropzone] [--nr] [--oe] [-fs size-in-MB]
                 [--noextras] [--debug] [--trace] [--opcodes] [-n opcode-num]

yarGen

optional arguments:
  -h, --help            show this help message and exit

Rule Creation:
  -m M                  Path to scan for malware
  -y min-size           Minimum string length to consider (default=8)
  -z min-score          Minimum score to consider (default=0)
  -x high-scoring       Score required to set string as 'highly specific
                        string' (default: 30)
  -w superrule-overlap  Minimum number of strings that overlap to create a
                        super rule (default: 5)
  -s max-size           Maximum length to consider (default=128)
  -rc maxstrings        Maximum number of strings per rule (default=20,
                        intelligent filtering will be applied)
  --excludegood         Force the exclude all goodware strings

Rule Output:
  -o output_rule_file   Output rule file
  -e output_dir_strings
                        Output directory for string exports
  -a author             Author Name
  -r ref                Reference (can be string or text file)
  -l lic                License
  -p prefix             Prefix for the rule description
  -b identifier         Text file from which the identifier is read (default:
                        last folder name in the full path, e.g. "myRAT" if -m
                        points to /mnt/mal/myRAT)
  --score               Show the string scores as comments in the rules
  --strings             Show the string scores as comments in the rules
  --nosimple            Skip simple rule creation for files included in super
                        rules
  --nomagic             Don't include the magic header condition statement
  --nofilesize          Don't include the filesize condition statement
  -fm FM                Multiplier for the maximum 'filesize' condition value
                        (default: 3)
  --globalrule          Create global rules (improved rule set speed)
  --nosuper             Don´t try to create super rules that match against
                        various files

Database Operations:
  --update              Update the local strings and opcodes dbs from the
                        online repository
  -g G                  Path to scan for goodware (dont use the database
                        shipped with yaraGen)
  -u                    Update local standard goodware database with a new
                        analysis result (used with -g)
  -c                    Create new local goodware database (use with -g and
                        optionally -i "identifier")
  -i I                  Specify an identifier for the newly created databases
                        (good-strings-identifier.db, good-opcodes-
                        identifier.db)

General Options:
  --dropzone            Dropzone mode - monitors a directory [-m] for new
                        samples to processWARNING: Processed files will be
                        deleted!
  --nr                  Do not recursively scan directories
  --oe                  Only scan executable extensions EXE, DLL, ASP, JSP,
                        PHP, BIN, INFECTED
  -fs size-in-MB        Max file size in MB to analyze (default=10)
  --noextras            Don´t use extras like Imphash or PE header specifics
  --debug               Debug output
  --trace               Trace output

Other Features:
  --opcodes             Do use the OpCode feature (use this if not enough high
                        scoring strings can be found)
  -n opcode-num         Number of opcodes to add if not enough high scoring
                        string could be found (default=3)
```

