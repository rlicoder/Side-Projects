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

    do
    {
	mainmenu.display();
	mainMenuCont.TakeInput();
        string str;
        switch(mainMenuCont.ReturnInput())
        {
            case 1: 
                cout << "Enter ID: ";
                cin >> str;
                if (sys.handleLogin(str))
                {
                    break;
                }
                sys.getAdmin() ? sys.handleAdmin() : sys.handleStudent();
                break;
            case 2:
                cout << "Program Terminated";
                exit(1);
            default:
                break;
        }
    }
    while(mainMenuCont.ReturnInput() != 2);
}
