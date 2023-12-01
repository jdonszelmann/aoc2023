use crate::day01::parse;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    inp.lines().map(|l| parse(l, true) as u64).sum()
}

pub fn run() {
    println!("aoc 2022 day 1 part 2");

    let inp = read_to_string("src/day01/data.in").expect("no input file found");
    println!("{}", answer(&inp))
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_1_part_2() {
        assert_eq!(answer(include_str!("data.in")), 56324);
    }

    #[test]
    pub fn test_day_1_example_2() {
        assert_eq!(answer(include_str!("test2.in")), 281);
    }
}
