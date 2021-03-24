#include <bits/stdc++.h>

using namespace std;

class Person
{
    int student_id;
    string email;
    string name;
    vector<Session> times;
};

class Session
{
    string class_id;
    int start_time;
    int end_time;
};

int main()
{
    int login_id;
    cout << "Enter your student id: ";
    cin >> login_id;

    menu();

}

void menu()
{
    cout << "What would you like to do? " << endl;

    cin >> ;
}
