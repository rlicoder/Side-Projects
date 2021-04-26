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
	int seconds;
    public:
	Date(int);
	
        int getMonth() { return month; };
        int getDay() { return day; };
        int getYear() { return year; };
        int getHour() { return hour; };
        int getMinute() { return minute; };
	int getSeconds() { return seconds; };

        void setMonth(int smonth) { this->month = smonth; };
        void setDay(int sday) { this->day = sday; };
        void setYear(int syear) { this->year = syear; };
        void setHour(int shour) { this->hour = shour; };
        void setMinute(int sminute) { this->minute = sminute; };
	void setSeconds(int sseconds) { this->seconds = sseconds; };

	bool isLeap();
	bool isLeap(int year);

	void output();

};

#endif
