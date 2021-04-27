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

};

#endif
