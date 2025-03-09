
directory listing

https://devblogs.microsoft.com/scripting/use-windows-powershell-to-search-for-files/

`Get-Childitem –Path C:\ -Include *interesting-file.txt* -File -Recurse -ErrorAction SilentlyContinue`

Help
```powershell
PS C:\Program Files (x86)\Internet Explorer> get-help get-childitem

NAME
    Get-ChildItem

SYNOPSIS
    Gets the files and folders in a file system drive.


SYNTAX
    Get-ChildItem [[-Filter] <String>] [-Attributes {ReadOnly | Hidden | System | Directory | Archive | Device | Normal | Temporary | SparseFile | ReparsePoint |
    Compressed | Offline | NotContentIndexed | Encrypted | IntegrityStream | NoScrubData}] [-Depth <UInt32>] [-Directory] [-Exclude <String[]>] [-File] [-Force]
    [-Hidden] [-Include <String[]>] -LiteralPath <String[]> [-Name] [-ReadOnly] [-Recurse] [-System] [-UseTransaction] [<CommonParameters>]

    Get-ChildItem [[-Path] <String[]>] [[-Filter] <String>] [-Attributes {ReadOnly | Hidden | System | Directory | Archive | Device | Normal | Temporary | SparseFile |
    ReparsePoint | Compressed | Offline | NotContentIndexed | Encrypted | IntegrityStream | NoScrubData}] [-Depth <UInt32>] [-Directory] [-Exclude <String[]>] [-File]
    [-Force] [-Hidden] [-Include <String[]>] [-Name] [-ReadOnly] [-Recurse] [-System] [-UseTransaction] [<CommonParameters>]

    Get-ChildItem [-Attributes <FileAttributes]>] [-Directory] [-File] [-Force] [-Hidden] [-ReadOnly] [-System] [-UseTransaction] [<CommonParameters>]


DESCRIPTION
    The Get-ChildItem cmdlet gets the items in one or more specified locations. If the item is a container, it gets the items inside the container, known as child items.
    You can use the Recurse parameter to get items in all child containers.

    A location can be a file system location, such as a directory, or a location exposed by a different Windows PowerShell provider, such as a registry hive or a
    certificate store.
    In a file system drive, the Get-ChildItem cmdlet gets the directories, subdirectories, and files. In a file system directory, it gets subdirectories and files.

    By default, Get-ChildItem gets non-hidden items, but you can use the Directory, File, Hidden, ReadOnly, and System parameters to get only items with these
    attributes. To create a complex attribute search, use the Attributes parameter. If you use these parameters, Get-ChildItem gets only the items that meet all search
    conditions, as though the parameters were connected by an AND operator.

    Note: This custom cmdlet help file explains how the Get-ChildItem cmdlet works in a file system drive. For information about the Get-ChildItem cmdlet in all drives,
    type "Get-Help Get-ChildItem -Path $null" or see Get-ChildItem at http://go.microsoft.com/fwlink/?LinkID=113308.


RELATED LINKS
    Online version: http://technet.microsoft.com/library/hh847897(v=wps.630).aspx
    Get-ChildItem (generic); http://go.microsoft.com/fwlink/?LinkID=113308
    FileSystem Provider
    Clear-Content
    Get-Content
    Get-ChildItem
    Get-Content
    Get-Item
    Remove-Item
    Set-Content
    Test-Path

REMARKS
    To see the examples, type: "get-help Get-ChildItem -examples".
    For more information, type: "get-help Get-ChildItem -detailed".
    For technical information, type: "get-help Get-ChildItem -full".
    For online help, type: "get-help Get-ChildItem -online"

```