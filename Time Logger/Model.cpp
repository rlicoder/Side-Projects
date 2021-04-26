#include "Model.hpp"

Model::Model()
{
    this->loggedin = false;
    this->currentid = "";
    
    ifstream in;
    in.open("classes.txt");

    string str;
    while (in >> str)
    {
        classes.push_back(str);
    }
    in.close();

    in.open("ids.txt");
    while (in >> str)
    {
	valid_ids.push_back(str);
    }
    in.close();
};

bool Model::handleLogin(int choice)
{
    string id = "";
    switch (choice)
    {
	case 1:
	    cout << "Enter ID: ";
	    cin >> id;
	    break;
	case 2:
	    cout << "Program Terminated" << endl;
	    exit(1);
	    break;
	default:
	    cout << "Error in handleLogin case";
	    break;
    }
    if (id != "")
    {
	for (int i = 0; i < valid_ids.size(); i++)
	{
	    if (valid_ids[i] == id)
	    {
		this->loggedin = true;
		this->currentid = id;
	    }
	}
    }
    if (this->loggedin)
    {
	cout << "Login Successful" << endl;
	return false;
    }
    else
    {
	cout << "Login Unsuccessful" << endl;
    }
    return true;
}