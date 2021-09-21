#include "Pokemon.h"

class GameState 
{
    bool weatherActive;
    int weatherEffectLeft;
    int weatherType;
    int turnNumber;
    int numAllyPokemon;
    int numEnemyPokemon;
    Pokemon Ally[6];
    Pokemon Enemey[6];

    bool GameOver() { return numAllyPokemon == 0 || numEnemyPokemon == 0 };
};
