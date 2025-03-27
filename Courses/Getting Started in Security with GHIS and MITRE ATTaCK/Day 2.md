
![[Images/Pasted image 20240612132641.png]]

MITRE matrix
Look at all the cathegories and techniques
we might not be able to stop all techniques but maybe 5 of 11 in one category

Lab [[Labs/3 - Password Spray|3 - Password Spray]]

Egress Traffic Analysis

The main difference between data egress and ingress is the direction of data flow: **ingress refers to data entering a system or network, while egress refers to data leaving a system or network**.

Check outgoing traffic too, not just incoming

![[Images/Pasted image 20240612134925.png|700]]

![[Images/Pasted image 20240612135011.png|600]]

We need more context, not just one alert

Simple machines and services starting to communicate with the internet?

##### Tools

![[Images/Pasted image 20240612135405.png|600]]

basic check on network traffic, not all the details
there are version `*`flow

![[Images/Pasted image 20240612135515.png|600]]

encrypted doesn't mean we can't get something from the traffic

![[Images/Pasted image 20240612135627.png|600]]

Find current unauthed stuff

RITA, free
![[Images/Pasted image 20240612135830.png|600]]
find patterns
find beaconing, consistent intermittent traffic

Check patterns in:
- interval
- con size
- data size
what's consistent, maybe one of them

Long connections
![[Images/Pasted image 20240612140901.png|600]]

Beacons
![[Images/Pasted image 20240612141107.png|700]]
1 first in confidence 100%
Does not have to be bad, there are normal ones

![[Images/Pasted image 20240612141308.png]]

![[Images/Pasted image 20240612141411.png]]

![[Images/Pasted image 20240612143254.png|600]]

Commersial solutions
![[Images/Pasted image 20240612143430.png|400]]

User agent strings
![[Images/Pasted image 20240612143704.png]]

![[Images/Pasted image 20240612143846.png|700]]

![[Images/Pasted image 20240612143931.png|700]]

Free & works with rita
![[Images/Pasted image 20240612144033.png]]

AC Hunter

Lab: [[Labs/4 - RITA and AC Hunter|4 - RITA and AC Hunter]]


### User Entity Behavior Analytics

collecting data on what the users are doing, normal stuff?

how to get value from?

most entries into the system occur one account

Logs are not that useful
![[Images/Pasted image 20240612151133.png|500]]

What should we log?

![[Images/Pasted image 20240612153024.png]]

User Entity Behavior Analytics
![[Images/Pasted image 20240612153140.png|600]]

user on the wrong os, the wrong location?

![[Images/Pasted image 20240612153755.png]]

![[Images/Pasted image 20240612153820.png|600]]

bad rules exists of course
false positive = was normal use
don't turn of the alerts -> fine tune

![[Images/Pasted image 20240612153958.png|600]]

![[Images/Pasted image 20240612154040.png|600]]

![[Images/Pasted image 20240612154312.png|400]]

![[Images/Pasted image 20240612154344.png|400]]

"egress and auth"

![[Images/Pasted image 20240612154444.png]]

Administrator should not be used a lot! :D

![[Images/Pasted image 20240612154557.png]]

![[Images/Pasted image 20240612154627.png]]
powershell script https://github.com/sans-blue-team/DeepBlueCLI

dig more with powershell
![[Images/Pasted image 20240612160602.png]]

Lab: [[Labs/5 - DeepBlueCLI|5 - DeepBlueCLI]]

![[Images/Pasted image 20240612161738.png|800]]

![[Images/Pasted image 20240612161935.png]]
^ good ones

Make sure you collect this

![[Images/Pasted image 20240612162133.png|400]]

![[Images/Pasted image 20240612162210.png]]
Command line not logged by default - Enable this!!

![[Images/Pasted image 20240612162248.png]]

![[Images/Pasted image 20240612162341.png]]

![[Images/Pasted image 20240612162356.png]]

![[Images/Pasted image 20240612162416.png]]

![[Images/Pasted image 20240612162547.png]]


SysMon

![[Images/Pasted image 20240612162713.png]]

Logs in event viewer, search in event viewer

![[Images/Pasted image 20240612163252.png]]
![[Images/Pasted image 20240612163307.png]]

![[Images/Pasted image 20240612163348.png]]
fw endpoint logs to central location

![[Images/Pasted image 20240612163414.png]]
most things are not very mysterious - but way to check stuff out

![[Images/Pasted image 20240612163604.png]]
Used in Hayabusa

![[Images/Pasted image 20240612163932.png]]

You NEED email logging

![[Images/Pasted image 20240612164004.png]]
^ log these and more
tune the rules






