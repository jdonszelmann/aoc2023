pub mod part1;
pub mod part2;

use crate::fold_mut::FoldMut;
use crate::update_with::UpdateWith;
use itertools::Itertools;
pub use part1::run as run_part1;
pub use part2::run as run_part2;
use std::collections::HashMap;

pub fn parse(inp: &str) -> (u64, HashMap<&str, u64>) {
    let (num, game) = inp.split_once(':').unwrap();

    (
        num.split_once(' ').unwrap().1.parse().unwrap(),
        game.split([',', ';', ' '])
            .tuples()
            .fold_mut(HashMap::new(), |m, (_, v, k)| {
                m.entry(k)
                    .or_insert(0)
                    .update_with_val(v.parse().unwrap(), std::cmp::max);
            }),
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
