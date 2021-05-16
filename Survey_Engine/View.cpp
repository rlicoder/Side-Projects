#include "View.hpp"

View::View(string filename)
{
    //read in the valid choices from a file that was passed from the constructor
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
    //output the choices. the number is handled by the system and not the file
    for (int i = 0; i < choices.size(); i++)
    {
	cout << i+1 << ": " << choices[i] << endl;
    }
}

int View::getSize()
{
    //get for the controller for validation of the input
    return (int)this->choices.size();
}