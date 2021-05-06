#include "Model.hpp"
#include "View.hpp"
#include "Controller.hpp"

enum QUESTION_TYPE{ SHORT_ANSWER, MULTIPLE_CHOICE, CHECK_BOX };

Model::Model()
{
    this->loggedin = false;
    this->admin = false;
    this->currentid = "";
    this->currentname = "";
    this->currentsession = "";
    this->insession = false;

    
    ifstream in;
    string str, str2;

    in.open("surveynames.txt");
    while (in >> str)
    {
	this->surveyNames.push_back(str);
    }
    in.close();
    
    in.open("valid_student_ids.txt");
    while (getline(in, str))
    {
	in >> str2;
	valid_student_ids.push_back({str, str2});
	Surveyee s(str, str2);
	sample.push_back(s);
	in.ignore();
    }
    in.close();
    
    in.open("admin_ids.txt");
    while (getline(in, str))
    {
	in >> str2;
        valid_admin_ids.push_back({str, str2});
	in.ignore();
    }
    in.close();
    
    for (int i = 0; i < surveyNames.size(); i++)
    {
	string str = surveyNames[i] + ".txt";
	Form x(str);
	surveys.push_back(x);
    }
};

bool Model::handleLogin(string name, string id)
{
    if (id != "" && name != "")
    {
	for (int i = 0; i < valid_student_ids.size(); i++)
	{
	    if (valid_student_ids[i] == make_pair(name, id))
	    {
		this->loggedin = true;
		this->currentid = id;
		this->currentname = name;
                this->admin = false;
	    }
	}
        for (int i = 0; i < valid_admin_ids.size(); i++)
        {
            if (valid_admin_ids[i] == make_pair(name, id))
            {
                this->loggedin = true;
                this->currentid = id;
                this->admin = true;
            }
        }
    }
    if (this->loggedin)
    {
	cout << "Login Successful" << endl;
        cout << (this->admin ? "Admin" : "Student") << endl;
	return false;
    }
    else
    {
	cout << "Login Unsuccessful" << endl;
    }
    return true;
}

void Model::handleStudent()
{
    View studentMenu("studentmenu.txt");
    Controller studentMenuCont(studentMenu.getSize());
    studentMenu.display();
    studentMenuCont.TakeInput();
    while(this->studentSwitch(studentMenuCont.ReturnInput()))
    {
	studentMenu.display();
	studentMenuCont.TakeInput();
    }
};

void Model::handleAdmin()
{
    View adminMenu("adminmenu.txt");
    Controller adminMenuCont(adminMenu.getSize());
    adminMenu.display();
    adminMenuCont.TakeInput();
    while (this->adminSwitch(adminMenuCont.ReturnInput()))
    {
        adminMenu.display();
        adminMenuCont.TakeInput();
    }
};

bool Model::adminSwitch(int choice)
{
    switch(choice)
    {
	case 1:
	    this->createSurvey();
	    return true;
	case 2:
	    this->deleteSurvey();
	    return true;
	case 3:
	    this->viewSurveyResults();
	    return true;
	default:
	    return false;
    }
};

bool Model::studentSwitch(int choice)
{
    switch(choice)
    {
	case 1:
	{
	    this->fillOutSurvey();
	    return true;
	}
	case 2:
	{
	    this->viewPreviousSurvey();
	    return true;
	}
	case 3:
	{
	    return false;
	}
    }
};

void Model::createSurvey()
{
    string name;
    cin.ignore();
    cout << "Enter the name of the survey: ";
    getline(cin, name);
    ofstream out("surveynames.txt", ios::app);
    out << name << endl;
    out.close();
    name += ".txt";

    View questionType("types.txt");
    Controller questionTypeCont(questionType.getSize());

    int n;
    cout << "How many questions are in this survey: ";
    cin >> n;
    out.open(name, ios::app);
    out << n << endl;
    out.close();
    for (int i = 0; i < n; i++)
    {
	questionType.display();
	questionTypeCont.TakeInput();
	this->createQuestionSwitch(questionTypeCont.ReturnInput()-1, name);
    }
};

