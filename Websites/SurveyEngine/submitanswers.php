<!DOCTYPE html>
<?php
//Include files
require_once('config.php');
if(session_status() == PHP_SESSION_NONE) {
    session_start();
}
?>
<html lang="">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="Survey.js"></script>
    <script src="Question.js"></script>
    <title>Submit Answers</title>
</head>

<body>
    <?php
    if($_SERVER["REQUEST_METHOD"] == "POST") {
        $conn = connDB("localhost", "root", "", "surveyengine");
        $jsontext = (isSet($_POST["survey"])) ? $_POST["survey"] : "";
        $id = $_SESSION["survey_id"];
        unset($_SESSION["survey_id"]);
        $sql = "UPDATE `entity_surveys` SET `survey_jsontext`='$jsontext' WHERE `survey_id`=" . $id . ";";
        if($jsontext == "" || $id == "") {
            echo $jsontext . "<br/>ID: " . $id . "<br/>";
        }
        if($conn->query($sql)) {
            header("location:submitted.php");
        } else {
            die($conn->error);
        }
    }
    ?>
    <form id="updateForm" method="post" target="_self">
        <input type="hidden" id="survey" name = "survey" />
    </form>
    <script>
        //Get survey json text
        var txt = 
        '<?php
        //Declare and initialize variables
        $length = (isSet($_GET["length"])) ? $_GET["length"] : 0;
        $key = (isSet($_GET["key"])) ? $_GET["key"] : "";
        $conn = connDB("localhost", "root", "", "surveyengine");
        $sql = "SELECT `survey_jsontext`, `survey_id` FROM `entity_surveys` WHERE `survey_key`='$key';";

        //If there is no key end function
        if($key == "") {
            die("<h1>Thats not even a correct survey key</h1>");
        }
        //Run query
        if($result = $conn->query($sql)) {//If query successful
            if($result->num_rows > 0) {
                $row = $result->fetch_assoc();
                $_SESSION["survey_id"] = $row["survey_id"];
                echo $row["survey_jsontext"];
            } else {
                echo "";
            }
        } else {
            echo "";
        }
        ?>';
        document.write(txt);
        
        //If text is not empty, create survey out of it
        var survey = new Survey(JSON.parse(txt));
        
        //Get array of answers
        var url = decodeURIComponent(window.location.href);
        var info = url.split("?");
        var nvp = info[1].split("&");
        var ansArray = new Object;
        for(var i = 2; i < nvp.length; ++i) {
            var map = nvp[i].split("=");
            var name = map[0];
            var value = map[1];
            value = value.replace(/\+/g, " ");
            ansArray[name]=value;
        }
        
        //Increment answer if matches
        for(var i = 0; i < survey.qArray.length; ++i) {
            for(var j = 0; j < survey.qArray[i].ans.length;++j) {
                if(ansArray["ques" + i] == survey.qArray[i].ans[j]) {
                    survey.qArray[i].ansIncrement(j);
                } 
            }
        }
        //Set survey json in form
        document.getElementById("survey").value = JSON.stringify(survey);
        document.getElementById("updateForm").submit();
    </script>
</body>
</html>
