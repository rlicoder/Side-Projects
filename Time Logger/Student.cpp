#include "Student.hpp"
#include "Session.hpp"

Student::Student(string sname, string sid)
{
    //name and id constructor
    name = sname;
    id = sid;
};

void Student::pushSession(Session s)
{
    //adding a session after a student has logged out
    sessions.push_back(s);
};

void Student::displayAllInfo()
{
    //output name and id
    cout << "Name: " << this->name << endl;
    cout << "ID: " << this->id << endl;
    for (int i = 0; i < this->sessions.size(); i++)
    {
	//output class name and the time range of the respective sessions
        cout << sessions[i].getClassName() << endl;
        sessions[i].getStart().output();
        sessions[i].getEnd().output();
    }
};

//all basic getter functions

int Student::getSessionStartUnix(int i)
{
    return sessions[i].getStartUnixTime();
};

int Student::getSessionEndUnix(int i)
{
    return sessions[i].getEndUnixTime();
};

string Student::getSessionClassName(int i)
{
    return sessions[i].getClassName();
};