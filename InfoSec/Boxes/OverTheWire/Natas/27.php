
<?php
$link = mysqli_connect('localhost', 'root', '');
mysqli_select_db($link, 'information_schema');

echo mysqli_real_escape_string($link, "te¿' =s#¤%ts\"\"tring")."<br>\n";

echo mysqli_real_escape_string($link, "¿' or 1=1 -- -")."<br>\n";

echo mysqli_real_escape_string($link, "dddd\",'|&$;:`({{@<%=ddd")."<br>\n";

echo htmlentities(mysqli_real_escape_string($link, "dddd\",'|&$;:`({{@<%=ddd"))."<br>\n";

echo mysqli_real_escape_string($link, "natas28\nanything") . "<br>\n";
echo mysqli_real_escape_string($link, "natas28/*anything") . "<br>\n";

mysqli_close($link);
?>
