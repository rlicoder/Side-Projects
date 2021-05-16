#include <bits/stdc++.h>
#include <ctime>
#include "Session.hpp"
#include "Date.hpp"
#include "View.hpp"
#include "Controller.hpp"
#include "Model.hpp"

using namespace std;

int main()
{

    Model sys;
    View mainmenu("mainmenu.txt");
    Controller mainMenuCont(mainmenu.getSize());

    //do while menu
    do
    {
	mainmenu.display();
	mainMenuCont.TakeInput();
	//name and id holders
        string str, str2;
        switch(mainMenuCont.ReturnInput())
        {
            case 1: 
		//getline clear buffer
		cin.ignore();
		cout << "Enter first and last name: ";
		getline(cin, str);
                cout << "Enter ID: ";
                cin >> str2;
		//pass to model class
                if (sys.handleLogin(str, str2))
                {
                    break;
                }
		//handle admin functions or student function based on the login
                sys.getAdmin() ? sys.handleAdmin() : sys.handleStudent();
                break;
            case 2:
		//terminate.
		//all database updates are written within the student/admin menu after the respective edits.
                cout << "Program Terminated";
                exit(1);
            default:
                break;
        }
    }
    while(mainMenuCont.ReturnInput() != 2);
    //2 is for exit
}
