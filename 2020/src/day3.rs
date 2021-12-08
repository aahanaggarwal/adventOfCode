use std::fs;

fn build_map(lines: &Vec<&str>) -> Vec<Vec<bool>> {
    lines
        .iter()
        .map(|&line| 
            line
            .chars()
            .into_iter()
            .map(|c| c == '#')
            .collect::<Vec<_>>()
        )
        .collect()
}

fn part1(map: &Vec<Vec<bool>>, right: usize, down: usize) -> i32 {
    let mut x: usize = 0;
    let mut y: usize = 0;
    let width = map[0].len();
    let height = map.len();
    let mut trees_hit = 0;

    for _ in map {
        if map[y][x] {
            trees_hit += 1;
        }
        y += down;
        x += right;
        if x >= width {
            x -= width;
        }
        if y >= height {
            break;
        }
    }
    trees_hit
}

fn part2(map: &Vec<Vec<bool>>) -> i128 {
    let slopes: Vec<(usize, usize)> = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];
    let mut trees_hit_mult: i128 = 1;

    for (right, down) in slopes.iter() {
        trees_hit_mult *= part1(map, *right, *down) as i128;
    }
    trees_hit_mult
}

pub fn solve(file_name: &str, part: i32) -> i128 {

    let contents = fs::read_to_string(file_name).expect("File Error");
    let lines = contents
        .split("\n")
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect::<Vec<_>>();

    let map = build_map(&lines);
    println!("{:?}", map);
    
    match part {
        1 => part1(&map, 3, 1).into(),
        2 => part2(&map),
        _ => -1
    }
}