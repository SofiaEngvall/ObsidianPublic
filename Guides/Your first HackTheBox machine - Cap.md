
Cap is an easy Linux machine. We will follow the Guided Mode questions.
To learn, give a question a try before you read the next step in this walkthrough.

### Getting started - nmap

> How many TCP ports are open?

The first thing we usually do is a port scan to on which ports the machine we're supposed to hack are listening on. This can tell us a lot about what programs are running on it. Maybe it is a web server or a file sharing server.

The most common tool used is `nmap`. We will first do a scan of the most common ports, to see how it works. Then we do a longer scan where we also ask nmap to run some extra checks to grab useful information from the machine. Our goal at the start is to find out as much as we possibly can!

Before we start if can be wise to ping the machine. This will work on most Linux machines while some Windows machines have ping turned off. Ping is just a way to see if we have our VPN running as it should. Making sure the machine can "hear" us.

`ping 10.10.10.245`
Replace this ip address with the one listed on hackthebox for you. I will keep using this address as an example, so you just keep replacing it.

The machine should have given you a response looking something like this:
```sh
┌──(kali㉿proxli)-[~/vpn]
└─$ ping 10.10.10.245
PING 10.10.10.245 (10.10.10.245) 56(84) bytes of data.
64 bytes from 10.10.10.245: icmp_seq=1 ttl=63 time=23.6 ms
64 bytes from 10.10.10.245: icmp_seq=2 ttl=63 time=23.1 ms
64 bytes from 10.10.10.245: icmp_seq=3 ttl=63 time=23.4 ms
^C
--- 10.10.10.245 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2001ms
rtt min/avg/max/mdev = 23.077/23.346/23.579/0.206 ms
```
*Ping does not automatically stop so you have to press Ctrl+C to stop it.*

Good, we know the VPN is working as it should. If you don't get and answers go back to [[../HTB VPN Connection & Starting a Box]] or ask for help. HackTheBox also has a guide here: https://help.hackthebox.com/en/articles/5185687-introduction-to-lab-access.

Now, let's run a basic nmap scan:
`nmap 10.10.10.245`

```sh
┌──(kali㉿proxli)-[~/vpn]
└─$ nmap 10.10.10.245 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-29 01:35 CEST
Nmap scan report for 10.10.10.245
Host is up (0.023s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 0.63 seconds
```

This scan will scan the 1000 most common ports (not the 1000 first ones). We can see that of these 3 are open. Common services like ftp (an older type of file sharing), ssh (a safe modern way of connecting to the machines terminal) and http (an unencrypted web server).

Let's not run a more advanced scan
`nmap -p- -sC -sV -Pn 10.10.10.245`
-p-  Scans all ports. You can also scan one port with -p80 or a range with -p20-23
-sC  Runs the most common scripts, for example grabbing more web server information
-sV  Tries to figure out the versions of the running services
-Pn  Stops nmap from running a ping first. In this case we don't need it but it's a good habit so we get a nmap result even if the machine has ping turned off

```sh
┌──(kali㉿proxli)-[~/vpn]
└─$ nmap -p- -sC -sV -Pn 10.10.10.245
Starting Nmap 7.95 ( https://nmap.org ) at 2025-04-29 01:47 CEST
Nmap scan report for 10.10.10.245
Host is up (0.024s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 fa:80:a9:b2:ca:3b:88:69:a4:28:9e:39:0d:27:d5:75 (RSA)
|   256 96:d8:f8:e3:e8:f7:71:36:c5:49:d5:9d:b6:a4:c9:0c (ECDSA)
|_  256 3f:d0:ff:91:eb:3b:f6:e1:9f:2e:8d:de:b3:de:b2:18 (ED25519)
80/tcp open  http    Gunicorn
|_http-server-header: gunicorn
|_http-title: Security Dashboard
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.22 seconds
```

As you can see, the second scan takes much longer. Sometimes when ports respond in odd ways it can take minutes. But we can also see that we got much more information about the machine we are exploring.

