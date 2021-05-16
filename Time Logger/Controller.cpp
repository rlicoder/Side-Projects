#include "Controller.hpp"

Controller::Controller(int end)
{
    //setting max for input validation
    max = end;
}

void Controller::TakeInput()
{
    cin >> choice;
    //check if the input is within range
    while (choice < 1 || choice > max)
    {
	cout << "Try again: ";
	cin >> choice;
    }
}

int Controller::ReturnInput()
{
    return this->choice;
}