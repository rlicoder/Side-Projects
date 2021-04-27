#include "Session.hpp"
#include <bits/stdc++.h>

using namespace std;

Session::Session(string sclass_name, int sstart, int send) : start(sstart), end(send)
{
    class_name = sclass_name;
};