use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 21 part 1");

    let input = read("src/day21/data.in").expect("no input file found");
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_21_part_1() {
        run();
    }
}
