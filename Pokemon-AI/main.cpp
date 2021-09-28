#include <bits/stdc++.h>

using namespace std;
int calculateDamage()
{
    //https://bulbapedia.bulbagarden.net/wiki/Damage
    float a = 2.f * level / 5 + 2;
    float b = a * power * attack / defense / 50;
    return b * weather * stab * type * conditions;
};

int main()
{
    //initialize game.
    Gamestate Game;

    //initialize pokemon ~12
    //start reading in moves

    //minimax();


}
