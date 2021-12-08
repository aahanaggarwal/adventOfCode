use std::fs;
use std::collections::HashSet;
use std::iter::FromIterator;

fn part1(entries: &Vec<i32>) -> i128 {
    for x in entries.iter() {
        for y in entries.iter() {
            if x+y == 2020 {
                return (x*y).into();
            }
        }
    }
    -1
}

fn part2(entries: &Vec<i32>) -> i128 {
    let entries_set = HashSet::<_>::from_iter(entries);

    for x in entries.iter() {
        for y in entries
            .iter()
            .filter(|&a| a+x < 2020)
            .collect::<Vec<_>>() {
            if entries_set.contains(&(2020-(x+y))) {
                return (x*y*(2020-(x+y))).into()
            }
        }
    }
    -1
}

pub fn solve(file_name: &str, part: i32) -> i128 {

    let contents = fs::read_to_string(file_name).expect("File Error");
    println!("{}", contents);

    let entries: Vec<i32> = contents
        .split_whitespace()
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect();

    match part {
        1 => part1(&entries),
        2 => part2(&entries),
        _ => -1
    }
}