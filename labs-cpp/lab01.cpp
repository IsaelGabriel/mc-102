#include <iostream>

using namespace std;

int get_play_index(string input)
{
    if(input == "pedra") return 0;
    if(input == "papel") return 1;
    if(input == "tesoura") return 2;
    if(input == "lagarto") return 3;
    if(input == "spock") return 4;

   return -1; 
}

int get_winner(int play_1, int play_2)
{
    int counters[5][2] = {{2,3},{0,4},{1,3},{4,1},{2,0}};

    if (play_1 == play_2)
    {
        cout << "empate";
        return 0;
    }

    if(play_2 == counters[play_1][0] || play_2 == counters[play_1][1])
    {
        cout << "Jornada nas Estrelas";
        return 0;
    }

    cout << "Interestelar";
    return 0;
}

int game()
{
    string input_1;
    string input_2;

    cin >> input_1;
    cin >> input_2;

    int play_1 = get_play_index(input_1);
    int play_2 = get_play_index(input_2);

    if (play_1 == -1 || play_2 == -1)
    {
        cout << "Jogadas inválidas!!!";
        return -1;
    }

    get_winner(play_1, play_2);

    return 0;
}

int main()
{
    game();

    return 0;
}