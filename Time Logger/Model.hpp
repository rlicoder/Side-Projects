#ifndef MODEL_HPP
#define MODEL_HPP
#include <bits/stdc++.h>

using namespace std;

class Model
{
    private:
	vector<string> classes;
	vector<string> valid_ids;

	bool loggedin;
	string currentid;
	
    public:
	Model();

	bool handleLogin(int choice);

};

#endif /* MODEL_HPP */

