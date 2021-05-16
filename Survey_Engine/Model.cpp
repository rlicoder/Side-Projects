#include "Model.hpp"
#include "View.hpp"
#include "Controller.hpp"

enum QUESTION_TYPE{ SHORT_ANSWER, MULTIPLE_CHOICE, CHECK_BOX };

Model::Model()
{
    //init to default values
    this->loggedin = false;
    this->admin = false;
    this->currentid = "";
    this->currentname = "";
    this->currentsession = "";
    this->insession = false;

    
    ifstream in;
    string str, str2;

    //read in all survey names
    in.open("surveynames.txt");
    while (in >> str)
    {
	this->surveyNames.push_back(str);
    }
    in.close();
    
    //read in all valid student ids
    in.open("valid_student_ids.txt");
    while (getline(in, str))
    {
	in >> str2;
	//push into valid ids 
	valid_student_ids.push_back({str, str2});
	//push into as sample size
	sample.emplace_back(str, str2);
	in.ignore();
    }
    in.close();
    
    in.open("admin_ids.txt");
    while (getline(in, str))
    {
	in >> str2;
	//read in admin ids
        valid_admin_ids.push_back({str, str2});
	in.ignore();
    }
    in.close();
    
    //read in all surveys using constructor
    for (int i = 0; i < surveyNames.size(); i++)
    {
	string str = surveyNames[i] + ".txt";
	Form x(str);
	surveys.push_back(x);
    }

    //read in student survey data (already taken)
    in.open("surveydata.txt");
    int n, ns, nq;
    in >> n;
    in.ignore();
    for (int i = 0; i < n; i++)
    {
	//read in name and id
	getline(in, str);
	getline(in, str2);
	//read in number of surveys
	in >> ns;
	in.ignore();
	//if zero, read in the next student
	if (ns == 0)
	{
	    continue;
	}
	//create a vector of forms
	vector<Form> z;
	for (int i = 0; i < ns; i++)
	{
	    string s;
	    //read in survey name
	    getline(in, s);
	    //read in number of questions
	    in >> nq;
	    in.ignore();
	    //create a vector of answers
	    vector<string> a(nq);
	    for (int i = 0; i < nq; i++)
	    {
		//read in each answer
		getline(in, a[i]);
	    }
	    z.emplace_back(s, a);
	}
	//push the survey to the appropriate student
	this->pushSurvey(str, str2, z);
    }
    in.close();
};

bool Model::handleLogin(string name, string id)
{
    if (id != "" && name != "")
    {
	//iterate through all the ids
	for (int i = 0; i < valid_student_ids.size(); i++)
	{
	    //check if the student ids match
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
	    //iterate through all the admin ids
            if (valid_admin_ids[i] == make_pair(name, id))
            {
                this->loggedin = true;
                this->currentid = id;
                this->admin = true;
            }
        }
    }
    //return if the login is successfull or unsucessful
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
    //output student menu and take input
    View studentMenu("studentmenu.txt");
    Controller studentMenuCont(studentMenu.getSize());
    studentMenu.display();
    studentMenuCont.TakeInput();
    //do while student menu loop with switch case
    while(this->studentSwitch(studentMenuCont.ReturnInput()))
    {
	studentMenu.display();
	studentMenuCont.TakeInput();
    }
};

void Model::handleAdmin()
{
    //output admin menu and take input
    View adminMenu("adminmenu.txt");
    Controller adminMenuCont(adminMenu.getSize());
    adminMenu.display();
    adminMenuCont.TakeInput();
    //do while admin menu loop with switch case
    while (this->adminSwitch(adminMenuCont.ReturnInput()))
    {
        adminMenu.display();
        adminMenuCont.TakeInput();
    }
};

bool Model::adminSwitch(int choice)
{
    //self explanatory
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
    //also self explanatory
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
    //take in the name of the survey
    cin.ignore();
    cout << "Enter the name of the survey: ";
    getline(cin, name);
    ofstream out("surveynames.txt", ios::app);
    out << name << endl;
    out.close();
    name += ".txt";
    //create a file for the survey

    //init
    View questionType("types.txt");
    Controller questionTypeCont(questionType.getSize());

    int n;
    //read in and output the number of questions
    cout << "How many questions are in this survey: ";
    cin >> n;
    out.open(name, ios::app);
    out << n << endl;
    out.close();
    for (int i = 0; i < n; i++)
    {
	//take in the question type and create the question based on the type
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

    //short answer just needs the question
    //multiple choice and check box need the extra choices for the user to choose
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
    //take user input and erase from the vector of surveys
    //cannot delete the actual survey info file yet nor from students

    surveys.erase(surveys.begin() + delSurvey.ReturnInput()-1);
};

void Model::viewSurveyResults()
{
    //output all results of the surveys
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
    //take in the survey answers
    fill.takeInput();

    //push to the sample group data
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
    //iterate through all surveys
    for (int i = 0; i < sample.size(); i++)
    {
	//if matching to the user's id and name
	if (sample[i].getName() == this->currentname && sample[i].getID() == this->currentid)
	{
	    //output results entered by the user
	    sample[i].getSurveyResults();
	}
    }
};

void Model::saveInfo()
{
    ofstream out;

    //output all survey names so the model knows which files to read in for data
    out.open("surveynames.txt");
    for (int i = 0; i < surveyNames.size(); i++)
    {
	out << surveyNames[i] << endl;
    }
    out.close();

    //for each survey name
    for (int i = 0; i < surveys.size(); i++)
    {
	//open the survey data file
	out.open(surveys[i].getName() + ".txt");
	//read in how many questions to look for
	out << surveys[i].getQuestionSize() << endl;
	//iterate through each question
	for (int j = 0; j < surveys[i].getQuestionSize(); j++)
	{
	    //output the type of question
	    out << surveys[i].getQuestion(j).getType() << endl;
	    //output the literal question string 
	    out << surveys[i].getQuestion(j).getLitQuestion() << endl;
	    //if there are extra question elements
	    if (surveys[i].getQuestion(j).getExtraQSize() != 0)
	    {
		//output the size of the extra elements
		out << surveys[i].getQuestion(j).getExtraQSize() << endl;
		//iterate through each extra q
		for (int k = 0; k < surveys[i].getQuestion(j).getExtraQSize(); k++)
		{
		    //output the question element
		    out << surveys[i].getQuestion(j).getExtraQ(k) << endl;
		}
	    }
	}
    }
    out.close();

    //for each survey, output the student answers
    out.open("surveydata.txt");
    out << sample.size() << endl;
    for (int i = 0; i <  sample.size(); i++)
    {
	out << sample[i].saveResults();
    }
    out.close();
};

void Model::pushSurvey(string name, string id, vector<Form> a)
{
    for (int i = 0; i < sample.size(); i++)
    {
	//push a survey to the correct student.
	if (sample[i].getName() == name && sample[i].getID() == id)
	{
	    sample[i].pushSurvey(a);
	}
    }
};












