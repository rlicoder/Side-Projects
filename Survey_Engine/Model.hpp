#ifndef MODEL_HPP
#define MODEL_HPP
#include <bits/stdc++.h>
#include "Form.hpp"
#include "Surveyee.hpp"

class Model
{
    private:
	vector<pair<string,string>> valid_student_ids;
        vector<pair<string,string>> valid_admin_ids;
	vector<string> surveyNames;
	vector<Form> surveys;
	vector<Surveyee> sample;

	bool loggedin;
        bool admin;
	bool insession;
	string currentsession;
	string currentid;
	string currentname;

	
    public:
	Model();

	~Model()
	{
	    cout << "destroyed!";
	}
        
        bool getAdmin() { return this->admin; };

	bool handleLogin(string name, string id);
        
        void handleStudent();
        
        void handleAdmin();
        
        bool studentSwitch(int choice);
        
        bool adminSwitch(int choice);
	
	void createSurvey();

	void deleteSurvey();

	void viewSurveyResults();

	void fillOutSurvey();

	void viewPreviousSurvey();

	bool createQuestionSwitch(int choice, string filename);

	void outputAllSurveyNames();

	void saveInfo();
};

#endif /* MODEL_HPP */

