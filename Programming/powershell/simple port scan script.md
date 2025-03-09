
```powershell
Test-NetConnection localhost -InformationLevel Detailed -Port 140
```

```powershell
$machine_to_scan = "localhost"

$scan_from_port = 1
$scan_to_port = 140

$open_ports = 0
for($port_no = $scan_from_port; $port_no -le $scan_to_port; $port_no++) {
  $result = Test-NetConnection $machine_to_scan -Port $port_no -InformationLevel Quiet
  if($result){$open_ports+=1}
}
Write-Host The number of open ports in the range $scan_from_port to $scan_to_port was $open_ports on $machine_to_scan.
```

