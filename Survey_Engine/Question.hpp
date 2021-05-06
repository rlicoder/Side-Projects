#ifndef QUESTION_HPP
#define QUESTION_HPP
#include <bits/stdc++.h>

using namespace std;

class Question
{
    private:
	int type;
	string question;
	vector<string> extraq;
    public:
	Question(int t, string q);

	Question(int t, string q, vector<string> qs);

	string getQuestion();

	int getType() { return this->type; };

	string getExtraQ(int choice);

	int getExtraQSize();
};

#endif /* QUESTION_HPP */

