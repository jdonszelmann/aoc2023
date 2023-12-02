use crate::day02::parse;
use std::fs::read_to_string;

fn answer(inp: &str) -> u64 {
    inp.lines()
        .map(parse)
        .filter(|(_, i)| {
            i.get("red").copied().unwrap_or_default() <= 12
                && i.get("green").copied().unwrap_or_default() <= 13
                && i.get("blue").copied().unwrap_or_default() <= 14
        })
        .map(|(num, _)| num)
        .sum()
}

pub fn run() {
    println!("aoc 2022 day 2 part 1");

    let input = read_to_string("src/day02/data.in").expect("no input file found");
    println!("{}", answer(&input))
}

#[cfg(test)]
mod tests {
    use super::{answer, run};

    #[test]
    pub fn test_day_2_part_1() {
        assert_eq!(answer(include_str!("data.in")), 2551);
    }

    #[test]
    pub fn test_day_2_part_1_example() {
        assert_eq!(answer(include_str!("test.in")), 8);
    }
}
