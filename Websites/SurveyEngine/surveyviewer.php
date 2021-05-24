<!DOCTYPE html>
<?php
if(session_status() == PHP_SESSION_NONE) {
    session_start();
}
if(!isSet($_SESSION["username"])) {//If not logged in
    header("location:index.php");
}
?>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="site.css" type="text/css" />
    <title>View all of your Surveys</title>
    <script>
        function share(key) {
            window.alert(location.hostname + "/SurveyEngine/share.php?key=" + key);
        }
        function setId(id) {
            document.getElementById("deleteId").value = id;
            document.getElementById("deleteForm").submit();
        }
    </script>
</head>

<body>
    <!--Header-->
    <header>
        <img src="viewerheader.png" alt="header" />
    </header>
    <div id="main">
        <h1>My Surveys</h1>
        <a href="home.php" style="float: left; text-decoration: none; display: block; position: absolute; width: 10vw; height: 7vh; line-height: 7vh; background: linear-gradient(#cbf6ff, #00d5ff); color: black; margin-left: 2vw; border-radius: 10px;">Home</a>
        <?php
        require_once('config.php');
        $conn = connDB("localhost", "root", "", "surveyengine");
        $id = $_SESSION["id"];
        $sql = "SELECT `survey_id`, `survey_name`, `survey_key` FROM `surveyengine`.`entity_surveys` WHERE `survey_user_id`=$id;";
        $result = $conn->query($sql);
        if($result->num_rows > 0) {
            echo "<ul style='list-style-type:none;'>";
            while($rows = $result->fetch_assoc()) {
                $key = $rows["survey_key"];
                $name = $rows["survey_name"];
                $sId = $rows["survey_id"];
                $_POST["deleteId"] = $sId;
                echo "<li><a href='mysurvey.php?id=$sId' target='_blank'>$name</a><input type='button' value='Share Link' onclick='share(\"$key\");' /></li>";
            }
        } else {
            echo "<h3>You Haven't Made Any Surveys Yet</h3>";
        }
        ?>
    </div>
</body>
</html>
