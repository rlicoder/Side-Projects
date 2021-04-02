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
    //get login information
    string login_id;
    string last_name;
    string dob;
    cout << "Enter your student id: ";
    cin >> login_id;
    cout << "Enter your last name: ";
    cin >> last_name;
    cout << "Enter your DOB: MMDDYYYY";
    cin >> dob;

    //hash the login information
    string str = login_id + last_name + dob;
    str = hash(str);



    menu();

}

void menu()
{
    cout << "What would you like to do? " << endl;

    cin >> ;
}
