use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 11 part 1");

    let input = read("src/day11/data.in").expect("no input file found");
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_11_part_1() {
        run();
    }
}
