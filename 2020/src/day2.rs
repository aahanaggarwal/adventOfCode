use std::fs;
use std::str::FromStr;

struct Password {
    lower_limit: usize,
    upper_limit: usize,
    character: char,
    password_str: String,
}

impl FromStr for Password {
    type Err = std::string::ParseError;

    fn from_str(line: &str) -> Result<Self, Self::Err> {
        let contents: Vec<&str> = line.split_ascii_whitespace().collect();
        let limits_str = contents[0];
        let character = contents[1].chars().nth(0).unwrap();

        let range: Vec<usize> = limits_str
            .split("-")
            .map(|s| s.trim())
            .filter(|s| !s.is_empty())
            .map(|s| s.parse::<usize>().unwrap())
            .collect::<Vec<usize>>();

        Ok(Password {
            lower_limit: range[0],
            upper_limit: range[1],
            character: character,
            password_str: String::from(contents[2]),
        })
    }
}

fn part1(password_entries: &Vec<Password>) -> i32 {
    let mut count: i32 = 0;
    for entry in password_entries.iter() {
        let num_occs = &entry.password_str.matches(entry.character).count();
        if num_occs >= &entry.lower_limit && num_occs <= &entry.upper_limit {
            count += 1;
        }
    }
    count
}

fn part2(password_entries: &Vec<Password>) -> i32 {
    let mut count: i32 = 0;
    for entry in password_entries.iter() {
        if &entry.password_str.len() < &entry.upper_limit {
            continue;
        }

        let matches_first = &entry
            .password_str
            .chars()
            .nth(entry.lower_limit - 1)
            .unwrap()
            == &entry.character;
        let matches_second = &entry
            .password_str
            .chars()
            .nth(entry.upper_limit - 1)
            .unwrap()
            == &entry.character;

        if matches_first ^ matches_second {
            count += 1;
        }
    }
    count
}

pub fn solve(file_name: &str, part: i32) -> i128 {
    let contents = fs::read_to_string(file_name).expect("File Error");
    println!("{}", contents);

    let password_entries: Vec<Password> = contents
        .split("\n")
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|s| Password::from_str(s).unwrap())
        .collect();

    match part {
        1 => part1(&password_entries).into(),
        2 => part2(&password_entries).into(),
        _ => -1,
    }
}
