#include <bits/stdc++.h>

using namespace std;

double dist(pair<double, double> x, pair<double,double> y)
{
    double a = y.first - x.first;
    double b = y.second - x.second;
    return sqrt(a*a+b*b);
}

int main()
{
    //only works for transformations such that it is a dilation followed by a translation
    //put inside the test.in file as follows:
    //the number of points in the set
    //the original points
    //the new points you want
    //ex:
    //2
    //(1,3)
    //(1,4)
    //(4,3)
    //(4,5)
    vector<pair<double, double>> org;
    string str;
    int n;
    cin >> n;
    for (int j = 0; j < n; j++)
    {
        cin >> str;
        str.erase(str.begin());
        str.pop_back();
        for (int i = 0; i < str.size(); i++)
        {
            if (str[i] == ',')
            {
                str[i] = ' ';
                break;
            }
        }
        stringstream s(str);
        string a;
        string b;
        while (s >> a >> b)
        {
            double x = stod(a);
            double y = stod(b);
            org.push_back({x,y});
        }
    }
    double avg_o = 0;
    for (int i = 1; i < org.size(); i++)
    {
        avg_o += dist(org[i], org[i-1]);
    }
    avg_o /= org.size()-1;

    vector<pair<double, double>> neww;
    for (int j = 0; j < n; j++)
    {
        cin >> str;
        str.erase(str.begin());
        str.pop_back();
        for (int i = 0; i < str.size(); i++)
        {
            if (str[i] == ',')
            {
                str[i] = ' ';
                break;
            }
        }
        stringstream s(str);
        string a;
        string b;
        while (s >> a >> b)
        {
            double x = stod(a);
            double y = stod(b);
            neww.push_back({x,y});
        }
    }
    double avg_n = 0;
    for (int i = 1; i < neww.size(); i++)
    {
        avg_n += dist(neww[i], neww[i-1]);
    }
    avg_n /= neww.size()-1;
    
    double ratio = avg_n / avg_o;
    for (int i = 0; i < org.size(); i++)
    {
        org[i].first *= ratio;
        org[i].second *= ratio;
    }

    double avg_x, avg_y;
    avg_x = avg_y = 0;
    assert(org.size() > 0);
    assert(neww.size() > 0);
    assert(org.size() == neww.size());
    for (int i = 0; i < org.size(); i++)
    {
        avg_x += neww[i].first - org[i].first;
        avg_y += neww[i].second - org[i].second;
    }
    avg_x /= org.size();
    avg_y /= org.size();
    cout << "Res:" << endl;
    for (int i = 0; i < org.size(); i++)
    {
        cout << org[i].first + avg_x << " " << org[i].second + avg_y << endl;
    }
    cout << endl << "Compared to the answers: " << endl;
    for (int i = 0; i < neww.size(); i++)
    {
        cout << neww[i].first << " " << neww[i].second << endl;
    }
    cout << "dilation ratio: " << ratio << endl;
    cout << "x translation: " << avg_x << endl;
    cout << "y translation: " << avg_y << endl;
}
