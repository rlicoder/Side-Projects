//Constructor for the Question
function Question(category,question,answers,ansCount){
    //How many arguments are provided
    var nArgs=arguments.length;//The number of arguments passed to the function
    if(nArgs==0||nArgs>4){//Empty Question
        this.cat="";
        this.qstn="";
        this.ans=[];
        this.ansCount=[];
    }else if(nArgs==4){
        this.cat=category;
        this.qstn=question;
        this.ans=answers;
        this.ansCount=ansCount;
    }else if(nArgs==3){//Question provided with all inputs
        this.cat=category;
        this.qstn=question;
        this.ans = answers;
        this.ansCount = [];
        for(var i = 0; i < this.ans.length; ++i) {
            this.ansCount.push(0);
        }
    }else if(nArgs==2){//Question provided with no answers added latter
        this.cat=category;
        this.qstn=question;
        this.ans = [];
        this.ansCount = [];
    }else{
        this.cat=category.cat;
        this.qstn=category.qstn;
        this.ans=category.ans;
        this.ansCount=category.ansCount;
    }
};
//Setting the Category
Question.prototype.setCat=function(category){
    this.cat=category;
};
//Setting the Question
Question.prototype.setQstn=function(question){
    this.qstn=question;
};
//Adding an Answer
Question.prototype.addAns=function(answer){
    this.ans.push(answer);
    this.ansCount.push(0);
};
//Incrementing an answer count
Question.prototype.ansIncrement=function(index){
    if(index<0||index>this.ans.length){
        console.log("Answer increment index: " + index + " is out of bounds");
        return;
    }
    this.ansCount[index]++;
};
//Accessing the Category
Question.prototype.getCat=function(){
    return this.cat;
};
//Accessing the Question
Question.prototype.getQstn=function(){
    return this.qstn;
};
//Accessing one of the Answers
Question.prototype.getAns=function(number){
    if(number>=0&&number<this.ans.length){
        return this.ans[number];
    }else{
        return "This is not a Question";
    }
};
//Displaying the Question
Question.prototype.display=function(){
    document.write("<p>"+this.qstn+"</p>");
    for(var i=0;i<this.ans.length;i++){
        if(this.ans[i].length>0)
            document.write("<input type='radio' name='" + this.cat + "' value='" + 
                this.ans[i] + "' required /><label>" + this.ans[i] + "</label><br/><br/>");
    }
};

//Put question into string for html
Question.prototype.toHTML = function() {
    var output = "<fieldset>";
    output += "<legend>" + this.qstn + "</legend>";
    for(var i = 0; i < this.ans.length; ++i) {
        if(this.ans[i].length > 0) {
            output += "<input type='radio' name='" + this.cat + "' value='" + 
                this.ans[i] + "' required /><label>" + this.ans[i] + "</label><br/><br/>";
        }
    }
    output += "</fieldset>";
    return output;
};

//Show answers
Question.prototype.showAnswers = function() {
    var output = "<fieldset>";
    output += "<legend>" + this.qstn + "</legend>";
    for(var i = 0; i < this.ans.length; ++i) {
        if(this.ans[i].length > 0) {
            output += "<p>Votes: " + this.ansCount[i] + "\t" + this.ans[i] + "</p>";
        }
    }
    output += "</fieldset>";
    return output;
}