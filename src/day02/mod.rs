pub mod part1;
pub mod part2;

use itertools::Itertools;
pub use part1::run as run_part1;
pub use part2::run as run_part2;
use std::collections::HashMap;

pub fn parse(inp: &str) -> (u64, HashMap<&str, u64>) {
    let (num, game) = inp.split_once(':').expect("game number");

    let mut max: HashMap<&str, u64> = HashMap::new();
    for (num, colour) in game
        .split([',', ';', ' '])
        .filter(|i| !i.is_empty())
        .tuples()
    {
        let num = num.parse().expect("number");
        let value = max.entry(colour).or_default();
        *value = (*value).max(num)
    }

    (
        num.split_once(' ').unwrap().1.parse().expect("game number"),
        max,
    )
}

pub fn run() {
    run_part1();
    run_part2();
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_2() {
        run();
    }
}
