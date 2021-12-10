use std::{
    collections::{HashMap, HashSet},
    fmt::Debug,
    fs,
};

struct InnerBag {
    number: i128,
    bag: String,
}

impl Debug for InnerBag {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("InnerBag")
            .field("number", &self.number)
            .field("bag", &self.bag)
            .finish()
    }
}

fn get_bag_contents(rule: &str) -> Vec<InnerBag> {
    rule.split(",")
        .map(|mut per_bag_rule| {
            per_bag_rule = per_bag_rule.trim();
            let num = per_bag_rule
                .split_whitespace()
                .collect::<Vec<&str>>()
                .first()
                .unwrap()
                .parse::<i32>()
                .unwrap_or(0);

            InnerBag {
                number: num as i128,
                bag: String::from(
                    per_bag_rule.split_whitespace().collect::<Vec<&str>>()[1..3].join(" "),
                ),
            }
        })
        .collect::<Vec<_>>()
}

fn part1(bag_to_contents: &HashMap<String, Vec<InnerBag>>) -> i128 {
    let init_bag = String::from("shiny gold");
    let mut can_contain: HashSet<&String> = HashSet::from_iter(vec![&init_bag]);
    let mut changed: bool = true;

    while changed {
        changed = false;
        for bag in bag_to_contents.keys() {
            for inner_bag in &bag_to_contents[bag] {
                if can_contain.contains(&inner_bag.bag) && !can_contain.contains(&bag) {
                    can_contain.insert(&bag);
                    changed = true;
                }
            }
        }
    }

    (can_contain.len() - 1) as i128
}

fn find_number_in_bag(
    bag_to_contents: &HashMap<String, Vec<InnerBag>>,
    bag_name: &String,
    known_values: &mut HashMap<String, i128>,
) -> i128 {
    if known_values.contains_key(bag_name) {
        return known_values[bag_name];
    }

    let mut count = 1;

    for inner_bag in &bag_to_contents[bag_name] {
        count += (inner_bag.number
            * find_number_in_bag(bag_to_contents, &inner_bag.bag, known_values))
            as i128
    }
    known_values.insert(bag_name.to_string(), count);
    count
}

fn part2(bag_to_contents: &HashMap<String, Vec<InnerBag>>) -> i128 {
    let known_values: &mut HashMap<String, i128> = &mut HashMap::new();
    known_values.insert(String::from("other bags."), 0);

    find_number_in_bag(bag_to_contents, &String::from("shiny gold"), known_values) - 1
}

pub fn solve(file_name: &str, part: i32) -> i128 {
    let contents = fs::read_to_string(file_name).expect("File Error");
    let lines: Vec<&str> = contents
        .split("\n")
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect();

    let bag_to_contents: HashMap<String, Vec<InnerBag>> =
        HashMap::from_iter(lines.iter().map(|&s| {
            let bag_rule_vec: Vec<&str> = s.split("bags contain").map(|x| x.trim()).collect();
            (
                String::from(*bag_rule_vec.first().unwrap()),
                get_bag_contents(&bag_rule_vec[1..].join("")),
            )
        }));

    println!("{:?}", bag_to_contents);

    match part {
        1 => part1(&bag_to_contents),
        2 => part2(&bag_to_contents),
        _ => -1,
    }
}
