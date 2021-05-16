#include "Date.hpp"
#include <bits/stdc++.h>

using namespace std;

Date::Date(int secs)
{
    //set the unit time
    this->unixtime = secs;
    //days per month
    vector<int> days_in_month {31,28,31,30,31,30,31,31,30,31,30,31};
    //start year of unix time
    this->year = 1970;
    //subtracting seconds per year respective to leap year
    while (secs - (this->isLeap() ? 366 : 365) * 24 * 60 * 60 > 0)
    {
	secs -= (this->isLeap() ? 366 : 365) * 24 * 60 * 60;
	this->year++;
    }

    //add day to february if leap year
    if (this->isLeap())
    {
	days_in_month[1]++;
    }

    //subtracting seconds per month
    this->month = 0;
    while (secs - days_in_month[this->month]*60*60*24 > 0)
    {
	secs -= days_in_month[this->month]*60*60*24;
	this->month++;
    }

    //subtracting seconds per day
    this->day = 0;
    for (int i = 0; i < days_in_month[this->month] && secs - 60*60*24 > 0; i++)
    {
	this->day++;
	secs -= 60*60*24;
    }

    //subtracting seconds per hour
    this->hour = 0;
    while (secs - 60*60 > 0)
    {
	this->hour++;
	secs -= 60*60;
    }
    //adding to adjust to timezone and daylight savings
    this->hour += 17;
    if (this->hour > 23)
    {
	hour -= 24;
	this->day++;
    }
    
    //per minute
    this->minute = 0;
    while (secs - 60 >= 0)
    {
	secs -= 60;
	this->minute++;
    }
    //remainder is seconds;
    this->seconds = secs;
};

bool Date::isLeap()
{
    return isLeap(this->year);
};

bool Date::isLeap(int year)
{
    //basic leap year validator
    if (year % 4 == 0)
    {
	if (year % 100 == 0 && year % 400 == 0)
	{
	    return true;
	}
	else if (year % 400 != 0 && year % 100 == 0)
	{
	    return false;
	}
	else
	{
	    return true;
	}
    }
    return false;
};

void Date::output()
{
    //output format that nice for the eyes
    cout << this->month+1 << "/" << this->day << "/" << this->year << endl;
    cout << this->hour << ":";
    cout << (this->minute < 10 ? "0" : "") << this->minute << ":";
    cout << (this->seconds < 10 ? "0" : "") << this->seconds << endl;
};