#include "Surveyee.hpp"

Surveyee::Surveyee(string sname, string sid)
{
    //name and id constructor
    this->name = sname;
    this->id = sid;
};


void Surveyee::getSurveyResults()
{
    //iterate through each answered survey and output the results
    for (int i = 0; i < answered.size(); i++)
    {
	cout << answered[i].getName() << endl;
	answered[i].outputAnswers();
    }
};

void Surveyee::insertSurvey(Form x)
{
    //push back a form that has been filled out
    answered.push_back(x);
};

string Surveyee::saveResults()
{
    string str = "";
    //output the name and id
    str += this->name + '\n';
    str += this->id + '\n';
    //output the number of surveys that they answered
    str += to_string((int)answered.size()) + '\n';
    for (int i = 0; i < answered.size(); i++)
    {
	//output the name of the survey
	str += answered[i].getName() + '\n';
	//output the number of answered
	str += to_string((int)answered[i].getAnswerSize()) + '\n';
	for (int j = 0; j < answered[i].getAnswerSize(); j++)
	{
	    //output the string answer
	    str += answered[i].getAnswer(j);
	}
    }
    return str;
}

void Surveyee::pushSurvey(vector <Form> a)
{
    //push a vector of forms. reading from database.
    this->answered = a;
};