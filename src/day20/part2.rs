use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 20 part 2");

    let input = read("src/day20/data.in").expect("no input file found");
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_20_part_2() {
        run();
    }
}
