use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 10 part 2");

    let input = read("src/day10/data.in").expect("no input file found");
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_10_part_2() {
        run();
    }
}
