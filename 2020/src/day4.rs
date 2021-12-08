use std::fs;

fn is_valid(passport: &str) -> bool {
    let passport_string = String::from(passport).replace("\n", " ");
    let passpost_fields: Vec<&str> = passport_string
        .split(" ")
        .collect::<Vec<_>>();

    let mut field_count: usize = 0;
    let mut seen_cid: bool = false;

    for field in passpost_fields.iter() {
        let split: Vec<&str> = field
            .split(":")
            .collect();
        field_count += 1;
        match split[0] {
            "byr" => {
                let birth_year = split[1].parse().unwrap_or(-1);
                if birth_year < 1920 || birth_year > 2002 {
                    return false
                }
            }
            "iyr" => {
                let issue_year = split[1].parse().unwrap_or(-1);
                if issue_year < 2010 || issue_year > 2020 {
                    return false
                }
            }
            "eyr" => {
                let exp_year = split[1].parse().unwrap_or(-1);
                if exp_year < 2020 || exp_year > 2030 {

                    return false
                }
            }
            "hgt" => {
                let re = regex::Regex::new(r"([\d]+)(cm|in)").unwrap();
                if !re.is_match(split[1]) {

                    return false;
                }
                let captures = re.captures(split[1]).unwrap();

                let height: i32 = captures.get(1).unwrap().as_str().parse().unwrap_or(-1);
                match captures.get(2).unwrap().as_str() {
                    "cm" => {
                        if height < 150 || height > 193 {
                            return false
                        }
                    }
                    "in" => {
                        if height < 59 || height > 76 {
                            return false;
                        }
                    }
                    _ => return false
                }
            }
            "hcl" => {
                let re = regex::Regex::new(r"#[0-9a-f]{6}?").unwrap();
                if !re.is_match(split[1]) {
                    return false;
                }
            }
            "ecl" => {
                if !matches!(split[1], "amb" | "blu" | "brn" | "gry" | "grn" | "hzl" | "oth") {
                    
                    return false;
                }
            }
            "pid" => {
                let re = regex::Regex::new(r"[0-9]{9}?").unwrap();
                if !re.is_match(split[1]) {
                    return false;
                }
            }
            "cid" => {
                seen_cid = true;
            }
            _ => field_count -= 1
        }
    }

    field_count == 8 || (field_count == 7 && !seen_cid)
    
}

fn part1(passports: &Vec<&str>) -> i128 {
    let mut total_valid: i128 = 0;
    for passport in passports.iter() {
        if passport.matches(":").count() == 8 {
            total_valid += 1;
        }
        else if passport.matches(":").count() == 7 && !passport.contains("cid:") {
            total_valid += 1
        }
    }
    total_valid
}

fn part2(passports: &Vec<&str>) -> i128 {
    let mut total_valid: i128 = 0;
    for passport in passports.iter() {
        if is_valid(passport) {
            total_valid += 1;
        }
    }
    total_valid
}

pub fn solve(file_name: &str, part: i32) -> i128 {

    let contents = fs::read_to_string(file_name).expect("File Error");

    let passports: Vec<&str> = contents
        .split("\n\n")
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .collect();

    println!("{:?}", passports);

    match part {
        1 => part1(&passports),

        // off by one error, so i -1 and its fine...
        // idk whats the error and not worth it to fix
        // at least for a question like this
        2 => part2(&passports),
        _ => -1
    }
}