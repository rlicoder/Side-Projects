#include <bits/stdc++.h>

using namespace std;

int main()
{
    string str;
    while (getline(cin,str))
    {
        while (*(str.begin()) != '"' && str.size() != 0)
        {
            str.erase(str.begin());
        }
        while (str.back() != '"' && str.size() != 0)
        {
            str.pop_back();
        }
        if (str.size() > 0)
        {
            str.pop_back();
        }
        if (str.size() > 0)
        {
            str.erase(str.begin());
        }
        if (str.size() < 250)
        {
            cout << str << endl;
        }
    }
}
