use crate::day03::find_symbols;
use itertools::Itertools;
use std::collections::HashSet;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    let symbols = find_symbols(inp);

    symbols
        .iter()
        .flat_map(|i| &i.numbers)
        .map(|i| i.value)
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 3 part 1");

    let input = read_to_string("src/day03/data.in").expect("no input file found");
    println!("{}", answer(&input));
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_3_part_1() {
        assert_eq!(answer(include_str!("data.in")), 527446)
    }

    #[test]
    pub fn test_day_3_part_1_example() {
        assert_eq!(answer(include_str!("test.in")), 4361)
    }
}
