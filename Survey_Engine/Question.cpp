#include "Question.hpp"

enum QUESTION_TYPE{ SHORT_ANSWER, MULTIPLE_CHOICE };

Question::Question(int t, string q)
{
    question = q;
    type = t;
};

Question::Question(int t, string q, vector<string> qs)
{
    type = t;
    question = q;
    extraq = qs;
};

string Question::getQuestion()
{
    string str = "";
    switch (type)
    {
	case 0:
	{
	    str += this->question;
	    break;
	}
	case 2:
	case 1:
	{
	    str += this->question;
	    for (int i = 0; i < extraq.size(); i++)
	    {
		str += '\n';
		str += '1' + i;
		str += ". ";
		str += extraq[i];
	    }
	    break;
	}
	default:
	{
	    break;
	}
    };
    return str;
};

string Question::getExtraQ(int choice)
{
    return extraq[choice];
};

int Question::getExtraQSize()
{
    return extraq.size();
};
