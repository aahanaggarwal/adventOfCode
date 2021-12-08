pub mod day1;
pub mod day2;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Not enough args");
        return
    }

    let file_ext: &str = if args.len() == 4 {"test"} else {"txt"};
    let answer: i32;
    let day_num: i32 = args[1].parse().unwrap();
    let part: i32 = args[2].parse().unwrap();

    let file_name = format!("inputs/day{}.{}", day_num, file_ext);


    match day_num {
        1 => {
            answer = day1::solve(&file_name, part);
        }
        2 => {
            answer = day2::solve(&file_name, part);
        }
        _ => {
            answer = -1;
            println!("Invalid args!")
        }
    }
    if answer != -1{
        println!("{}", answer);
    }
}