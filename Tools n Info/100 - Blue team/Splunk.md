
three main components

Forwarder
- agent/client
- low resource need

Indexer
- processing the data
- normalizes data into field-value pairs
- determines the datatype
- stores as events
- responds to searches..

Search Head
- in Search & Reporting App
- uses Splunk Search Processing Language
- request is sent to the indexer
- makes tables and charts


![[Images/Pasted image 20250702205225.png]]

`Add data`, to `Upload` log file, for example
1. Select Source
2. Select Source Type
3. Input Settings ->Select the index where these logs will be dumped and hostName to be associated with the logs
4. Review
5. Done

Example data:
![[Images/Pasted image 20250702203735.png]]
Case sensitive search
`source="VPN-logs-1663593355154.json" host="vpn-data" index="vpn-logs" sourcetype="_json" UserName="Maleena"`

![[Images/Pasted image 20250702205104.png]]

##### EPOCH time

use eval to make human readable

### Metadata

`| metadata type=sourcetypes index=botsv2 | eval firstTime=strftime(firstTime,"%Y-%m-%d %H:%M:%S") | eval lastTime=strftime(lastTime,"%Y-%m-%d %H:%M:%S") | eval recentTime=strftime(recentTime,"%Y-%m-%d %H:%M:%S") | sort - totalCount`

`metadata type=sourcetypes index=main`
`metadata type=hosts index=os`

![[Images/Pasted image 20250702211534.png]]
![[Images/Pasted image 20250702212115.png]]

![[Images/Pasted image 20250702211757.png]]
![[Images/Pasted image 20250702211958.png]]

![[Images/Pasted image 20250702211903.png]]
![[Images/Pasted image 20250702211932.png]]

### Example searches

`index="botsv2" "tor" "amber" "install"  | sort -_time desc`

`index="botsv2" 10.0.2.101 sourcetype=stream:http site="*.com" |stats count by site`
`index="botsv2" 10.0.2.101 sourcetype=stream:http site="*.com" | dedup site | table site`

`index="botsv2" source="stream:dns" "www.brewertalk.com"  | table host_addr{}  | dedup host_addr{}`

