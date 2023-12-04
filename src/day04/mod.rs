pub mod part1;
pub mod part2;

pub use part1::run as run_part1;
pub use part2::run as run_part2;
use std::collections::{HashMap, HashSet};
use std::io::BufRead;
use std::str::FromStr;

struct Game {
    my_numbers: HashSet<u64>,
    winning_numbers: HashSet<u64>,
}

fn parse_numbers(numbers: &str) -> HashSet<u64> {
    numbers
        .trim()
        .split(' ')
        .filter(|i| !i.is_empty())
        .map(FromStr::from_str)
        .collect::<Result<_, _>>()
        .unwrap()
}

fn parse_game(line: &str) -> (u64, Game) {
    let (game_num, numbers) = line.split_once(':').unwrap();
    let game_num = game_num.split_once(' ').unwrap().1.trim().parse().unwrap();

    let (winning_numbers, my_numbers) = numbers.split_once('|').unwrap();

    (
        game_num,
        Game {
            my_numbers: parse_numbers(my_numbers),
            winning_numbers: parse_numbers(winning_numbers),
        },
    )
}

fn parse(inp: &str) -> HashMap<u64, Game> {
    inp.lines().map(parse_game).collect()
}

pub fn run() {
    run_part1();
    run_part2();
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_4() {
        run();
    }
}
