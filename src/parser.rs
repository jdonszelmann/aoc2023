use std::str::{Chars, FromStr};
use itertools::{Itertools, MultiPeek};

pub struct Parser<'a> {
    stream: MultiPeek<Chars<'a>>,
}

impl<'a> Parser<'a> {
    pub fn new(i: &'a str) -> Self {
        Self {
            stream: i.chars().multipeek(),
        }
    }

    pub fn is_empty(&mut self) -> bool {
        self.stream.peek().is_none()
    }

    pub fn accept(&mut self, c: char) -> Option<()> {
        if self.stream.peek() == Some(&c) {
            let _ = self.stream.next();
            // println!("accept: {c}");
            Some(())
        } else {
            self.stream.reset_peek();
            None
        }
    }

    pub fn accept_with(&mut self, c: impl Fn(char) -> bool) -> Option<char> {
        if let Some(&i) = self.stream.peek() {
            if c(i) {
                let _ = self.stream.next();
                Some(i)
            } else {
                self.stream.reset_peek();
                None
            }
        } else {
            self.stream.reset_peek();
            None
        }
    }

    pub fn accept_str(&mut self, s: &str) -> Option<()> {
        for i in s.chars() {
            if self.stream.peek() != Some(&i) {
                self.stream.reset_peek();
                return None;
            }
        }

        // println!("accept: {s}");
        for i in s.chars() {
            self.stream.next();
        }

        Some(())
    }

    pub fn whitespace(&mut self) -> bool {
        let mut res = false;

        while self.accept_with(|i| i.is_whitespace()).is_some() {
            res = true;
        }

        res
    }

    pub fn parse_num<T: FromStr>(&mut self) -> Option<T> {
        let mut res = String::new();

        while let Some(i) = self.accept_with(|i| i.is_ascii_digit()) {
            res.push(i)
        }

        if res.is_empty() {
            None
        } else {
            // println!("num: {res}");
            Some(res.parse().ok()?)
        }
    }
}

