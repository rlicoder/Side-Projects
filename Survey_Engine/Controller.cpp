#include "Controller.hpp"

Controller::Controller(int end)
{
    //high end of valid entries
    max = end;
}

void Controller::TakeInput()
{
    cin >> choice;
    //while loop validation
    while (choice < 1 || choice > max)
    {
	cout << "Try again: ";
	cin >> choice;
    }
}

int Controller::ReturnInput()
{
    //basic getter, why am i even commenting this?
    return this->choice;
}