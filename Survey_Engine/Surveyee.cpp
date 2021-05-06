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