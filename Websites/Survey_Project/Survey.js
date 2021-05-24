/*
 * Author:      Sebastian Hall
 * Purpose:     Survey class
 */

//Constructor for the Survey
function Survey(name,description,quesNum){
    this.name = name;
    this.description = description;
    this.quesNum = quesNum;
};
//Copy constructor
function SurveyCopy(obj) {
    var q;
    var arr = [];
    for(var i = 0; i < obj.quesNum.length; ++i){
        q = new Question(obj.quesNum[i]);
        arr.push(q);
    }
    var survey2 = new Survey(obj.name, obj.description, arr);
    return survey2;
};
//Set name
Survey.prototype.setName = function(name) {
    this.name = name;
};
//Set description
Survey.prototype.setDesc = function(description) {
    this.description = description;
};
//Set quesNum array
Survey.prototype.setQuesNum = function(quesNum) {
    this.quesNum = quesNum;
};
//Get name
Survey.prototype.getName = function() {
    return this.name;
};
//Get description
Survey.prototype.getDesc = function() {
    return this.description;
};
//Get quesNum array
Survey.prototype.getQuesNum = function() {
    return this.quesNum;
};
//Display the Survey object
Survey.prototype.display = function() {
    document.write(this.name + "<br/>" + this.description + "<br/><br/>");
    for(var i = 0; i < this.quesNum.length; ++i) {
        var group = "question" + (i + 1);
        document.write("<fieldset id=" + group  + " style=\"width:33%\">");
        this.quesNum[i].display();
        document.write("</fieldset><br/><br/>");
    }
};