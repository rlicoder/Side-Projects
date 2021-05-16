#include <bits/stdc++.h>
#include "Form.hpp"
#include "Model.hpp"
#include "Controller.hpp"
#include "View.hpp"

using namespace std;

int main()
{
    Model sys;
    View mainmenu("mainmenu.txt");
    Controller mainMenuCont(mainmenu.getSize());
    
    //do while menu loop
    do
    {
	mainmenu.display();
	mainMenuCont.TakeInput();
	//name and id 
        string str, str2;
        switch(mainMenuCont.ReturnInput())
        {
            case 1: 
		//login case
		cin.ignore();
		cout << "Enter first and last name: ";
		getline(cin, str);
                cout << "Enter ID: ";
                cin >> str2;
		//pass to the model class to handle
                if (sys.handleLogin(str, str2))
                {
                    break;
                }
		//handle the admin and student menu functions
                sys.getAdmin() ? sys.handleAdmin() : sys.handleStudent();
                break;
            case 2:
		//terminate
                cout << "Program Terminated" << endl;
		//save info to database;
		sys.saveInfo();
                exit(0);
            default:
                break;
        }
    }
    while(mainMenuCont.ReturnInput() != 2);

    return 0;
}