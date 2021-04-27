#include "Model.hpp"
#include "View.hpp"
#include "Controller.hpp"
#include "Student.hpp"

Model::Model()
{
    this->loggedin = false;
    this->admin = false;
    this->currentid = "";
    
    ifstream in;
    in.open("classes.txt");

    string str;
    while (in >> str)
    {
        classes.push_back(str);
    }
    in.close();

    in.open("ids.txt");
    while (in >> str)
    {
	valid_student_ids.push_back(str);
    }
    in.close();
    
    in.open("admin_ids.txt");
    while (in >> str)
    {
        valid_admin_ids.push_back(str);
    }
    in.close();
    
    in.open("studentdata.txt");
    string id, name, class_name;
    int start, end;
    in >> id;
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

bool Model::handleLogin(string id)
{
    if (id != "")
    {
	for (int i = 0; i < valid_student_ids.size(); i++)
	{
	    if (valid_student_ids[i] == id)
	    {
		this->loggedin = true;
		this->currentid = id;
                this->admin = false;
	    }
	}
        for (int i = 0; i < valid_admin_ids[i].size(); i++)
        {
            if (valid_admin_ids[i] == id)
            {
                this->loggedin = true;
                this->currentid = true;
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
    this->studentSwitch(studentMenuCont.ReturnInput());
};

void Model::handleAdmin()
{
    View adminMenu("adminmenu.txt");
    Controller adminMenuCont(adminMenu.getSize());
    adminMenu.display();
    adminMenuCont.TakeInput();
    while (this->adminSwitch(adminMenuCont.ReturnInput()))
    {
        this->update();
        adminMenu.display();
        adminMenuCont.TakeInput();
    }
            
};

bool Model::adminSwitch(int choice)
{
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
            return true;
        case 4: 
            this->deleteClass();
            return true;
        default:
            return false;
            break;
            
    }
};

void Model::studentSwitch(int choice)
{
    
};

void Model::displayStudents()
{
    for (int i = 0; i < students.size(); i++)
    {
        students[i].displayAllInfo();
    }
}

void Model::displayClasses()
{
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
    int choice;
    View delClass("classes.txt");
    Controller delClassCont(delClass.getSize());
    delClass.display();
    delClassCont.TakeInput();
    classes.erase(classes.begin() + delClassCont.ReturnInput()-1);
}

void Model::update()
{
    ofstream out;
    out.open("classes.txt");
    for (int i = 0; i < classes.size(); i++)
    {
        out << classes[i] << endl;
    }
    out.close();
};