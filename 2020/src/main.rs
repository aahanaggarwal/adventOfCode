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
        1 => day01::solve(&file_name, part),
        2 => day02::solve(&file_name, part),
        3 => day03::solve(&file_name, part),
        4 => day04::solve(&file_name, part),
        5 => day05::solve(&file_name, part),
        6 => day06::solve(&file_name, part),
        7 => day07::solve(&file_name, part),
        _ => {
            println!("Invalid args!");
            -1
        }
    };
    if answer != -1 {
        println!("{}", answer);
    }
}
