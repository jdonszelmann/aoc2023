pub mod part1;
pub mod part2;

use crate::fold_mut::FoldMut;
use itertools::Itertools;
pub use part1::run as run_part1;
pub use part2::run as run_part2;
use std::collections::{HashMap, HashSet};
use std::iter;

#[derive(Debug)]
struct Number {
    value: u64,
    coordinates: Vec<(usize, usize)>,
}

#[derive(Debug)]
struct Symbol {
    numbers: Vec<Number>,
    symbol: char,
    coordinate: (usize, usize),
}

fn find_symbols(inp: &str) -> Vec<Symbol> {
    let data = inp
        .lines()
        .enumerate()
        .flat_map(|(y, line)| {
            line.chars()
                .enumerate()
                .map(move |(x, c)| ((x, y), c))
                .chain(iter::once(((1000, 1000), '\n')))
        })
        .collect_vec();

    let symbols: HashMap<_, _> = data
        .iter()
        .filter(|(_, c)| !c.is_ascii_digit() && *c != '.')
        .copied()
        .collect();

    let symbol_neighbours: HashMap<_, _> = symbols
        .keys()
        .flat_map(|&(x, y)| {
            [
                ((x - 1, y), (x, y)),
                ((x - 1, y - 1), (x, y)),
                ((x, y - 1), (x, y)),
                ((x + 1, y - 1), (x, y)),
                ((x + 1, y), (x, y)),
                ((x + 1, y + 1), (x, y)),
                ((x, y + 1), (x, y)),
                ((x - 1, y + 1), (x, y)),
            ]
        })
        .collect();

    let (numbers, _) = data.iter().fold_mut(
        (HashMap::<(usize, usize), Vec<_>>::new(), None),
        |(acc, number), &((x, y), c)| {
            if c.is_ascii_digit() {
                if let Some(n) = *number {
                    acc.get_mut(&n).unwrap().push((c, (x, y)));
                } else {
                    acc.insert((x, y), vec![(c, (x, y))]);
                    *number = Some((x, y))
                }
            } else {
                *number = None;
            }
        },
    );

    let part_numbers = numbers
        .iter()
        .map(|(k, v)| Number {
            value: v.iter().map(|i| i.0).collect::<String>().parse().unwrap(),
            coordinates: v.iter().map(|i| i.1).collect(),
        })
        .filter_map(|i| {
            Some((
                i.coordinates
                    .iter()
                    .filter_map(|c| symbol_neighbours.get(c))
                    .next()?,
                i,
            ))
        })
        .fold_mut(HashMap::new(), |acc, (sym, num)| {
            acc.entry(*sym)
                .or_insert_with(|| Symbol {
                    numbers: vec![],
                    symbol: *symbols.get(sym).unwrap(),
                    coordinate: *sym,
                })
                .numbers
                .push(num)
        })
        .into_values()
        .collect_vec();

    part_numbers
}

pub fn run() {
    run_part1();
    run_part2();
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_3() {
        run();
    }
}
