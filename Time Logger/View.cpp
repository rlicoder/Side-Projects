#include "View.hpp"

View::View(string filename)
{
    //constructor with filename variables. reads in all the lines for menu based output
    ifstream in;
    in.open(filename);
    string str;
    while (getline(in, str))
    {
	choices.push_back(str);
    }
}

void View::display()
{
    cout << endl;
    //number is within the class.
    //makes it easier to edit
    for (int i = 0; i < choices.size(); i++)
    {
	cout << i+1 << ": " << choices[i] << endl;
    }
}

int View::getSize()
{
    //for controller class for input validation.
    return (int)this->choices.size();
}