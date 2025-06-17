
Start menu:
- `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`

Task Manager:
- Startup tab

Registry:
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

(Local) Group Police Editor
- Computer Configuration\Windows Settings\Scripts (Startup/Shutdown)
- User Configuration\Windows Settings\Scripts (Startup/Shutdown)

Task Scheduler
- This can also be a place to check
- For an easy check use powershell:
  `Get-ScheduledTask | Select TaskName, TaskPath, State | ConvertTo-Html -Title "Scheduled Tasks" | Out-File ($f = [IO.Path]::GetTempFileName() + ".html"); Start-Process $f`
  Just paste this in powershell to run it and a readable list will be opened in your browser.
- For more information:
  `Get-ScheduledTask | Where-Object {$_.State -ne 'Disabled'} | ForEach-Object { $info = Get-ScheduledTaskInfo $_; if ($info.LastRunTime -gt (Get-Date).AddYears(-1)) { [pscustomobject]@{LastRunTime=$info.LastRunTime;TaskName=$_.TaskName;TaskPath=$_.TaskPath;Action=($_.Actions | ForEach-Object {$_.Execute}) -join "; ";Description=$_.Description} } } | Sort-Object LastRunTime -Descending | ConvertTo-Html -Title "Scheduled Tasks" | Out-File ($f=[IO.Path]::GetTempFileName()+".html"); Start-Process $f`
- Updated with more info:
  `Get-ScheduledTask | Where-Object {$_.State -ne 'Disabled'} | ForEach-Object { $info=Get-ScheduledTaskInfo $_; if ($info.LastRunTime -gt (Get-Date).AddYears(-1)) { $action = if ($_.Actions -and ($_.Actions | Where-Object { ([string]$_.Execute).Trim() -ne '' -or ([string]$_.Arguments).Trim() -ne '' })) { ($_.Actions | ForEach-Object { (([string]$_.Execute) + ' ' + ([string]$_.Arguments)).Trim() }) -join '; ' } else { try { $xml = [xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath); ($xml.Task.Actions.ComHandler | ForEach-Object { $data = if ($_.Data -and $_.Data.InnerText.Trim() -ne '') { ', Data=' + $_.Data.InnerText.Trim() } else { '' }; 'ClassId=' + $_.ClassId + $data }) -join '; ' } catch { 'No action or could not retrieve details' } }; [pscustomobject]@{LastRunTime=$info.LastRunTime; Task=$_.TaskPath + $_.TaskName; Action=$action; Description=$_.Description} } } | Sort-Object LastRunTime -Descending | ConvertTo-Html -Title 'Scheduled Tasks' | Out-File ($f=[IO.Path]::GetTempFileName()+'.html'); Start-Process $f`
- Readable version:
```powershell
Get-ScheduledTask |
Where-Object { $_.State -ne 'Disabled' } |
ForEach-Object {
    $info = Get-ScheduledTaskInfo $_
    if ($info.LastRunTime -gt (Get-Date).AddYears(-1)) {
        $action = if (
            $_.Actions -and
            ($_.Actions | Where-Object {
                ([string]$_.Execute).Trim() -ne '' -or
                ([string]$_.Arguments).Trim() -ne ''
            })
        ) {
            ($_.Actions | ForEach-Object {
                (([string]$_.Execute) + ' ' + ([string]$_.Arguments)).Trim()
            }) -join '; '
        } else {
            try {
                $xml = [xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath)
                ($xml.Task.Actions.ComHandler | ForEach-Object {
                    $data = if ($_.Data -and $_.Data.InnerText.Trim() -ne '') {
                        ', Data=' + $_.Data.InnerText.Trim()
                    } else {
                        ''
                    }
                    'ClassId=' + $_.ClassId + $data
                }) -join '; '
            } catch {
                'No action or could not retrieve details'
            }
        }

        [pscustomobject]@{
            LastRunTime = $info.LastRunTime
            Task        = $_.TaskPath + $_.TaskName
            Action      = $action
            Description = $_.Description
        }
    }
} |
Sort-Object LastRunTime -Descending |
ConvertTo-Html -Title 'Scheduled Tasks' |
Out-File ($f = [IO.Path]::GetTempFileName() + '.html')
Start-Process $f
```

