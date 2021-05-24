/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


//Survey constructor with copy constructor(if 1 arg provided)
function Survey(name, desc, qArray) {
    var numArg = arguments.length;//Get number of arguments
    if(numArg === 0 || numArg > 3) {//If invalid number of arguments
        this.name = "default name";
        this.desc = "default description";
        this.qArray = [];
    } else if(numArg === 3) {//Survey with all 3 arg
        this.name = name;
        this.desc = desc;
        this.qArray = qArray;
    } else if(numArg === 2) {//Survey with no questions
        this.name = name;
        this.desc = desc;
        this.qArray = [];
    } else if(numArg === 1) {//Copy constructor
        this.name = name.name;
        this.desc = name.desc;
        this.qArray = [];
        for(var i = 0; i < name.qArray.length; ++i) {
            this.qArray.push(new Question(name.qArray[i]));
        }
    }
}

//Set survey name
Survey.prototype.setName = function(name) {
    this.name = name;
};

//Return survey name
Survey.prototype.getName = function() {
    return this.name;
};

//Set survey description
Survey.prototype.setDesc = function(desc) {
    this.desc = desc;
};

//Return survey description
Survey.prototype.getDesc = function() {
    return this.desc;
};

//Push a question to survey
Survey.prototype.pushQ = function(quest) {
    this.qArray.push(quest);
};

//Pop a question from the survey
Survey.prototype.popQ = function() {
    this.qArray.pop();
};

//Add a question at the specified index
Survey.prototype.addQAt = function(index, ques) {
    if(index < 0 || index > this.qArray.length) {//Invalid index
        console.log("Invalid index or may cause holes. Index: " + index);
    } else if(index > 0 && index < this.qArray.length) {//Index (0,qArray.length)
        var temp1 = this.qArray.slice(0, index);
        var temp2 = this.qArray.slice(index, this.qArray.length);
        temp1.push(ques);
        this.qArray = temp1.concat(temp2);
    } else if(index == this.qArray.length) {//Index is qArray.length
        this.qArray.push(ques);
    } else {//Index is 0
        this.qArray.unshift(ques);
    }
};

//Remove a question at the specified index
Survey.prototype.rmvQAt = function(index) {
    if(index < 0 || index >= this.qArray.length) {
        console.log("No question exists at index = " + index);
    } else {
        this.qArray.splice(index, 1);
    }
};

//Return question at index
Survey.prototype.qAt = function(index) {
    //Check for invalid index
    if(index < 0 || index >= this.qArray.length) {
        return null;//Returns empty question object
    }
    //Return question at index
    return this.qArray[index];
};

//Return survey as HTML formatted string
Survey.prototype.toHTML = function() {
    //Declare variables
    var output = "";//Final html output string
    var numQuest = this.qArray.length;//Number of questions in survey
    
    //Display name and description in paragraphs
    output += "<h2>" + this.name + "</h2>";//Output name
    output += "<h3>" + this.desc + "</h3>";//Output description
    
    //Output each question
    for(var i = 0; i < numQuest; ++i) {
        output += this.qArray[i].toHTML();
    }
    //Return survey string in HTML format
    return output;
};

//Display survey with document.write
Survey.prototype.display = function() {
    //Declare variables
    var output = "";//Final html output string
    var numQuest = this.qArray.length;//Number of questions in survey
    
    //Display name and description in paragraphs
    output += "<h2>" + this.name + "</h2>";//Output name
    output += "<h3>" + this.desc + "</h3>";//Output description
    
    //Output each question
    for(var i = 0; i < numQuest; ++i) {
        output += this.qArray[i].toHTML();
    }
    //Display survey
    document.write(output);
};

//Display result set with answers of query
Survey.prototype.resultSet = function() {
    var output = "<h1>Cumulative Results</h1>";
    output += "<h2>" + this.name + "</h2>";
    output += "<h3>" + this.desc + "</h3>";
    for(var i = 0; i < this.qArray.length; ++i) {
        output += this.qArray[i].showAnswers();
    }
    return output;
};





