bool Model::createQuestionSwitch(int choice, string filename)
{
    cin.ignore();
    ofstream out;
    out.open(filename, ios::app);
    string q, str;
    vector<string> a;
    cout << "Enter the question: ";
    getline(cin, q);

    switch(choice)
    {
	case SHORT_ANSWER:
	{
	    out << SHORT_ANSWER << endl;
	    out << q << endl;
	    out.close();
	    return true;
	}
	case MULTIPLE_CHOICE:
	{
	    out << MULTIPLE_CHOICE << endl;
	    cout << "Enter one choice (-1 to stop): ";
	    getline(cin, str);
	    while (str != "-1")
	    {
		a.push_back(str);
		cout << "Enter one choice (-1 to stop): ";
		getline(cin, str);
	    }
	    out << a.size() << endl;
	    for (int i = 0; i < a.size(); i++)
	    {
		out << a[i] << endl;
	    }
	    out.close();
	    return true;
	}
	case CHECK_BOX:
	{
	    out << CHECK_BOX << endl;
	    cout << "Enter one choice (-1 to stop): ";
	    getline(cin, str);
	    while (str != "-1")
	    {
		a.push_back(str);
		cout << "Enter one choice (-1 to stop): ";
		getline(cin, str);
	    }
	    out << a.size() << endl;
	    for (int i = 0; i < a.size(); i++)
	    {
		out << a[i] << endl;
	    }
	    out.close();
	    return true;
	}
	default:
	{
	    out.close();
	    return false;
	}
    }
};

void Model::deleteSurvey()
{
    int choice;
    View delSurveyMenu("surveynames.txt");
    Controller delSurvey(surveys.size());

    delSurveyMenu.display();
    delSurvey.TakeInput();

    surveys.erase(surveys.begin() + delSurvey.ReturnInput()-1);
};

void Model::viewSurveyResults()
{
    for (int i = 0; i < sample.size(); i ++)
    {
	sample[i].getSurveyResults();
	cout << endl;
    }
};

void Model::fillOutSurvey()
{
    View viewSurvey("surveynames.txt");
    Controller viewSurveyCont(viewSurvey.getSize());

    viewSurvey.display();
    viewSurveyCont.TakeInput();

    Form fill(surveyNames[viewSurveyCont.ReturnInput()-1] + ".txt");
    fill.takeInput();

    for (int i = 0; i < sample.size(); i++)
    {
	if (sample[i].getName() == currentname && sample[i].getID() == currentid)
	{
	    sample[i].insertSurvey(fill);
	}
    }
};

void Model::viewPreviousSurvey()
{
    for (int i = 0; i < sample.size(); i++)
    {
	if (sample[i].getName() == this->currentname && sample[i].getID() == this->currentid)
	{
	    sample[i].getSurveyResults();
	}
    }
};

void Model::saveInfo()
{
    ofstream out;

    out.open("surveynames.txt");
    for (int i = 0; i < surveyNames.size(); i++)
    {
	out << surveyNames[i] << endl;
    }
    out.close();

    for (int i = 0; i < surveys.size(); i++)
    {
	out.open(surveys[i].getName() + ".txt");
	out << surveys[i].getQuestionSize() << endl;
	for (int j = 0; j < surveys[i].getQuestionSize(); j++)
	{
	    out << surveys[i].getQuestionType(i) << endl;
	    out << surveys[i].getQuestion(j).getQuestion() << endl;
	    if (surveys[i].getQuestion(j).getExtraQSize() != 0)
	    {
		for (int k = 0; k < surveys[i].getQuestion(j).getExtraQSize(); k++)
		{
		    out << surveys[i].getQuestion(j).getExtraQ(k) << endl;
		}
	    }
	}
    }
};