#ifndef STUDENT_HPP
#define STUDENT_HPP
#include <bits/stdc++.h>
#include "Session.hpp"

using namespace std;

class Student
{
    private:
        vector<Session> sessions;
    public:
        //hash constructor
        Student(string encryption);

        //new student constructor
        Student(string username, string password);

};

#endif
