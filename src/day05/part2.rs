
use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 5 part 2");

    let input = read("src/day05/data.in").expect("no input file found");
}


#[cfg(test)]
mod tests {
    use super::run;
    
    #[test]
    pub fn test_day_5_part_2() {
        run();
    }
}
                    