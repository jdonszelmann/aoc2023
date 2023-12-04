use crate::day04::{parse, Game};
use std::collections::HashMap;
use std::fs::read_to_string;

fn answer_rec(game_num: u64, games: &HashMap<u64, Game>, outcomes: &mut HashMap<u64, u64>) -> u64 {
    if let Some(&i) = outcomes.get(&game_num) {
        return i;
    }

    let game = games.get(&game_num).unwrap();
    let start = game_num + 1;
    let end = game_num + game.my_numbers.intersection(&game.winning_numbers).count() as u64;
    let outcome = (start..=end)
        .map(|i| answer_rec(i, games, outcomes))
        .sum::<u64>()
        + 1;

    outcomes.insert(game_num, outcome);
    outcome
}

fn answer(inp: &str) -> u64 {
    let games = parse(inp);
    let mut outcomes = HashMap::new();
    games
        .keys()
        .map(|&i| answer_rec(i, &games, &mut outcomes))
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 4 part 2");

    let input = read_to_string("src/day04/data.in").expect("no input file found");
    println!("{}", answer(&input))
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_4_part_2() {
        assert_eq!(answer(include_str!("data.in")), 6227972);
    }

    #[test]
    pub fn test_day_4_part_2_example() {
        assert_eq!(answer(include_str!("test.in")), 30);
    }
}
