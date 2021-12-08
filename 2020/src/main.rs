pub mod day1;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Not enough args");
        return
    }

    let file_ext: &str = if args.len() == 4 {"test"} else {"txt"};
    let answer: i32;

    match args[1].parse() {
        Ok(1) => {
            let file_name = format!("inputs/day{}.{}", 1, file_ext);

            let part: i32 = args[2].parse().unwrap();
            answer = day1::solve(&file_name, part);
        }
        _ => {
            answer = -1;
            println!("Invalid args!")
        }
    }

    println!("{}", answer);
}