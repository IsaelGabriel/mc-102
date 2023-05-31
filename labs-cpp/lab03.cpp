#include <iostream>

using namespace std;

int main()
{
    int player_total;

    cin >> player_total;

    int player_numbers[player_total];
    string line;

    cin >> line;

    for(int i = 0; i < (player_total * 2); i += 2)
    {
        player_numbers[(int) (i / 2)] = line[i];
        cout << line[i];
        cout << player_numbers[(int) (i / 2)];

    }

    return 0;
}
