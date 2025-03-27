
```powershell
$last_search_was_a_hit = $true
Get-Childitem -Path c:\ -Recurse -Exclude "*.exe","*.dll" | ForEach-Object {

	if ($last_search_was_a_hit) {Write-Host ""}
	else {Write-Host "`r" -NoNewline}

    if (($($_.FullName).length) -le ($Host.UI.RawUI.WindowSize.Width-1)) {
		Write-Host $($_.FullName) -NoNewline
    }
    else {
		Write-Host $($_.FullName).Substring(0,($Host.UI.RawUI.WindowSize.Width-1)) -NoNewline
    }

	$matches = $_ | Select-String -Pattern "API_KEY"
	if ($matches) {
        foreach ($match in $matches) {
            [PSCustomObject]@{
                Path       = $match.Path
                LineNumber = $match.LineNumber
                SearchWord = "API_KEY"
            }
            $match.Line
            ""
        }
	    Start-Sleep -Seconds 1
		$last_search_was_a_hit = $true
    }
    else {
	    $last_search_was_a_hit = $false
    }

	if ($last_search_was_a_hit) {Write-Host ""}
    Write-Host ("`r" + (" " * ($Host.UI.RawUI.WindowSize.Width-1))) -NoNewline
}
```
