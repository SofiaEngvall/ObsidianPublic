

ps `get-item wmplayer.exe | Select-object *`

cmd `wmic datafile where name="C:\\Program Files\\Windows Media Player\\wmplayer.exe" get /value`
needs full path