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
    
    do
    {
	mainmenu.display();
	mainMenuCont.TakeInput();
        string str, str2;
        switch(mainMenuCont.ReturnInput())
        {
            case 1: 
		cin.ignore();
		cout << "Enter first and last name: ";
		getline(cin, str);
                cout << "Enter ID: ";
                cin >> str2;
                if (sys.handleLogin(str, str2))
                {
                    break;
                }
                sys.getAdmin() ? sys.handleAdmin() : sys.handleStudent();
                break;
            case 2:
                cout << "Program Terminated" << endl;
		sys.saveInfo();
                exit(0);
            default:
                break;
        }
    }
    while(mainMenuCont.ReturnInput() != 2);

    return 0;
}