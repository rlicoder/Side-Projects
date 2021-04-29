#ifndef MODEL_HPP
#define MODEL_HPP
#include <bits/stdc++.h>
#include "Student.hpp"

using namespace std;

class Model
{
    private:
	vector<string> classes;
	vector<pair<string,string>> valid_student_ids;
        vector<pair<string,string>> valid_admin_ids;
        vector<Student> students;

	bool loggedin;
        bool admin;
	bool insession;
	string currentsession;
	string currentid;
	string currentname;

	int start;
	int end;
	
    public:
	Model();
        
        bool getAdmin() { return this->admin; };

	bool handleLogin(string name, string id);
        
        void handleStudent();
        
        void handleAdmin();
        
        bool studentSwitch(int choice);
        
        bool adminSwitch(int choice);
        
        void displayStudents();
        
        void displayClasses();
        
        void createClass();
        
        void deleteClass();
        
        void updateClass();

	void updateHours();

	void joinClass();

	void leaveClass();

	void checkHours();

	void addStudent();

	void pushStudent(pair<string,string> a);

	void updateStudent();

	void deleteStudent();

};

#endif /* MODEL_HPP */

