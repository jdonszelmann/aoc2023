use crate::day04::parse;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    parse(inp)
        .values()
        .map(|x| x.winning_numbers.intersection(&x.my_numbers).count())
        .map(|i| if i == 0 { 0 } else { 1 << (i - 1) })
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 4 part 1");

    let input = read_to_string("src/day04/data.in").expect("no input file found");
    println!("{}", answer(&input));
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_4_part_1() {
        assert_eq!(answer(include_str!("data.in")), 26426)
    }

    #[test]
    pub fn test_day_4_part_1_example() {
        assert_eq!(answer(include_str!("test.in")), 13)
    }
}
