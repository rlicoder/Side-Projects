#include "Question.hpp"

enum QUESTION_TYPE{ SHORT_ANSWER, MULTIPLE_CHOICE, CHECK_BOX };

Question::Question(int t, string q)
{
    //question type and question initializer
    question = q;
    type = t;
};

Question::Question(int t, string q, vector<string> qs)
{
    //type, question and extra qs if the question is check box or multiple choice
    type = t;
    question = q;
    extraq = qs;
};

string Question::getQuestion()
{
    string str = "";
    //based on the type, output respectively
    switch (type)
    {
	case SHORT_ANSWER:
	{
	    //case 
	    str += this->question;
	    break;
	}
	case MULTIPLE_CHOICE:
	case CHECK_BOX:
	{
	    //output the question and then the extra values that go with the multiple choice and check box questions.
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

//basic getters.
string Question::getExtraQ(int choice)
{
    return extraq[choice];
};

int Question::getExtraQSize()
{
    return extraq.size();
};
