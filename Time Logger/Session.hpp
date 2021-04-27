#ifndef SESSION_HPP
#define SESSION_HPP
#include "Date.hpp"
#include <bits/stdc++.h>

using namespace std;

class Session
{
    private:
        Date start;
        Date end;
        string class_name;
    public:
        Session(string sclass_name, int sstart, int send);
        
        Date getStart() { return start; };
        Date getEnd() { return end; };
        string getClassName() { return class_name; };

};

#endif
