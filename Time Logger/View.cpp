#include "View.hpp"

View::View(string filename)
{
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
    for (int i = 0; i < choices.size(); i++)
    {
	cout << i+1 << ": " << choices[i] << endl;
    }
}

int View::getSize()
{
    return (int)this->choices.size();
}