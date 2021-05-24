<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="Survey.js"></script>
    <script src="Question.js"></script>
    <title>Take Your Survey</title>
    <link href="site.css" rel="stylesheet" type="text/css" />
</head>

<body>
    <!--Header-->
    <header>
        <img src="takesurveyheader.png" alt="header" />
    </header>
    <div id="main">
        <h1 style="width: 40%; margin: auto;">Take Your Survey</h1>
        <form action="submitanswers.php" method="get" target="_self">
            <input id="length" type="hidden" name="length" />
            <input id="key" type="hidden" name="key" />
            <script>
                var txt = '<?php
                    require_once('config.php');
                    $key = $_GET["key"];
                    $conn = connDB("localhost", "root", "", "surveyengine");
                    $sql = "SELECT `survey_jsontext` FROM `entity_surveys` WHERE `survey_key`='$key';";
                    if($result = $conn->query($sql)) {//If query succeeds
                        if($result->num_rows > 0) {//If the survey was found
                            $row = $result->fetch_assoc();
                            echo $row["survey_jsontext"];
                        } else {//Else no survey was found
                            echo "";
                        }
                    } else {//Else query fails
                        echo "";
                    }
                    ?>';
                var survey = new Survey(JSON.parse(txt));
                document.write(survey.toHTML());
                document.getElementById("length").value = survey.qArray.length;
                document.getElementById("key").value = '<?php if(isSet($_GET["key"])){echo $_GET["key"];} else {echo "";}?>';
            </script>
            <input type="submit" value="Submit Survey" />
        </form>
    </div>
</body>
</html>
