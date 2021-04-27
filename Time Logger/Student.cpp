#include "Student.hpp"
#include "Session.hpp"

Student::Student(string sname, string sid)
{
    name = sname;
    id = sid;
};

void Student::pushSession(Session s)
{
    sessions.push_back(s);
};

void Student::displayAllInfo()
{
    cout << "Name: " << this->name << endl;
    cout << "ID: " << this->id << endl;
    for (int i = 0; i < this->sessions.size(); i++)
    {
        cout << sessions[i].getClassName() << endl;
        sessions[i].getStart().output();
        sessions[i].getEnd().output();
    }
};
