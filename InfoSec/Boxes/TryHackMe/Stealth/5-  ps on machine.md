```powershell
CF C:\Users\evader\Documents> cd Task
CF C:\Users\evader\Documents\Task> ls


    Directory: C:\Users\evader\Documents\Task


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----         9/4/2023   2:13 PM           3114 file.ps1                                                              
-a----        8/29/2023   3:06 PM             71 log.txt                                                               


CF C:\Users\evader\Documents\Task> cat  log.txt
File log.txt has been modified.
File vulnerable.ps1 has been modified.
CF C:\Users\evader\Documents\Task> rm log.txt
CF C:\Users\evader\Documents\Task> cat file.ps1
$FolderPath = "C:\xampp\htdocs\uploads\"

$FileDictionary = @{}

# Populate the initial state of the dictionary with file names and timestamps
$Files = Get-ChildItem -Path $FolderPath
foreach ($file in $Files) {
    $FileDictionary[$file.Name] = $file.LastWriteTime
}

# Watch for changes in the directory
while ($true) {
    Start-Sleep -Seconds 1
    
    # Check for changes in the directory
    $Files = Get-ChildItem -Path $FolderPath
    foreach ($file in $Files) {
        if ($FileDictionary.ContainsKey($file.Name)) {
            # Compare the current timestamp with the stored timestamp
            if ($file.LastWriteTime -ne $FileDictionary[$file.Name]) {
                Write-Host "File $($file.Name) has been modified."
                # Update the dictionary with the new timestamp
                $FileDictionary[$file.Name] = $file.LastWriteTime

                                         # Check if the file is executable, a PowerShell script, or a pdf document
            $extension = $file.Extension.ToLower()
            if ($extension -eq ".ps1") {
                                $scriptPath = "C:\xampp\htdocs\uploads\$($file.Name)"
                                        try{
                                #Invoke-Expression -Command "powershell.exe -ExecutionPolicy Bypass -File $scriptPath"

                                Start-Job -ScriptBlock { param($scriptPath) powershell.exe -ExecutionPolicy Bypass -File $scriptPath } -ArgumentList $scriptPath

                                }

                        catch {
    Write-Host "An exception occurred: $_.Exception.Message"
}



                #Write-Host "Opening file: $($file.Name)"
                #Start-Process -FilePath $file.FullName
            }
            }
        } else {
            # New file detected
            Write-Host "File $($file.Name) has been added."
            
            # Add the new file to the dictionary
            $FileDictionary[$file.Name] = $file.LastWriteTime
            
            # Check if the file is executable, a PowerShell script, or a pdf document
            $extension = $file.Extension.ToLower()
            if ($extension -eq ".ps1") {
                                $scriptPath = "C:\xampp\htdocs\uploads\$($file.Name)"

                                try{
                                #Invoke-Expression -Command "powershell.exe -ExecutionPolicy Bypass -File $scriptPath"
                                Start-Job -ScriptBlock { param($scriptPath) powershell.exe -ExecutionPolicy Bypass -File $scriptPath } -ArgumentList $scriptPath
                                }

                        catch {
    Write-Host "An exception occurred: $_.Exception.Message"
}






                           #Write-Host "Opening file: $($file.Name)"
                #Start-Process -FilePath $file.FullName
            }
        }
    }
    
    # Check for deleted files
    $deletedFiles = @()
    foreach ($fileName in $FileDictionary.Keys) {
        if (-not (Test-Path -Path (Join-Path $FolderPath $fileName))) {
            Write-Host "File $fileName has been deleted."
            # Add the deleted file to the array for removal
            $deletedFiles += $fileName
        }
    }

    # Remove the deleted files from the dictionary
    foreach ($deletedFile in $deletedFiles) {
        $FileDictionary.Remove($deletedFile)
    }
}
CF C:\Users\evader\Documents\Task> ls    


    Directory: C:\Users\evader\Documents\Task


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----         9/4/2023   2:13 PM           3114 file.ps1                                                              


CF C:\Users\evader\Documents\Task> cd..
CF C:\Users\evader\Documents> ls


    Directory: C:\Users\evader\Documents


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-----        12/8/2023  11:38 PM                Task                                                                  


CF C:\Users\evader\Documents> cd..
CF C:\Users\evader> ls


    Directory: C:\Users\evader


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-r---        7/25/2023   2:50 PM                3D Objects                                                            
d-r---        7/25/2023   2:50 PM                Contacts                                                              
d-r---        8/29/2023  10:33 AM                Desktop                                                               
d-r---        8/29/2023  10:33 AM                Documents                                                             
d-r---         9/4/2023   3:12 PM                Downloads                                                             
d-r---        7/25/2023   2:50 PM                Favorites                                                             
d-r---        7/25/2023   2:50 PM                Links                                                                 
d-r---        7/25/2023   2:50 PM                Music                                                                 
d-r---        7/25/2023   2:50 PM                Pictures                                                              
d-r---        7/25/2023   2:50 PM                Saved Games                                                           
d-r---        7/25/2023   2:50 PM                Searches                                                              
d-r---        7/25/2023   2:50 PM                Videos                                                                


CF C:\Users\evader> cd  desktop
CF C:\Users\evader\desktop> ls


    Directory: C:\Users\evader\desktop


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website                                                  
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website                                   
-a----         8/3/2023   7:12 PM            194 encodedflag                                                           


CF C:\Users\evader\desktop> cat "EC2 Feedback.website"   
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
Prop4=31,Amazon Web Services Survey
[InternetShortcut]
IDList=
URL=https://aws.qualtrics.com/SE/?SID=SV_e5MoFJhV18gTAyw
IconFile=https://aws.qualtrics.com/WRQualtricsShared/Brands/amazonmr/favicon.ico
IconIndex=1
[{A7AF692E-098D-4C08-A225-D433CA835ED0}]
Prop5=3,0
Prop9=19,0
Prop2=65,2C0000000000000001000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEB010000420000006F0500009A0200005B
[{9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3}]
Prop5=8,Microsoft.Website.41922747.DA8E48B2
CF C:\Users\evader\desktop> cat "EC2 Microsoft Windows Guide.website"
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,2
Prop4=31,What Is Amazon EC2? - Amazon Elastic Compute Cloud
[InternetShortcut]
IDList=
URL=http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/IntroWindowsUserGuide.html
IconFile=http://d36cz9buwru1tt.cloudfront.net/favicon.ico
IconIndex=1
[{A7AF692E-098D-4C08-A225-D433CA835ED0}]
Prop5=3,0
Prop9=19,0
Prop2=65,2C0000000000000001000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFA20000004A00000026040000A3020000D8
[{9F4C2855-9F79-4B39-A8D0-E1D42DE1D5F3}]
Prop5=8,Microsoft.Website.DC9AD30B.5334099
CF C:\Users\evader\desktop> cat encodedflag
-----BEGIN CERTIFICATE-----
WW91IGNhbiBnZXQgdGhlIGZsYWcgYnkgdmlzaXRpbmcgdGhlIGxpbmsgaHR0cDov
LzxJUF9PRl9USElTX1BDPjo4MDAwL2FzZGFzZGFkYXNkamFramRuc2Rmc2Rmcy5w
aHA=
-----END CERTIFICATE-----
CF C:\Users\evader\desktop> 
```

WW91IGNhbiBnZXQgdGhlIGZsYWcgYnkgdmlzaXRpbmcgdGhlIGxpbmsgaHR0cDovLzxJUF9PRl9USElTX1BDPjo4MDAwL2FzZGFzZGFkYXNkamFramRuc2Rmc2Rmcy5waHA=