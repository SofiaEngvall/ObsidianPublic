
part of the [[../../Windows/Sysinternal Tools|Sysinternal Tools]]

Logs from sysmon are found in `Applications and Services Logs/Microsoft/Windows/Sysmon/Operational`

provides detailed information about process creations, network connections, and changes to file creation time

config file required - how to analyze the events
https://github.com/SwiftOnSecurity/sysmon-config
https://github.com/ion-storm/sysmon-config/blob/develop/sysmonconfig-export.xml
##### Example rule

Event ID 8: CreateRemoteThread

monitor for processes injecting code into other processes.
could be used by malware to hide malicious activity

```xml
<RuleGroup name="" groupRelation="or">
  <CreateRemoteThread onmatch="include">
    <StartAddress name="Alert,Cobalt Strike" condition="end with">0B80</StartAddress>
    <SourceImage condition="contains">\</SourceImage>
  </CreateRemoteThread>
</RuleGroup>
```

- look at the memory address for a specific ending condition which could be an indicator of a Cobalt Strike beacon
- look for injected processes that do not have a parent process - anomaly

