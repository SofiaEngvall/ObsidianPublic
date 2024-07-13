<!DOCTYPE html>
<html>

<body>

    <h1>My very important header</h1>

    <?php

    function xor_encrypt($text) {
        $key = '<censored>';
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }

    function xor_encrypt_correct_key($text) {
        $key = 'eDWo';
        $outText = '';

        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }

    function loadData() {
        $mydata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
        global $_COOKIE;
        if(array_key_exists("data", $_COOKIE)) { //if the cookie data exists
            // "decrypt" the cookie
	        $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
            
	        if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
    	        if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
		            $mydata['showpassword'] = $tempdata['showpassword'];
		            $mydata['bgcolor'] = $tempdata['bgcolor'];
	            }
	        }
        }
        return $mydata;
    }

    function saveData($d) { //the "encryption" of the cookie
        setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
    }

    //$data = loadData();

    // just does bgcolor - but this is the only input
    //if(array_key_exists("bgcolor",$_REQUEST)) {
    //    if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
    //        $data['bgcolor'] = $_REQUEST['bgcolor'];
    //    }
    //}

    //saveData($data);

    //if($data["showpassword"] == "yes") {
    //    print "The password for natas12 is <censored><br>";
    //}
    
    echo "no<br>--<br>";

    //echo array("showpassword" => "no", "bgcolor" => "#ffffff")."<br>";
    //this only prints a notice about us trying to print an array, it does NOT print anything

    print_r(array("showpassword" => "no", "bgcolor" => "#ffffff"));
    //Array ( [showpassword] => no [bgcolor] => #ffffff )  - print_r prints more info, smarter, can handle array

    echo "<br>".json_encode( array("showpassword" => "no", "bgcolor" => "#ffffff"))."<br>";
    //{"showpassword":"no","bgcolor":"#ffffff"} <- the array converted to json format - this is an actual string and what is used for "encryption"

    echo xor_encrypt(json_encode( array("showpassword" => "no", "bgcolor" => "#ffffff")))."<br>";
    //GAMK QUPA  AF A - The result after xor with the key "censored"

    echo base64_encode(xor_encrypt(json_encode( array("showpassword" => "no", "bgcolor" => "#ffffff"))));
    //R0EWBhwYAgQXTUsMFwpRVVALCxwQQQcJEAAeChYcBkFGCBUJFAMCHEE= - just base 64 of the same



    //------------------------------
    echo "<br><br>";

    echo "yes<br>---<br>";

    //echo array("showpassword" => "yes", "bgcolor" => "#ffffff")."<br>";
    //this only prints a notice about us trying to print an array, it does NOT print anything

    print_r(array("showpassword" => "yes", "bgcolor" => "#ffffff"));
    //Array ( [showpassword] => yes [bgcolor] => #ffffff )  - print_r prints more info, smarter, can handle array

    echo "<br>".json_encode( array("showpassword" => "yes", "bgcolor" => "#ffffff"))."<br>";
    //{"showpassword":"yes","bgcolor":"#ffffff"} <- the array converted to json format - this is an actual string and what is used for "encryption"

    echo xor_encrypt(json_encode( array("showpassword" => "yes", "bgcolor" => "#ffffff")))."<br>";
    //GAMK QUPMOG LYGM X - The result after xor with the key "censored"

    echo base64_encode(xor_encrypt(json_encode( array("showpassword" => "yes", "bgcolor" => "#ffffff"))));
    //R0EWBhwYAgQXTUsMFwpRVVAcAU0eT0cMFAwdCQtMHllHTRUJFAMCWB4e - just base 64 of the same

    //------------------------------
    echo "<br><br>";

    echo "cookie<br>------<br>";

    $cookie = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=";
    echo $cookie."<br>";
    //HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg=

    $cookie = base64_decode($cookie);
    echo "cookie base64 decoded: ".$cookie."<br>";
    //cookie base64 decoded: f$ 3'7  uUG*8MIf5+;fmMF"1 "1M

    //base64_encode(xor_encrypt(json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"))));
    $temp = json_encode(array("showpassword" => "no", "bgcolor" => "#ffffff"));
    echo "default array json encoded: ".$temp."<br>";
    //default array json encoded: {"showpassword":"no","bgcolor":"#ffffff"}

    $text = $cookie;
    $key = $temp;
    $outText = '';

    //Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    print_r($outText);
    //eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe

    echo "<br><br>".base64_encode(xor_encrypt_correct_key(json_encode(array("showpassword" => "yes", "bgcolor" => "#ffffff"))));
    //HmYkBwozJw4WNyAAFyB1VUc9MhxHaHUNAic4Awo2dVVHZzEJAyIxCUc5

    echo "<br>"."<br>";

    ?>

</body>

</html>
