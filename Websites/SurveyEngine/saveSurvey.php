<?php
require_once('config.php');

//Start session
session_start();
if(!isSet($_SESSION["username"]) || $_SERVER["REQUEST_METHOD"] != "POST") {//If not logged in
    header("location:index.php");
}

//Declare variables
$server = 'localhost';//Server name
$username = 'root';//Server username
$password = '';//Server password
$db = 'surveyengine';//Database name
$sql;//SQL query to be executed
$result;//Result of SQL query
$sname = $_POST["surveyName"];//Name of survey
$userid = $_SESSION["id"];//ID of user
$jsontext = $_POST["jsonText"];//Survey in json text form
$key = array();//Unique sharing key of survey
$possible = array(0,1,2,3,4,5,6,7,8,9);

//Create connection to database
$conn = connDB($server, $username, $password, $db);

//Create unique key
for($i = 0; $i < 40; ++$i) {
    array_push($key, array_rand($possible, 1));
}
$key = implode($key);

//Check to see if survey record already exists in db
$sql = "SELECT `survey_name` FROM `surveyengine`.`entity_surveys` WHERE `survey_name`='$sname';";
$result = $conn->query($sql);

//Store survey in db
If($result->num_rows > 0) {//Update record

} else {//Create record
    $sql = "INSERT INTO `surveyengine`.`entity_surveys` (`survey_jsontext`, `survey_name`, `survey_user_id`, `survey_key`) VALUES ('$jsontext', '$sname', $userid, $key);";
    $conn->query($sql);
}

//Close connection and direct to home page
$conn->close();
header("location:home.php");
?>