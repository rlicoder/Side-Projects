#ifndef VIEW_HPP
#define VIEW_HPP
#include <bits/stdc++.h>

using namespace std;

class View
{
    private:
	vector<string> choices;
    public:
	View(string filename);

	void display();

	int getSize();
};


#endif /* VIEW_HPP */

