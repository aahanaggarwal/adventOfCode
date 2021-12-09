use std::{collections::HashSet, fs, vec};

fn find_point(mut min: i32, mut max: i32, max_char: char, string: &str) -> i32 {
    let mut index = 0;
    while max > min {
        let mid = min + ((max - min) / 2);
        if string.chars().nth(index).unwrap() == max_char {
            max = mid;
        } else {
            min = mid + 1;
        }
        index += 1;
    }
    max
}

fn part1(tickets: &Vec<&str>) -> i128 {
    let mut ticket_ids: Vec<i128> = vec![];
    for ticket in tickets {
        let row_num = find_point(0, 127, 'F', &ticket[..7]);
        let col_num = find_point(0, 7, 'L', &ticket[7..]);
        let ticket_id = row_num * 8 + col_num;
        ticket_ids.push(ticket_id.into());

        println!("{}", ticket_id);
    }

    *ticket_ids.iter().max().unwrap()
}

fn part2(tickets: &Vec<&str>) -> i128 {
    let mut ticket_ids: HashSet<i128> = HashSet::<_>::new();
    for ticket in tickets {
        let row_num = find_point(0, 127, 'F', &ticket[..7]);
        let col_num = find_point(0, 7, 'L', &ticket[7..]);
        let ticket_id: i128 = (row_num * 8 + col_num).into();

        ticket_ids.insert(ticket_id.into());

        println!("{}", ticket_id);
    }

    for ticket_id in ticket_ids.iter() {
        if ticket_ids.contains(&(ticket_id - 2)) && !ticket_ids.contains(&(ticket_id - 1)) {
            return ticket_id - 1;
        }
        if ticket_ids.contains(&(ticket_id + 2)) && !ticket_ids.contains(&(ticket_id + 1)) {
            return ticket_id + 1;
        }
    }

    -1
}

pub fn solve(file_name: &str, part: i32) -> i128 {
    let contents = fs::read_to_string(file_name).expect("File Error");
    let tickets: Vec<&str> = contents
        .split_whitespace()
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect();

    println!("{:?}", tickets);

    match part {
        1 => part1(&tickets),
        2 => part2(&tickets),
        _ => -1,
    }
}
