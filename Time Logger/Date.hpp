#ifndef DATE_HPP
#define DATE_HPP

class Date
{
    private:
        int month;
        int day;
        int year;

        int hour;
        int minute;
    public:
        int getMonth() { return month; };
        int getDay() { return day; };
        int getYear() { return year; };
        int getHour() { return hour; };
        int getMinute() { return minute; };

        void setMonth(int smonth) { this->month = smonth; };
        void setDay(int sday) { this->day = sday; };
        void setYear(int syear) { this->year = syear; };
        void setHour(int shour) { this->hour = shour; };
        void setMinute(int sminute) { this->minute = sminute; };

};
