
/B takes all data - has to be run in admin cmd
don't forget /XJ or you might do as I did and fill up 4 TB from a 500GB hdd due to circular references lol

```sh
C:\WINDOWS\system32>robocopy F:\ D:\OldCDriveBackup /E /B /COPY:DT /R:1 /W:1 /XJ /XF hiberfil.sys pagefile.sys swapfile.sys /XD "$RECYCLE.BIN" "System Volume Information"
```

```sh
          New Dir          2    F:\WpSystem\S-1-5-21-723537995-1841945705-822197383-1001\AppData\Local\Packages\MICROSOFT.MINECRAFTUWP_8wekyb3d8bbwe_bak\treatments\treatment_packs2\
100%        New File                 233        treatment_metadata.json
100%        New File                2342        treatment_tags.json
          New Dir          2    F:\WpSystem\S-1-5-21-723537995-1841945705-822197383-1001\AppData\Local\Packages\MICROSOFT.MINECRAFTUWP_8wekyb3d8bbwe_bak\treatments\treatment_packs2\jWhq9D3rgbo=\
100%        New File                 238        contents.json
100%        New File                 271        manifest.json
          New Dir          1    F:\WpSystem\S-1-5-21-723537995-1841945705-822197383-1001\AppData\Local\Packages\MICROSOFT.MINECRAFTUWP_8wekyb3d8bbwe_bak\treatments\treatment_packs2\jWhq9D3rgbo=\ui\
100%        New File                4469        pdp_screen.json
          New Dir          0    F:\WUDownloadCache\
          New Dir          0    F:\XboxGames\

------------------------------------------------------------------------------

               Total    Copied   Skipped  Mismatch    FAILED    Extras
    Dirs :    511664    511601        63         0         0         0
   Files :   2009164   2009122        14         0        28         0
   Bytes : 335.512 g 335.502 g   10.06 m         0         0         0
   Times :   2:15:50   1:16:09                       0:00:28   0:59:12


   Speed :            78840009 Bytes/sec.
   Speed :            4511.261 MegaBytes/min.
   Ended : Friday, 2 October 2026 22:58:19
```