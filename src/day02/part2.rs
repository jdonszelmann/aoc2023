
use std::fs::read;

pub fn run() {
    println!("aoc 2022 day 2 part 2");

    let input = read("src/day02/data.in").expect("no input file found");
}


#[cfg(test)]
mod tests {
    use super::run;
    
    #[test]
    pub fn test_day_2_part_2() {
        run();
    }
}
                    