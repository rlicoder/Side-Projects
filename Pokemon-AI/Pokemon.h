class Pokemon
{
    string name;
    //ability
    //item
    
    //HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10 
    //https://pokemon.fandom.com/wiki/HP
    int health;

    int attack;
    int defense;
    int spatk;
    int spdef;
    int speed;
    int type[2];

    bool fainted;
    bool active;

    Move moves[4];
};
