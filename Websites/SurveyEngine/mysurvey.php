<!DOCTYPE html>
<?php
if(session_status() == PHP_SESSION_NONE) {
    session_start();
}
if(!isSet($_SESSION["username"])) {//If not logged in
    header("location:index.php");
}
?>
<html lang="">
<head>
    <meta charset="utf-8">
    <script src="Survey.js"></script>
    <script src="Question.js"></script>
    <link href="site.css" rel="stylesheet" type="text/css" />
    <title>Your Survey</title>
</head>

<body>
    <!--Header-->
    <header>
        <img src="viewerheader.png" alt="header" />
    </header>
    <div id="main">
    <?php
        require_once('config.php');
        $conn = connDB("localhost", "root", "", "surveyengine");
        $id = $_GET["id"];
        $sql = "SELECT `survey_jsontext` FROM `surveyengine`.`entity_surveys` WHERE `survey_id`=$id;";
        $result = $conn->query($sql);
        $row = $result->fetch_assoc();
        $txt = $row["survey_jsontext"];
        echo "<script>" .
                "var obj = JSON.parse('$txt');" .
                "var srvy = new Survey(obj);" . 
                "document.write(srvy.resultSet());" . 
             "</script>";
    ?>
    </div>
</body>
</html>
