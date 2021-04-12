#include <bits/stdc++.h>

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
    for (int i = 0; i < classes.size(); i++)
    {
        cout << classes[i] << endl;
    }

}
