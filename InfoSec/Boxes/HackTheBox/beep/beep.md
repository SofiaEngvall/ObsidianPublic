
htb Beep 2023-07-30

![](file:///C:/Users/sofia/Downloads/boxes/images/image16.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image17.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image22.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image13.png)

Getting urllib has no attribute urlopen,  googling,  finding  this & trying  but it can’t  find request either, googling  again

![](file:///C:/Users/sofia/Downloads/boxes/images/image33.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image14.png)

and finding this:

![](file:///C:/Users/sofia/Downloads/boxes/images/image25.png)

works

![](file:///C:/Users/sofia/Downloads/boxes/images/image4.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image5.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image7.png)

both chmod & nmap …

![](file:///C:/Users/sofia/Downloads/boxes/images/image10.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image32.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image26.png)

![](file:///C:/Users/sofia/Downloads/boxes/images/image20.png)

My Review:

Too bad google shows too much

While my nmap ran I tried http://ip and a name was mentioned. I googled this name and exploit. Almost all hits were writeups for the box. I choose one that was not, the first one and tried running the python script to get a reverse shell. The script failed in several ways. I had to edit it quite a bit and finally found this: https://stackoverflow.com/questions/2792650/import-error-no-module-name-urllib2 regarding importing urllib and got the script working. Then it took a very short time to try sudo -l since I don't know much more lol. So this was good for a infosec noob like me with programming exp. But without the python problems it would not have taken me many  minutes and that's odd since this is only my second box.

Mostly too bad with the mega hint when googling. Hard not to read a bit of the solution when scanning the google results! I guess I should exclude writeups from the search results?

