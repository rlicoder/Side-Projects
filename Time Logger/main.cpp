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
    }
    while(sys.handleLogin(mainMenuCont.ReturnInput()));

    View studentmenu("studentmenu.txt");
    Controller studentMenuCont(studentmenu.getSize());

    studentmenu.display();
    studentMenuCont.TakeInput();

}
