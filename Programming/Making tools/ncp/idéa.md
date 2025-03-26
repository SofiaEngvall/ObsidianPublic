downloaded a few files with nc and now I'm thinking I might make a python3 script to simplify this

To start it at both ends

The sending side:
- enumerating the files in a dir recursively
- first sending a text file list of the file names including structure (directories) and file size
- then sending each file in the list
-  The sending sides nc threads will automatically exit when the connection is dropped

The receiving side:
- first getting the file list
- then getting one file at a time
	-  doing the actual nc in a separate thread to be aborted
	-  when a check find the file have reached the known file size
	-  going through and recieveing all the files as they are send

Making it possible to do this more controlled with just a simple nc file transter

Also this being one script with the options "nccp.py send" and "nccp.py receive"

I just realized that the machine doesn't have python and that this is common, so I'll make it an executable

What should I use, c?

I guess a new name is needed ncp for network copy maybe, googling, finding lots of things with this name but nothing similar


