#ifndef CONTROLLER_HPP
#define CONTROLLER_HPP
#include <bits/stdc++.h>

using namespace std;

class Controller
{
    private:
	int choice;
	int max;
    public:
	Controller(int end);
	void TakeInput();
	int ReturnInput();
};

#endif /* CONTROLLER_HPP */

