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
        <meta charset="utf-8" />
        <link href="site.css" rel="stylesheet" type="text/css">
        <script src="Survey.js"></script>
        <script src="Question.js"></script>
        <title>Survey Engine</title>
    </head>
    <body>
        <!--Header-->
        <header>
            <img src="header.png" alt="header" />
        </header>
        <div id="main">
            <h1>Create Surveys</h1>
            <h2>Share With Others</h2>
            <h2>View Your Results</h2>
            <div class="opt"><a href="creator.php" class="optLink">Create a New Survey</a></div>
            <div class="opt"><a href="surveyviewer.php" class="optLink">View Your Created Surveys</a></div>
        </div>
    </body>
</html>