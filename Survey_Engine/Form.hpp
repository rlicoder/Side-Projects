#ifndef FORM_HPP
#define FORM_HPP
#include "Question.hpp"
#include <bits/stdc++.h>

using namespace std;

class Form
{
    private:
	string formName;
	vector<Question> questions;
	vector<vector<string>> answers;
    public:
	Form(string filename);

	string getName() { return this->formName; };
	
	void takeInput();

	void outputAnswers();

	string getAnswer(int i);

	int getAnswerSize (int i) { return answers[i].size(); };

	int getQuestionSize() { return this->questions.size(); };

	int getQuestionType(int i);

	Question getQuestion(int i) { return this->questions[i]; };

};

#endif /* FORM_HPP */

