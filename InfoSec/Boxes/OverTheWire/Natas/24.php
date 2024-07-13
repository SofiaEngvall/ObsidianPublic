
<?php

echo $_REQUEST["passwd"]."<br>";
echo $_REQUEST["truetest"]."<br>";
echo ["apples", "bananas"]."<br>";
print_r(["apples", "bananas"]);
echo "<br>".serialize(["apples", "bananas"])."<br>";

if(strcmp($_REQUEST["truetest"],"foo")){
    echo "true<br>";
}
else{
    echo "false<br>";
}

echo strcmp(false, 0)."<br>";

echo strcmp($_REQUEST["passwd"], "123");

if(!strcmp($_REQUEST["passwd"],"123")){
    echo "<br>The credentials for the next level are:<br>";
    echo "<pre>Username: natas25 Password: <censored></pre>";
}
else{
    echo "<br>Wrong!<br>";
}

?>  
