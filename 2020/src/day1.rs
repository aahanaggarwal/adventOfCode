use std::fs;

fn part1(entries: &Vec<i32>) -> i32 {
    for x in entries.iter() {
        for y in entries.iter() {
            if x+y == 2020 {
                return x*y
            }
        }
    }
    -1
}

fn part2(_entries: &Vec<i32>) -> i32 {
    -1
}

pub fn solve(file_name: &str, part: i32) -> i32 {

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