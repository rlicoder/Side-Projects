#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    string str;

    for (int i = 0; i < n; i++)
    {
        cin >> str;
        for (int i = 1; i < str.size(); i++)
        {
            str[i] = tolower(str[i]);
        }
        cout << str << endl;
        cin >> str >> str >> str >> str;
    }
}