Both these scans scan only for TCP ports. There are as many UDP ports as TCP ports but it takes much longer to scan UDP and the results are not as certain. This is because the base of the TCP protocol is to confirm packets received while TCP does not.

This means we have the answer for our first question!

Before you even read the next question, ask yourself what ways you can see to get even more information about this machine.

### Exploring the web page

> After running a "Security Snapshot", the browser is redirected to a path of the format `/[something]/[id]`, where `[id]` represents the id number of the scan. What is the `[something]`?

What are they talking about? Ah, parts on an URL. Let's open up a browser and browse to the IP address. To make sure the browser doesn't decide to google out IP address we'll put http:// before it.

If we had not had this hint, we could still have arrived at the same conclusion, right? We need to look at the web page.

`http://10.10.10.245`

We arrive at the web page and we seem to be logged in as Nathan. Hmm...
![[Images/Pasted image 20250429021154.png]]

The web site seem to show security information. Oh, on the second page we can download a pcap file (a network packet capture file). This is interesting, but this one contains "0 packets".
![[Images/Pasted image 20250429021924.png]]

The third page contains ip config information from this computer.
![[Images/Pasted image 20250429022303.png]]

Oh, interesting. Here we can for example see from the inside that the machine is listening to the ports we found and there's also a 53 (dns) mentioned. (We can disregard this one.)
![[Images/Pasted image 20250429141216.png]]

Now let's go back to the interesting pcap download page. Just as the question mentioned, we noticed an id in the URL. This is very interesting.

There is a common vulnerability called IDOR which means that while logged in as one user, you can change the id number in the browser URL and see other users data. We have to try this out!

### Burp Suite basics

We could do this in the browser, but why not take the opportunity to learn Burp!

Let's start burp
![[Images/Pasted image 20250429023941.png]]
Click `Next` and `Start Burp` without changing any options to start Burp.

First time Burp user?
If this is the first time you started burp and used it with your browser you can find a guide how to set it up here: https://   . In short, there are two things you need to do. Add the plugin FoxyProxy to your browser and proxy for burp and http for hostname 127.0.0.1 and port 8080 (Options, Proxy, Add). Then enable the burp proxy by selecting it in FoxyProxy and go to `http://burpsuite` in the browser. Click CA Certificate to download burps cert and go to your browsers settings. View Certificates and import the certificate. More details on the cert download here: https://portswigger.net/burp/documentation/desktop/external-browser-config/certificate/ca-cert-firefox

When you have Burp open, click the Proxy tab and make sure it says `Intercept off`. Go to the HTTP history. If your Burp is correctly connected to your browser all requests made by your browser should be passed through, proxied, through Burp and end up in this list.

Test this by going back to your browser, making sure that proxying through Burp is enabled in FoxyProxy (or another way) Press Ctrl+F5 to fully update the web page you are on, the PCAP download page.

Go back to Burp and look at the list. It should now be far from empty. Find the line where URL is `/data/10` and click it
![[Images/Pasted image 20250429025819.png]]

The lower part of the screen will now be split into two sections where you can see the Request sent from your browser and the Response from the web server. If you never saw these before, take the opportunity to study them.

Now right click the Request text and select `Send to Repeater`, then click the `Repeater` tab at the top of Burp.
![[Images/Pasted image 20250429030205.png]]

You can also send it to have burp perform an automated "attack" on the id number.

In Burps Repeater tab we can easily modify a request and sent it again, however many times we want. Right not we just want to modify the number at the very top that also was easily changed in the browser, but the next time we might want to change something else. To see what information is actually sent to the server is really great and Burp makes this so easy.

One thing to think about is that the last number of lines in the request should be the same number as they are or funny things might happen.

Click the `Send` button to send your request again. If we do this several times while changing the text it's useful to use the shortcut `Crtl`+`Space` to send a request.
![[Images/Pasted image 20250429033941.png]]

