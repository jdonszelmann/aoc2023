pub mod part1;
pub mod part2;

use itertools::Itertools;
pub use part1::run as run_part1;
pub use part2::run as run_part2;
use std::iter;

#[derive(Copy, Clone, Debug, PartialEq)]
#[allow(clippy::upper_case_acronyms)]
enum Machine {
    START,

    O,
    ON,
    T,
    TW,
    TH,
    THR,
    THRE,
    F,
    FO,
    FOU,
    FI,
    FIV,
    S,
    SI,
    SE,
    SEV,
    SEVE,
    E,
    EI,
    EIG,
    EIGH,
    N,
    NI,
    NIN,

    EN,
    OW,
    EE,
    EER,
    EERH,
    R,
    RU,
    RUO,
    EV,
    EVI,
    X,
    XI,
    NE,
    NEV,
    NEVE,
    THG,
    THGI,
    ENI,

    REJECT,
    ACCEPT(u8),
}

impl Machine {
    pub fn step(self, c: char, words: bool) -> Self {
        match c {
            '0' if self == Machine::START => Self::ACCEPT(0),
            '1' if self == Machine::START => Self::ACCEPT(1),
            '2' if self == Machine::START => Self::ACCEPT(2),
            '3' if self == Machine::START => Self::ACCEPT(3),
            '4' if self == Machine::START => Self::ACCEPT(4),
            '5' if self == Machine::START => Self::ACCEPT(5),
            '6' if self == Machine::START => Self::ACCEPT(6),
            '7' if self == Machine::START => Self::ACCEPT(7),
            '8' if self == Machine::START => Self::ACCEPT(8),
            '9' if self == Machine::START => Self::ACCEPT(9),

            _ if !words => Self::REJECT,

            'o' if self == Machine::START => Self::O,
            't' if self == Machine::START => Self::T,
            'f' if self == Machine::START => Self::F,
            'r' if self == Machine::START => Self::R,
            's' if self == Machine::START => Self::S,
            'x' if self == Machine::START => Self::X,
            'e' if self == Machine::START => Self::E,
            'n' if self == Machine::START => Self::N,

            'n' if self == Self::O => Self::ON,
            'n' if self == Self::E => Self::EN,
            'w' if self == Self::T => Self::TW,
            'w' if self == Self::O => Self::OW,
            'h' if self == Self::T => Self::TH,
            'e' if self == Self::E => Self::EE,
            'o' if self == Self::F => Self::FO,
            'u' if self == Self::R => Self::RU,
            'i' if self == Self::F => Self::FI,
            'v' if self == Self::E => Self::EV,
            'i' if self == Self::S => Self::SI,
            'i' if self == Self::X => Self::XI,
            'e' if self == Self::S => Self::SE,
            'e' if self == Self::N => Self::NE,
            'i' if self == Self::E => Self::EI,
            'h' if self == Self::T => Self::TH,
            'i' if self == Self::N => Self::NI,

            'e' if self == Self::ON => Self::ACCEPT(1),
            'o' if self == Self::EN => Self::ACCEPT(1),
            'o' if self == Self::TW => Self::ACCEPT(2),
            't' if self == Self::OW => Self::ACCEPT(2),
            'r' if self == Self::TH => Self::THR,
            'r' if self == Self::EE => Self::EER,
            'u' if self == Self::FO => Self::FOU,
            'o' if self == Self::RU => Self::RUO,
            'v' if self == Self::FI => Self::FIV,
            'i' if self == Self::EV => Self::EVI,
            'x' if self == Self::SI => Self::ACCEPT(6),
            's' if self == Self::XI => Self::ACCEPT(6),
            'v' if self == Self::SE => Self::SEV,
            'v' if self == Self::NE => Self::NEV,
            'g' if self == Self::EI => Self::EIG,
            'g' if self == Self::TH => Self::THG,
            'n' if self == Self::NI => Self::NIN,
            'i' if self == Self::EN => Self::ENI,

            'e' if self == Self::THR => Self::THRE,
            'h' if self == Self::EER => Self::EERH,
            'r' if self == Self::FOU => Self::ACCEPT(4),
            'f' if self == Self::RUO => Self::ACCEPT(4),
            'e' if self == Self::FIV => Self::ACCEPT(5),
            'f' if self == Self::EVI => Self::ACCEPT(5),
            'e' if self == Self::SEV => Self::SEVE,
            'e' if self == Self::NEV => Self::NEVE,
            'h' if self == Self::EIG => Self::EIGH,
            'i' if self == Self::THG => Self::THGI,
            'e' if self == Self::NIN => Self::ACCEPT(9),
            'n' if self == Self::ENI => Self::ACCEPT(9),

            'e' if self == Self::THRE => Self::ACCEPT(3),
            't' if self == Self::EERH => Self::ACCEPT(3),
            'n' if self == Self::SEVE => Self::ACCEPT(7),
            's' if self == Self::NEVE => Self::ACCEPT(7),
            't' if self == Self::EIGH => Self::ACCEPT(8),
            'e' if self == Self::THGI => Self::ACCEPT(8),

            _ => Self::REJECT,
        }
    }

    fn accept(self) -> Option<u8> {
        if let Self::ACCEPT(v) = self {
            Some(v)
        } else {
            None
        }
    }

    fn not_reject(&self) -> bool {
        !matches!(self, Self::REJECT)
    }
}

fn find_number(
    inp: &mut impl Iterator<Item = char>,
    mut machines: Vec<Machine>,
    words: bool,
) -> u8 {
    for m in &machines {
        if let Some(i) = m.accept() {
            return i;
        }
    }

    machines.push(Machine::START);
    let c = inp.next().expect("number in string");

    for m in &mut machines {
        *m = m.step(c, words)
    }

    machines.retain(|i| i.not_reject());

    find_number(inp, machines, words)
}

pub fn parse(inp: &str, words: bool) -> u8 {
    let fst = find_number(&mut inp.chars(), vec![], words);
    let lst = find_number(&mut inp.chars().rev(), vec![], words);
    fst * 10 + lst
}

pub fn run() {
    run_part1();
    run_part2();
}

#[cfg(test)]
mod tests {
    use super::run;

    #[test]
    pub fn test_day_1() {
        run();
    }
}
