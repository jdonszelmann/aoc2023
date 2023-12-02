use crate::day02::parse;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    inp.lines()
        .map(parse)
        .map(|(_, i)| i.get("red").unwrap() * i.get("green").unwrap() * i.get("blue").unwrap())
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 2 part 2");

    let input = read_to_string("src/day02/data.in").expect("no input file found");
    println!("{}", answer(&input))
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_2_part_2() {
        assert_eq!(answer(include_str!("data.in")), 62811);
    }

    #[test]
    pub fn test_day_2_part_2_example() {
        assert_eq!(answer(include_str!("test.in")), 2286);
    }
}
