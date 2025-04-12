
YARA is tool that identifies and classifies files based on their content, helping malware researchers and lots of others.

http://virustotal.github.io/yara/
https://github.com/VirusTotal/yara

Great info doc
https://n3nu.medium.com/getting-started-with-yara-a-beginners-guide-to-understanding-and-creating-yara-rules-73bda308fd98

https://yara.readthedocs.io/en/stable/writingrules.html

`sudo apt install yara`

[[loki]] runs yara rules


### Running yara

`yara rule.yar file_to_test`

`yara file2.yar file2/1ndex.php`


testing with a simple condition true = does the file exist

when there's a file
```shell-session
cmnatic@thm:~$ yara myfirstrule.yar somefile 
examplerule somefile
```

with no file
```sh
cmnatic@thm:~$ yara myfirstrule.yar sometextfile
error scanning sometextfile: could not open file
```

### Modules

https://github.com/cuckoosandbox/cuckoo automated malware analysis environment
https://pypi.org/project/pefile/


### Rules and more

https://github.com/InQuest/awesome-yara
pen testing https://github.com/DiabloHorn/yara4pentesters/blob/master/juicy_files.txt
forensics https://github.com/Xumeiquer/yara-forensics

Generate rules: https://github.com/Neo23x0/yarGen [[yarGen]]

To read
- https://www.bsk-consulting.de/2015/02/16/write-simple-sound-yara-rules/    
- https://www.bsk-consulting.de/2015/10/17/how-to-write-simple-but-sound-yara-rules-part-2/
- https://www.bsk-consulting.de/2016/04/15/how-to-write-simple-but-sound-yara-rules-part-3/

### Commands and rules

A Yara **command**:
- A Yara Rule file
- A file or directory name or a process ID

Ex. `yara myrule.yar somedirectory`


A Yara **rule** (in yaml): 
- A name
- A condition

```yaml
rule examplerule {
        condition: true
}
```
This rule only checks if the file exists


#### Strings

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!"

	condition:
		$hello_world
}
```
checks if the text "Hello World!" is in the file

for hex use $my_hex_string = { 00 00 54 }


### Conditions

- true
- any of them
- <= (less than or equal to)
- >= (more than or equal to)
- != (not equal to)

Combine conditions with:
- and
- not
- or

#### Any of them

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!"
		$hello_world_lowercase = "hello world"
		$hello_world_uppercase = "HELLO WORLD"

	condition:
		any of them
}
```
will match all strings :O


### Number of matches

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!"

	condition:
        #hello_world <= 10
}
```
matches if there are less than or equal to ten occurrences of the "Hello World!" string


### Filesize

```yaml
rule helloworld_checker{
	strings:
		$hello_world = "Hello World!" 
        
        condition:
	        $hello_world and filesize < 10KB 
}
```
contains "Hello World!" and is bigger than 10kB





















![[Images/Pasted image 20250408210940.png]]

