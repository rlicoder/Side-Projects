#ifndef STUDENT_HPP
#define STUDENT_HPP
#include <bits/stdc++.h>
#include "Session.hpp"

using namespace std;

class Student
{
    private:
        string name;
        string id;
        vector<Session> sessions;
    public:
        Student(string sname, string sid);
        
        void pushSession(Session s);
        
        void displayAllInfo();
	
	string getID() { return this->id; };

	string getName() { return this->name; };

	string getSessionClassName(int i);

	int getSessionStartUnix(int i);

	int getSessionEndUnix(int i);

	int getSize() { return this->sessions.size(); };

};

#endif
