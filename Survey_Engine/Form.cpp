#include "Form.hpp"

enum QUESTION_TYPE{ SHORT_ANSWER, MULTIPLE_CHOICE, CHECK_BOX };

Form::Form(string filename)
{
    this->formName = filename.substr(0, filename.size()-4);
    
    ifstream in;
    in.open(filename);

    //read in the size of the questions needed to iterate through
    int size;
    in >> size;
    for (int i = 0; i < size; i++)
    {
	int type, num;
	string str;
	in >> type;
	in.ignore();
	//based on the question type
	switch(type)
	{
	    //only have to take in the literal question
	    case SHORT_ANSWER:
	    {
		getline(in, str);
		questions.emplace_back(SHORT_ANSWER, str);
		break;
	    }

	    //have to take in the extra elements
	    case MULTIPLE_CHOICE:
	    {
		string s;
		getline(in, str);
		in >> num;
		in.ignore();
		vector<string> qs;
		for (int i = 0; i < num; i++)
		{
		    getline(in, s);
		    qs.push_back(s);
		}
		questions.emplace_back(MULTIPLE_CHOICE, str, qs);
		break;
	    }
	    //same as mult choice
	    case CHECK_BOX:
	    {
		string s;
		getline(in, str);
		in >> num;
		in.ignore();
		vector<string> qs;
		for (int i = 0; i < num; i++)
		{
		    getline(in, s);
		    qs.push_back(s);
		}
		questions.emplace_back(CHECK_BOX, str, qs);
		break;
	    }

	    default:
	    {
		cout << "Error in reading in question type" << endl;
		break;
	    }
	}
    }

    in.close();

    answers = vector<vector<string>>((int)questions.size(), vector<string>());
}

Form::Form(string sname, vector<string> a)
{
    //constructor for a form that already has the answers
    this->formName = sname;
    this->answers = vector<vector<string>> (a.size(), vector<string>());
    for (int i = 0; i < a.size(); i++)
    {
	answers[i].push_back(a[i]);
    }
};

void Form::takeInput()
{
    cin.ignore();
    for (int i = 0; i < questions.size(); i++)
    {
	cout << questions[i].getQuestion() << endl;
	string ans;
	int choice;
	switch(questions[i].getType())
	{
	    //just take the short answer response
	    case SHORT_ANSWER:
	    {
		getline(cin, ans);
		answers[i].push_back(ans);
		break;
	    }
	    //take in only one choice
	    case MULTIPLE_CHOICE:
	    {
		cin >> choice;
		answers[i].push_back(questions[i].getExtraQ(--choice));
		break;
	    }
	    //take in many choices until -1 is reached
	    case CHECK_BOX:
	    {
		cin >> choice;
		while (choice != -1)
		{
		    answers[i].push_back(questions[i].getExtraQ(--choice));
		    cin >> choice;
		}
		break;
	    }
	    default: 
	    {
		break;
	    }
	}
    }
};

string Form::getAnswer(int i)
{
    //output the answers
    string str = "";
    for (int j = 0; j < answers[i].size(); j++)
    {
	str += answers[i][j] + " \n"[j+1==(int)answers[i].size()];
    }
    return str;
};

void Form::outputAnswers()
{
    //iterate through each
    for (int i = 0; i < answers.size(); i++)
    {
	cout << getAnswer(i) << endl;
    }
};

//all basic getters
int Form::getQuestionType(int i)
{
    return questions[i].getType();
};

int Form::getQuestionSize()
{
    return this->questions.size();
};

int Form::getAnswerSize()
{
    return this->answers.size();
}