When you sent the request several tabs appeared on the Response side. You can see the response in Pretty, Raw, Hex and Rendered format. Check out render and after a bit of a wait you'll see something similar to the browser.

Now, let's edit the request. We need to try different id numbers. Try maybe 11, 12, 13? Did you find anything interesting? Remember to use `Crtl`+`Space` to send between each edit of the number. Maybe lower numbers?

Now switch back to `Pretty` and Scroll down to `Number of IP Packets` copy the text to the search field. Click the Cogwheel and check Auto-scroll to match when text changes. Do a few more tests of id numbers. How many pcap files with more than zero packets did you find?

Also scroll further down in the response and explore if you want. Big parts of this is off course what you would have seen if you right clicked the page in the browser and selected View Source.

Now when we have some interesting files to download we could go back to the browser and just enter the number there. You can also right click the Response and select `Show response in browser`.

![[Images/Pasted image 20250429035354.png]]

![[Images/Pasted image 20250429035445.png]]

This is the easiest as we will be downloading a file here, not just read data in the source code. Bur we can also search for download (the text on the button).
![[Images/Pasted image 20250429035646.png]]
As you can see, this search is not case sensitive.
We could replace the /data/0 after GET in the Request with /download/0. Actually, let's do that!

As the pcap is a mix of text and binary data this will look a bit funny.
![[Images/Pasted image 20250429040203.png]]
We could possibly find the information we need in here. It would be similar to cat:ing a pcap in the terminal, where you could for example filter the information with grep. Wireshark is a much nicer tool graphical to read pcap data in though.

Now, let's open the url in the browser and download the pcap. id 0 seem to have the most packets.

![[Images/Pasted image 20250429141738.png]]

Download the pcap and open it. (You should have Wireshark installed)

![[Images/Pasted image 20250429142529.png]]

### Time for Wireshark

Check through the packages and see if you can find any interesting and useful information. One thing to look for is credentials.

![[Images/Pasted image 20250429142855.png]]

In packets 36 and 40 we found a FTP login. As FTP is not encrypted it is all in clear text. We can use credentials to log in to the ftp. We saw that the machine is running a ftp server in our nmap results.

user: nathan
password: Buck3tH4TF0RM3!

### What can we find on FTP?

First let's make a directory for files we might find
![[Images/Pasted image 20250429143728.png]]

And we connect

`ftp 10.10.10.245`

![[Images/Pasted image 20250429143904.png]]

What files can we see? Let's download them all.

`dir`  to list files
`mget *` to download all files in the directory

![[Images/Pasted image 20250429144828.png]]

Type `exit` to disconnect.

![[Images/Pasted image 20250429145151.png]]

Oh, we got the user without actually connecting to the machines terminal.

...

### Password reuse?

Also always check for password re-use, in other words. Will the same password and username work for other services...

Might the one we have also work for ssh?

![[Images/Pasted image 20250429150507.png]]
![[Images/Pasted image 20250429150626.png]]

Yay, we're in!

Here we can see all the users files.

### Escalation privileges

Now we just have to find a way to get root credentials and read the root flag.

(I will add more about finding different vulnerabilities here later. What I usually look for and since linpeas is on the box we will go through that too. But now I have a limited time so we will use the hint given in the Guided Mode.)

> What is the full path to the binary on this machine has special capabilities that can be abused to obtain root privileges?

Capabilities is a newer kind of permissions on files. They make it possible for a program to have some extra permissions instead of having to be run, for example, with root.

To find capabilities on the machine, we run
`getcap -r / 2>/dev/null`

![[Images/Pasted image 20250429151401.png]]

Look at python! It has just the permissions we need.

(I will add more explanations later)

![[Images/Pasted image 20250429152057.png]]

The root flag is usually in the `/root` driectory

![[Images/Pasted image 20250429152320.png]]

There we have the root flag, and you should also have the information to be able to answer all the questions!

Please ask me if you have any questions!! <3

(I will add more explanations and information later - Sorry for the limited version today!)
