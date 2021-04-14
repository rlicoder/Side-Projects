#include <bits/stdc++.h>
#include "Session.hpp"
#include "Date.hpp"

using namespace std;

int main()
{
    vector<string> classes;
    ifstream in ("classes.txt");

    string str;
    while (in >> str)
    {
        classes.push_back(str);
    }
    for (int i = 0; i < (int)classes.size(); i++)
    {
        cout << i+1 << ": " << classes[i] << endl;
    }
    cin >> choice;
}
