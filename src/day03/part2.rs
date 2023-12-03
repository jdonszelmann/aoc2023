use crate::day03::find_symbols;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    let symbols = find_symbols(inp);

    symbols
        .iter()
        .filter(|i| i.symbol == '*' && i.numbers.len() == 2)
        .map(|i| i.numbers.iter().map(|n| n.value).product::<u64>())
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 3 part 2");

    let input = read_to_string("src/day03/data.in").expect("no input file found");
    println!("{}", answer(&input));
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_3_part_2() {
        assert_eq!(answer(include_str!("data.in")), 73201705)
    }

    #[test]
    pub fn test_day_3_part_2_example() {
        assert_eq!(answer(include_str!("test.in")), 467835)
    }
}
