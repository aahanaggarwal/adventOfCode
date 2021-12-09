use advent_of_code_2020::*;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Not enough args");
        return;
    }

    let file_ext: &str = if args.len() == 4 { "test" } else { "txt" };
    let answer: i128;
    let day_num: i32 = args[1].parse().unwrap();
    let part: i32 = args[2].parse().unwrap();

    let file_name = format!("inputs/day{}.{}", day_num, file_ext);

    answer = match day_num {
        1 => day1::solve(&file_name, part),
        2 => day2::solve(&file_name, part),
        3 => day3::solve(&file_name, part),
        4 => day4::solve(&file_name, part),
        5 => day5::solve(&file_name, part),
        _ => {
            println!("Invalid args!");
            -1
        }
    };
    if answer != -1 {
        println!("{}", answer);
    }
}
