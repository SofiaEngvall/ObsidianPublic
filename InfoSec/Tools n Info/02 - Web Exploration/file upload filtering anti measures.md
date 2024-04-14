
## Where's the filter
### Client-side

Usually javascript

Can be easily circumvented since it's run on our machine

We can both see the code and send whatever we want to the server

### Server side

Usually php but can be C#, Node.js, Python, Ruby on Rails...

You can't see the code or affect how it is run - We need to make a payload that can slip through

## Filtering types
### Extension filtering

Extensions can be whitelisted or blacklisted in the filter = They either list what's allowed or what is not allowed

### File type filtering

##### MIME

MIME (**M**ultipurpose **I**nternet **M**ail **E**xtension) types are used to identify file type in emails and in http transfers

In a http request header it looks like:
`Content-Type: image/jpeg`

This is usually based on the file extension, even server side.

##### Magic Number validation

At the start of a file there is a specific string of bytes
This is also how unix ids file types

PNG    89 50 4E 47  0D 0A 1A 0A    .PNG.
GIF      47 49 46 38 37 61   
JPG      FF D8 FF DB    

You can easily see this in a file editor and it can of course be changed but the file might not work as intended when changed

https://en.wikipedia.org/wiki/List_of_file_signatures
### File Length filtering

If a small file is expected for the upload there might be a size limitation

### File Name Filtering

File names might be changed when uploaded
- to make sure the file name is unique
- to sanitize bad/odd characters (null, forward slashes, other control characters)

But they might not too

### File content Filtering

Full contents of the file might be scanned to make sure the extension, mime type and magic number is correct and not modified.


## Exploits

### PHP

Until ver 5, you could bypass extension filtering by appending a null byte and a valid extension

### Image exif data

It was possible to inject PHP code into the exif data of an image


### Getting around Client Side Filtering

1 - We can turn off javascript
2 - Intercept and modify the incoming page
  Turn on Intercept in the Burp proxy, reload the page and when it popps up in Intercept, right click and choose "Do Intercept", "Response to this request", click Forward
  ![[Pasted image 20240211000203.png|500]]
  And edit the code to remove the filter, then click Forward again and the filter will be disabled in the normal browser
  If you need to edit js files loaded by the page you need to go to the options tab, "Intercept Client Requests" and add `^js$|` to the list of file extensions
3 - Intercept and modify the file upload
  If the blockage is on selecting a file, select a file that matches the filter. Then before clicking upload or similar, turn on burp proxy intercept and edit the mimetype and filename to by your exploit instead. Or just have intercept on all the time
  Then we can run gobusted to find the location of the script so we can run it. Don't forget to turn on nc it it's a rev sh.
4 - Send the file using a tool like curl
  Like: `curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>`
  Get the parameters by using burp or the browser console

### Getting around Server Side Filtering

THM: to look into more

Assuming that our malicious file upload has been stopped by the server, here are some ways to ascertain what kind of server-side filter may be in place:

- If you can successfully upload a file with a totally invalid file extension (e.g. `testingimage.invalidfileextension`) then the chances are that the server is using an extension _blacklist_ to filter out executable files. If this upload fails then any extension filter will be operating on a whitelist.
- Try re-uploading your originally accepted innocent file, but this time change the magic number of the file to be something that you would expect to be filtered. If the upload fails then you know that the server is using a magic number based filter.
- As with the previous point, try to upload your innocent file, but intercept the request with Burpsuite and change the MIME type of the upload to something that you would expect to be filtered. If the upload fails then you know that the server is filtering based on MIME types.
- Enumerating file length filters is a case of uploading a small file, then uploading progressively bigger files until you hit the filter. At that point you'll know what the acceptable limit is. If you're very lucky then the error message of original upload may outright tell you what the size limit is. Be aware that a small file length limit may prevent you from uploading the reverse shell we've been using so far.  
    
You should now be well equipped to take on the challenge in task eleven.

own notes:

