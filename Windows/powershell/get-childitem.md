
ls
gci

`get-childitem -path whereever`

`Get-ChildItem | Sort-Object Length`

`Get-ChildItem | Where-Object -Property "Extension" -eq ".txt"`

`Get-ChildItem | Select-Object Name,Length`

`Get-ChildItem | Where-Object -Property "Name" -like "ship*"`

`Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 1`

