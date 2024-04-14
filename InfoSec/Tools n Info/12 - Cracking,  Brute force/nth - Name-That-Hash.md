
https://github.com/HashPals/Name-That-Hash

https://nth.skerritt.blog/

sudo apt install name-that-hash


```sh
┌──(kali㉿kali)-[~]
└─$ nth --help                                                                                                    
Usage: nth [OPTIONS]

  Name That Hash - Instantly name the type of any hash!

  Github:

  https://github.com/hashpals/name-that-hash

  From the creator of RustScan and Ciphey. Follow me on Twitter!

  https://twitter.com/bee_sec_san

  Example usage:

      nth --text '5f4dcc3b5aa765d61d8327deb882cf99'

      nth --file hash

      nth --text '5f4dcc3b5aa765d61d8327deb882cf99' --greppable

      Note: Use single quotes ' as inverted commas " do not work well on
      Linux.

Options:
  -t, --text TEXT      Check one hash, use single quotes ' as inverted commas
                       " messes up on Linux.
  -f, --file FILENAME  Checks every hash in a newline separated file.
  -g, --greppable      Are you going to grep this output? Prints in JSON
                       format.
  -b64, --base64       Decodes hashes in Base64 before identification. For
                       files with mixed Base64 & non-encoded it attempts
                       base64 first and then falls back to normal hash
                       identification per hash.
  -a, --accessible     Turn on accessible mode, does not print ASCII art. Also
                       does not print very large blocks of text, as this can
                       cause some pain with screenreaders. This reduces the
                       information you get. If you want the least likely
                       feature but no banner, use --no-banner.
  -e, --extreme        Searches for hashes within a string. This mode will get
                       5d41402abc4b2a76b9719d911017c592 from
                       ####5d41402abc4b2a76b9719d911017c592###
  --no-banner          Removes banner from startup.
  --no-john            Don't print John The Ripper Information.
  --no-hashcat         Don't print Hashcat Information.
  -v, --verbose        Turn on debugging logs. -vvv for maximum logs.
  --help               Show this message and exit.
```

```sh
┌──(kali㉿kali)-[~]
└─$ nth --text '$6$Uk8SVGLsBuSmD75R$WE.iZ9ZkzBS21Us7QuYg54amvZ3YjcWTu8LiQ2VZx1/fs.kRbvPnvwQw6T5Rtr6UdaXso7zT1KdsNJAOzmrwF1'

  _   _                           _____ _           _          _   _           _     
 | \ | |                         |_   _| |         | |        | | | |         | |    
 |  \| | __ _ _ __ ___   ___ ______| | | |__   __ _| |_ ______| |_| | __ _ ___| |__  
 | . ` |/ _` | '_ ` _ \ / _ \______| | | '_ \ / _` | __|______|  _  |/ _` / __| '_ \ 
 | |\  | (_| | | | | | |  __/      | | | | | | (_| | |_       | | | | (_| \__ \ | | |
 \_| \_/\__,_|_| |_| |_|\___|      \_/ |_| |_|\__,_|\__|      \_| |_/\__,_|___/_| |_|

https://twitter.com/bee_sec_san
https://github.com/HashPals/Name-That-Hash 

$6$Uk8SVGLsBuSmD75R$WE.iZ9ZkzBS21Us7QuYg54amvZ3YjcWTu8LiQ2VZx1/fs.kRbvPnvwQw6T5Rtr6UdaXso7zT1KdsNJAOzmrwF1

Most Likely 
SHA-512 Crypt, HC: 1800 JtR: sha512crypt
```