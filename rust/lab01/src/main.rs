use std::io;

// Rock, Paper, Scissors, Lizard, Spock
// This array sets the options that are defeated by each index
static OPTIONS : [&[i8; 2]; 5] = [[2, 3], [0, 4], [1, 3], [4, 1], [2, 0]];

fn beats(x : &i8, y : &i8) -> bool
{
    return (OPTIONS[&x][0] == y) || (OPTIONS[x][1] == y);    
}

fn main() {
    let mut user_input : String = String::new();
    let stdin = io::stdin();
    let mut moves : [i8; 2];

    for i in 0..2
    {
        stdin.read_line(&mut user_input); // Read move
        println!("");
        moves[i] = user_input.parse::<i8>().unwrap(); // Set move to option
    }

    let mut result : String = "\nempate\n".to_string();

    if beats(&moves[0], &moves[1])
    {
        result = "Jornada nas Estrelas".to_string();
    }else if beats(&moves[0], &moves[1])
    {
        result = "Interstelar".to_string();
    }

    println!("{}\n", result);

}