- To instead use csv format and open as a spreadsheet
```powershell
Export-Csv -Path ($f = [IO.Path]::GetTempFileName() + '.csv') -NoTypeInformation
Start-Process $f
```


```powershell
Get-ScheduledTask |
Where-Object {
    $_.State -ne 'Disabled'
} |
ForEach-Object {
    $info = Get-ScheduledTaskInfo $_

    if ($info.LastRunTime -gt (Get-Date).AddYears(-1)) {
        $action = if (
            $_.Actions -and
            ($_.Actions | Where-Object {
                ([string]$_.Execute).Trim() -ne '' -or
                ([string]$_.Arguments).Trim() -ne ''
            })
        ) {
            $_.Actions |
            ForEach-Object {
                (([string]$_.Execute) + ' ' + ([string]$_.Arguments)).Trim()
            } -join '; '
        }
        else {
            try {
                $xml = [xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath)

                $xml.Task.Actions.ComHandler |
                ForEach-Object {
                    $clsid = $_.ClassId
                    $name = (Get-ItemProperty -Path "Registry::HKEY_CLASSES_ROOT\CLSID\$clsid" -Name '(default)' -ErrorAction SilentlyContinue).'(default)'
                    if (-not $name) { $name = $clsid }
                    $arg = if (
                        $_.Data -and
                        $_.Data.InnerText.Trim() -ne ''
                    ) {
                        "($($_.Data.InnerText.Trim()))"
                    } else {
                        ''
                    }
                    "COM class: $name$arg"
                } -join '; '
            }
            catch {
                'No action or could not retrieve details'
            }
        }

        [pscustomobject]@{
            LastRunTime = $info.LastRunTime
            Task        = $_.TaskPath + $_.TaskName
            Action      = $action
            Description = $_.Description
        }
    }
} |
Sort-Object LastRunTime -Descending |
Export-Csv -Path ($f = [IO.Path]::GetTempFileName() + '.csv') -NoTypeInformation

Start-Process $f
```

```powershell
Get-ScheduledTask | Where-Object {$_.State -ne 'Disabled'} | ForEach-Object { $info=Get-ScheduledTaskInfo $_; if ($info.LastRunTime -gt (Get-Date).AddYears(-1)) { $action=if ($_.Actions -and ($_.Actions | Where-Object { ([string]$_.Execute).Trim() -ne '' -or ([string]$_.Arguments).Trim() -ne '' })) { ($_.Actions | ForEach-Object { (([string]$_.Execute) + ' ' + ([string]$_.Arguments)).Trim() }) -join '; ' } else { try { $xml=[xml](Export-ScheduledTask -TaskName $_.TaskName -TaskPath $_.TaskPath); ($xml.Task.Actions.ComHandler | ForEach-Object { $clsid=$_.ClassId; $name=(Get-ItemProperty -Path "Registry::HKEY_CLASSES_ROOT\CLSID\$clsid" -Name '(default)' -ErrorAction SilentlyContinue).'(default)'; if(-not $name){$name=$clsid}; $arg=if ($_.Data -and $_.Data.InnerText.Trim() -ne '') { "($($_.Data.InnerText.Trim()))" } else { '' }; "COM class: $name$arg" }) -join '; ' } catch { 'No action or could not retrieve details' } }; [pscustomobject]@{LastRunTime=$info.LastRunTime; Task=$_.TaskPath + $_.TaskName; Action=$action; Description=$_.Description} } } | Sort-Object LastRunTime -Descending | Export-Csv -Path ($f=[IO.Path]::GetTempFileName()+'.csv') -NoTypeInformation; Start-Process $f
```