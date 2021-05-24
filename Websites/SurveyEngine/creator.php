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
        <meta charset="UTF-8">
        <script src="Question.js"></script>
        <script src="Survey.js"></script>
        <link href="site.css" rel="stylesheet" type="text/css" />
        <title>Create a Survey</title>
    </head>
    <body>
        <!--Header-->
        <header>
            <img src="creatorheader.png" alt="header" />
        </header>
        <div id="main">
            <a href="home.php" style="float: left; text-decoration: none; display: block; position: absolute; width: 10vw; height: 7vh; line-height: 7vh; background: linear-gradient(#cbf6ff, #00d5ff); color: black; margin-left: 2vw; border-radius: 10px;">Home</a>
            <!--Button to create survey-->
            <input type="button" id="createSurvey" value="Create Survey" onclick="createSurvey();" /><br/>
            
            <!--Buttons to add question, edit name, edit description-->
            <input type="button" id="addQ" value="Edit Questions" onclick="resetAction()" disabled />
            <input type="button" id="editName" value="Edit Name" onclick="editNameAction()" disabled />
            <input type="button" id="editDesc" value="Edit description" onclick="editDescAction()" disabled />
            
            <!--Area where button result from above spawns-->
            <div id="actionArea">&nbsp;</div>
            
            <!--Output current survey-->
            <div id="surveyPreview">&nbsp;</div>
                
            <!--Button to save survey and leave page-->
            <form action="saveSurvey.php" method="post" onsubmit="setJsonText();">
                <input type="submit" value="Save Survey" id="saveSurvey" disabled/>
                <input type="hidden" name="jsonText" id="jsonText" />
                <input type="hidden" name="surveyName" id="surveyName" />
            </form>
        </div>
        
        <script>
            //Declare variables
            var survey;//Will contain survey
            var actionArea = document.getElementById("actionArea");
            
            //Function to create an empty survey object
            function createSurvey() {
                //Create empty survey
                survey = new Survey();
                
                //Disable creation button, enable other buttons
                document.getElementById("createSurvey").disabled = true;
                document.getElementById("addQ").disabled = false;
                document.getElementById("editName").disabled = false;
                document.getElementById("editDesc").disabled = false;
                document.getElementById("saveSurvey").disabled = false;
                
                //Show survey in preview area
                preview();
                
                //Setset action area to add question
                resetAction();
            }
            
            //Function to show survey in preview area
            function preview() {
                //Display survey in preview area
                document.getElementById("surveyPreview").innerHTML = survey.toHTML();
            }
            
            //Function to the edit name action
            function editNameAction() {
                //Declare variables
                var output = "";
                
                //Build output string
                output += "<label for='nameInput'>Name</label><br/>";
                output += "<input type='text' class='req' id='nameInput' /><span class='err'>&nbsp;</span><br/>";
                output += "<input type='button' value='Change Name' onclick='editName()' />";
                
                //Set output in action area
                actionArea.innerHTML = output;
            }
            
            //Function that edits name
            function editName() {
                //Get element that contains new name
                var txt = document.getElementById("nameInput");
                
                //Check if name is empty
                if(!isValid())
                    return;
                
                //Set the surveys name
                survey.setName(cleanTxt(txt.value));
                
                //Remove edit name action from action area
                resetAction();
                
                //Update survey preview
                preview();
            }
            
            //Function to the edit description action
            function editDescAction() {
                //Declare variables
                var output = "";
                
                //Build output string
                output += "<label for='descInput'>Description</label><br/>";
                output += "<input type='text' class='req' id='descInput' /><span class='err'>&nbsp;</span><br/>";
                output += "<input type='button' value='Change Description' onclick='editDesc()' />";
                
                //Set output in action area
                actionArea.innerHTML = output;
            }
            
            //Function that edits description
            function editDesc() {
                //Get element that contains new description
                var txt = document.getElementById("descInput");
                
                //Check if description is empty
                if(!isValid())
                    return;
                
                //Set the surveys description
                survey.setDesc(cleanTxt(txt.value));
                
                //Remove edit description action from action area
                resetAction();
                
                //Update survey preview
                preview();
            }
            
            //Resets action area to default which is add question
            function resetAction() {
                //Declare variables
                var output = "";
                
                //Build output string to add question
                output += "<h3>Add A Question</h3>";
                output += "<input type='button' id='addQues' value='Add Question' onclick='addQues()' />";
                output += "<input type='button' id='addAns' value='Add Another Answer' onclick='addAns()' /><br/>";
                output += "<label for='ques'>Question<label><br/>";
                output += "<input id='ques' class='req' type='text' /><span class='err'></span><br/>";
                output += "<label>Answers</label><br/>";
                
                //Set output in action area
                actionArea.innerHTML = output;
                
                //Add two answers as default
                addAns();
                addAns();
            }
            
            //Add another answer to action area
            function addAns() {
                //Declare variables
                var output = "";
                
                //Build output string
                output += "<input class='ans req' type='text' /><span class='err'></span><br/>";
                
                //Append to action area
                actionArea.innerHTML += output;
            }
            
            //Add question to survey
            function addQues() {
                //Declare variables
                var q;//The question
                var name;//Questions name
                var cat = "ques" + survey.qArray.length;
                var ans = [];//Array of answers
                
                //Initialize variables
                name = document.getElementById("ques").value;
                name = cleanTxt(name);
                ans = document.getElementsByClassName("ans");
                
                //Check for any empty answers
                if(!isValid())//If not valid
                    return;//Exit function, don't add question
                
                //Create question
                q = new Question(cat, name);
                
                //Add answers to question
                for(var i = 0; i < ans.length; ++i) {
                    q.addAns(cleanTxt(ans[i].value));//Add answer to question
                }
                
                //Push to survey
                survey.pushQ(q);
                
                //Reset action area
                resetAction();
                
                //Update survey preview
                preview();
            }
            
            //Sets error messages and returns if valid fields
            function isValid() {
                //Declare variables
                var req = document.getElementsByClassName("req");//All required inputs
                var err = document.getElementsByClassName("err");//All error spans
                var status = true;
                
                //Set / remove error messages as necessary
                for(var i = 0; i < req.length; ++i){
                    if(req[i].value === ""){
                        err[i].innerHTML = "*Required";//Set error message
                        status = false;//Mark fields as incomplete
                    } else {
                        err[i].innerHTML = "";//Remove error message
                    }
                }
                //Return status
                return status;
            }
            
            //Removes bad values from text input
            function cleanTxt(txt) {
                var temp = txt.trim();
                temp = temp.replace(/['"]/g, "");
                return temp;
            }
            
            //Sets json text in hidden text field to pass in form
            function setJsonText() {
                document.getElementById("surveyName").value = survey.getName();
                document.getElementById("jsonText").value = JSON.stringify(survey);
            }
       </script>
    </body>
</html>
