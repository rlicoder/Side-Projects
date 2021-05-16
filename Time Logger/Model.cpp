#include "Model.hpp"
#include "View.hpp"
#include "Controller.hpp"
#include "Student.hpp"
#include "Date.hpp"

Model::Model()
{
    //basic init
    this->loggedin = false;
    this->admin = false;
    this->currentid = "";
    this->currentname = "";
    this->currentsession = "";
    this->insession = false;

    //read in data from files
    
    ifstream in;
    in.open("classes.txt");

    string str, str2;
    while (in >> str)
    {
        classes.push_back(str);
    }
    in.close();

    in.ignore();
    in.open("valid_student_ids.txt");
    while (getline(in, str))
    {
	in >> str2;
	valid_student_ids.push_back({str, str2});
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
    
    in.open("studentdata.txt");
    string id, name, class_name;
    int start, end;
    in >> id;
    //read in survey data from students
    while (id != "-1")
    {
        in.ignore();
        getline(in, name);
        Student a(name, id);
        in >> class_name;
        while (class_name != "-1")
        {
            in >> start >> end;
            Session b(class_name, start, end);
            a.pushSession(b);
            in >> class_name;
        }
        students.push_back(a);
        in >> id;
    }
    
};

bool Model::handleLogin(string name, string id)
{
    if (id != "" && name != "")
    {
	//go through each valid id
	for (int i = 0; i < valid_student_ids.size(); i++)
	{
	    //student login success
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
	    //admin login success
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
	//outputting login result to the user
	cout << "Login Successful" << endl;
        cout << (this->admin ? "Admin" : "Student") << endl;
	return false;
    }
    else
    {
	cout << "Login Unsuccessful" << endl;
    }
    //return that the login was successful, otherwise, continue login loop
    return true;
}

void Model::handleStudent()
{
    View studentMenu("studentmenu.txt");
    Controller studentMenuCont(studentMenu.getSize());
    //tell the user what class they're in
    if (this->insession)
    {
	cout << "Current Session: " << this->currentsession << endl;
    }
    studentMenu.display();
    studentMenuCont.TakeInput();
    while(this->studentSwitch(studentMenuCont.ReturnInput()))
    {
	//tell the user if they are in a class or not
	if (this->insession)
	{
	    cout << "Current Session: " << this->currentsession << endl;
	}
	else
	{
	    cout << "You are currently not in a session" << endl;
	}
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
    //take admin menu input
    while (this->adminSwitch(adminMenuCont.ReturnInput()))
    {
        adminMenu.display();
        adminMenuCont.TakeInput();
    }
            
};

bool Model::adminSwitch(int choice)
{
    //switch branching. function names pretty self explanatory.
    switch(choice)
    {
        case 1: 
            this->displayStudents();
            return true;
        case 2:
            this->displayClasses();
            return true;
        case 3:
            this->createClass();
	    this->updateClass();
            return true;
        case 4: 
            this->deleteClass();
	    this->updateClass();
            return true;
	case 5:
	    this->addStudent();
	    this->updateStudent();
	    return true;
	case 6:
	    this->deleteStudent();
	    this->updateStudent();
	    return true;
        default:
	    this->admin = false;
	    this->loggedin = false;
	    this->currentid = "";
            return false;
            break;
            
    }
};

bool Model::studentSwitch(int choice)
{
    //switch for student. also self explanatory
    switch(choice)
    {
	case 1:
	    this->joinClass();
	    return true;
	case 2:
	    this->leaveClass();
	    this->updateHours();
	    return true;
	case 3:
	    this->checkHours();
	    return true;
	case 4:
	    if (this->insession)
	    {
		this->leaveClass();
		this->updateHours();
	    }
	    this->loggedin = false;
	    this->currentid = "";
	    this->currentname = "";
	    this->currentsession = "";
	    return false;
	default:
	    cout << "Error";
	    return false;
    }
};

void Model::displayStudents()
{
    //output all students.
    for (int i = 0; i < students.size(); i++)
    {
        students[i].displayAllInfo();
    }
}

void Model::displayClasses()
{
    //output the name of all classes.
    for (int i = 0; i < classes.size(); i++)
    {
        cout << classes[i] << endl;
    }
};

void Model::createClass()
{
    string str;
    cout << "Enter class: ";
    cin >> str;
    classes.push_back(str);
};

void Model::deleteClass()
{
    //delete string from vector. Does not affect previous logs.
    int choice;
    View delClass("classes.txt");
    Controller delClassCont(delClass.getSize());
    delClass.display();
    delClassCont.TakeInput();
    classes.erase(classes.begin() + delClassCont.ReturnInput()-1);
}

void Model::updateClass()
{
    //rewrite classes into database.
    ofstream out;
    out.open("classes.txt");
    for (int i = 0; i < classes.size(); i++)
    {
        out << classes[i] << endl;
    }
    out.close();
};

void Model::updateHours()
{
    ofstream out;
    out.open("studentdata.txt");
    for (int i = 0; i < students.size(); i++)
    {
	//output name and id
	out << students[i].getID() << endl;
	out << students[i].getName() << endl;
	for (int j = 0; j < students[i].getSize(); j++)
	{
	    //output the class name, and their start/end times
	    out << students[i].getSessionClassName(j) << endl;
	    out << students[i].getSessionStartUnix(j) << endl;
	    out << students[i].getSessionEndUnix(j) << endl;
	}
	out << -1 << endl;
    }
    out << -1 << endl;
    out.close();
};

void Model::joinClass()
{
    if (this->insession)
    {
	//check if the user is already in a session
	cout << "Error, you are already in a session" << endl;
	return;
    }
    View joinClassMenu("classes.txt");
    Controller joinClassCont(joinClassMenu.getSize());

    joinClassMenu.display();
    joinClassCont.TakeInput();

    //successful login
    this->insession = true;
    this->currentsession = classes[joinClassCont.ReturnInput()-1];

    //init timer
    start = time(0);
};

void Model::leaveClass()
{
    if (!this->insession)
    {
	cout << "Error, you are not currently in a session" << endl;
	return;
    }
    this->insession = false;

    //end timer;
    end = time(0);

    //create the session and push it in
    Session a(currentsession, start, end);

    this->currentsession = "";

    for (int i = 0; i < students.size(); i++)
    {
	//validate id, ids should be unique
	if (students[i].getID() == currentid)
	{
	    students[i].pushSession(a);
	}
    }
};

void Model::checkHours()
{
    //create a map, key is class name, value is time spent total
    map<string, int> times;
    //iterate through all classes, add up all the times.	
    for (int i = 0; i < students.size(); i++)
    {
	if (students[i].getName() == this->currentname && students[i].getID() == this->currentid)
	{
	    for (int j = 0; j < students[i].getSize(); j++)
	    {
		times[students[i].getSessionClassName(j)] += students[i].getSessionEndUnix(j) - students[i].getSessionStartUnix(j);
	    }
	}
    }
    //output results
    for (auto it : times)
    {
	cout << it.first << ": " << it.second << endl;
    }
};

void Model::addStudent()
{
    cin.ignore();
    cout << "Enter a student's first and last name: ";
    string str, str2;
    getline(cin, str);
    cout << "Enter the student's ID: ";
    cin >> str2;
    //basic student creation
    this->pushStudent(make_pair(str, str2));
};

void Model::pushStudent(pair<string, string> a)
{
    //push a pair value to valid student id's
    valid_student_ids.push_back(a);
};

void Model::deleteStudent()
{
    View delStudentMenu("valid_student_ids.txt");
    Controller delStudentCont(delStudentMenu.getSize());

    delStudentMenu.display();
    delStudentCont.TakeInput();

    //using vector erase to destroy a pair based erase.
    //input can take either the value for the id or the name.
    //math magic :P
    valid_student_ids.erase(valid_student_ids.begin() + (delStudentCont.ReturnInput() % 2 == 0 ? delStudentCont.ReturnInput()-1 : delStudentCont.ReturnInput()) / 2);
};

void Model::updateStudent()
{
    ofstream out;
    //rewrite student data to the database
    out.open("valid_student_ids.txt");
    for (int i = 0; i < valid_student_ids.size(); i++)
    {
	out << valid_student_ids[i].first << endl;
	out << valid_student_ids[i].second << endl;
    }
};