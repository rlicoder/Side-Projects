#include "Surveyee.hpp"

Surveyee::Surveyee(string sname, string sid)
{
    this->name = sname;
    this->id = sid;
};


void Surveyee::getSurveyResults()
{
    for (int i = 0; i < answered.size(); i++)
    {
	cout << answered[i].getName() << endl;
	answered[i].outputAnswers();
    }
};

void Surveyee::insertSurvey(Form x)
{
    answered.push_back(x);
};

string Surveyee::saveResults()
{
    string str = "";
    str += this->name + '\n';
    str += this->id + '\n';
    str += to_string((int)answered.size()) + '\n';
    for (int i = 0; i < answered.size(); i++)
    {
	str += answered[i].getName() + '\n';
	str += to_string((int)answered[i].getAnswerSize()) + '\n';
	for (int j = 0; j < answered[i].getAnswerSize(); j++)
	{
	    str += answered[i].getAnswer(j);
	}
    }
    return str;
}

void Surveyee::pushSurvey(vector <Form> a)
{
    this->answered = a;
};