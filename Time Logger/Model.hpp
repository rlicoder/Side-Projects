#ifndef MODEL_HPP
#define MODEL_HPP
#include <bits/stdc++.h>
#include "Student.hpp"

using namespace std;

class Model
{
    private:
	vector<string> classes;
	vector<string> valid_student_ids;
        vector<string> valid_admin_ids;
        vector<Student> students;

	bool loggedin;
        bool admin;
	string currentid;
	
    public:
	Model();
        
        bool getAdmin() { return this->admin; };

	bool handleLogin(string id);
        
        void handleStudent();
        
        void handleAdmin();
        
        void studentSwitch(int choice);
        
        bool adminSwitch(int choice);
        
        void displayStudents();
        
        void displayClasses();
        
        void createClass();
        
        void deleteClass();
        
        void update();

};

#endif /* MODEL_HPP */

