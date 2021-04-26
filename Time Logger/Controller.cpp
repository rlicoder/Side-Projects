#include "Controller.hpp"

Controller::Controller(int end)
{
    max = end;
}

void Controller::TakeInput()
{
    cin >> choice;
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