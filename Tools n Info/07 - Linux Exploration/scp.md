
`scp -i id_rsa annie@10.10.245.157:/home/annie/Pictures/redhead-annie-1389225_960_720.jpg .`
`scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .`
`scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt`
`scp -r user1@10.10.38.138:~ .`
## Help

```sh
usage: scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config]
           [-i identity_file] [-J destination] [-l limit] [-o ssh_option]
           [-P port] [-S program] [-X sftp_option] source ... target
```

man
```sh
## Name

**scp** - secure copy (remote file copy program)

## Synopsis

**scp** [**-1246BCpqrv**] [**-c** _cipher_] [**-F** _ssh_config_] [**-i** _identity_file_] [**-l** _limit_] [**-o** _ssh_option_] [**-P** _port_] [**-S** _program_] [

         [_user_@]_host1_:]_file1 ..._ [                                    [_user_@]_host2_:]_file2_

## Description

**scp** copies files between hosts on a network. It uses **[ssh](https://linux.die.net/man/1/ssh)**(1) for data transfer, and uses the same authentication and provides the same security as **[ssh](https://linux.die.net/man/1/ssh)**(1). Unlike **[rcp](https://linux.die.net/man/1/rcp)**(1), **scp** will ask for passwords or passphrases if they are needed for authentication.

File names may contain a user and host specification to indicate that the file is to be copied to/from that host. Local file names can be made explicit using absolute or relative pathnames to avoid **scp** treating file names containing ':' as host specifiers. Copies between two remote hosts are also permitted.

When copying a source file to a target file which already exists, **scp** will replace the contents of the target file (keeping the inode).

If the target file does not yet exist, an empty file with the target file name is created, then filled with the source file contents. No attempt is made at "near-atomic" transfer using temporary files.

The options are as follows:

      **-1**'        Forces **scp** to use protocol 1.

**-2**' Forces **scp** to use protocol 2.

**-4**' Forces **scp** to use IPv4 addresses only.

**-6**' Forces **scp** to use IPv6 addresses only.

**-B**' Selects batch mode (prevents asking for passwords or passphrases).

**-C**' Compression enable. Passes the **-C** flag to **[ssh](https://linux.die.net/man/1/ssh)**(1) to enable compression.

**-c** _cipher_  
Selects the cipher to use for encrypting the data transfer. This option is directly passed to **[ssh](https://linux.die.net/man/1/ssh)**(1).

**-F** _ssh_config_  
Specifies an alternative per-user configuration file for **ssh**. This option is directly passed to **[ssh](https://linux.die.net/man/1/ssh)**(1).

**-i** _identity_file_  
Selects the file from which the identity (private key) for public key authentication is read. This option is directly passed to **[ssh](https://linux.die.net/man/1/ssh)**(1).

**-l** _limit_  
Limits the used bandwidth, specified in Kbit/s.

**-o** _ssh_option_  
Can be used to pass options to **ssh** in the format used in **[ssh_config](https://linux.die.net/man/5/ssh_config)**(5). This is useful for specifying options for which there is no separate **scp** command-line flag. For full details of the options listed below, and their possible values, see **[ssh_config](https://linux.die.net/man/5/ssh_config)**(5).

AddressFamily  
BatchMode  
BindAddress  
ChallengeResponseAuthentication  
CheckHostIP  
Cipher  
Ciphers  
Compression  
CompressionLevel  
ConnectionAttempts  
ConnectTimeout  
ControlMaster  
ControlPath  
GlobalKnownHostsFile  
GSSAPIAuthentication  
GSSAPIDelegateCredentials  
HashKnownHosts  
Host'  
HostbasedAuthentication  
HostKeyAlgorithms  
HostKeyAlias  
HostName  
IdentityFile  
IdentitiesOnly  
KbdInteractiveDevices  
LogLevel  
MACs'  
NoHostAuthenticationForLocalhost  
NumberOfPasswordPrompts  
PasswordAuthentication  
Port'  
PreferredAuthentications  
Protocol  
ProxyCommand  
PubkeyAuthentication  
RekeyLimit  
RhostsRSAAuthentication  
RSAAuthentication  
SendEnv  
ServerAliveInterval  
ServerAliveCountMax  
SmartcardDevice  
StrictHostKeyChecking  
TCPKeepAlive  
UsePrivilegedPort  
User'  
UserKnownHostsFile  
VerifyHostKeyDNS

**-P** _port_  
Specifies the port to connect to on the remote host. Note that this option is written with a capital 'P', because **-p** is already reserved for preserving the times and modes of the file in **[rcp](https://linux.die.net/man/1/rcp)**(1).

**-p**' Preserves modification times, access times, and modes from the original file.

**-q**' Quiet mode: disables the progress meter as well as warning and diagnostic messages from **[ssh](https://linux.die.net/man/1/ssh)**(1).

**-r**' Recursively copy entire directories. Note that **scp** follows symbolic links encountered in the tree traversal.

**-S** _program_  
Name of _program_ to use for the encrypted connection. The program must understand **[ssh](https://linux.die.net/man/1/ssh)**(1) options.

**-v**' Verbose mode. Causes **scp** and **[ssh](https://linux.die.net/man/1/ssh)**(1) to print debugging messages about their progress. This is helpful in debugging connection, authentication, and configuration problems.

The **scp** utility exits 0 on success, and >0 if an error occurs.

**IPV6**

IPv6 address can be used everywhere where IPv4 address. In all entries must be the IPv6 address enclosed in square brackets. Note: The square brackets are metacharacters for the shell and must be escaped in shell.
```