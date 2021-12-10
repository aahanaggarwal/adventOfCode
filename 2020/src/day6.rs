use std::{clone, collections::HashSet, fs};

fn part1(answers: &Vec<Vec<&str>>) -> i128 {
    let mut count: usize = 0;
    for group in answers.iter() {
        let mut answered_yes: HashSet<char> = HashSet::new();
        for person in group.iter() {
            for question in person.chars() {
                answered_yes.insert(question);
            }
        }
        count += answered_yes.len();
    }
    count as i128
}

fn part2(answers: &Vec<Vec<&str>>) -> i128 {
    let mut count: usize = 0;
    for group in answers.iter() {
        let mut all_answered_yes: HashSet<char> = HashSet::from_iter(group[0].chars());
        if group.len() > 1 {
            for person in group[1..].iter() {
                let curr_set = HashSet::from_iter(person.chars());
                all_answered_yes = all_answered_yes.intersection(&curr_set).cloned().collect();
            }
        }
        count += all_answered_yes.len();
    }
    count as i128
}

pub fn solve(file_name: &str, part: i32) -> i128 {
    let contents = fs::read_to_string(file_name).expect("File Error");
    let answers: Vec<Vec<&str>> = contents
        .split("\n\n")
        .map(|group| {
            group
                .split_whitespace()
                .map(|s| s.trim())
                .filter(|s| !s.is_empty())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<Vec<_>>>();

    println!("{:?}", answers);

    match part {
        1 => part1(&answers),
        2 => part2(&answers),
        _ => -1,
    }
}
