use std::process::exit;

use crate::instrs;

fn get_instruction(num: u16) -> &'static str {
    if num > 21 {
        panic!("Not an instruction: {}", num);
    }
    let str = match num {
        0 => "halt",
        21 => "noop",
        19 => "out",
        6 => "jmp",
        _ => {
            println!("Instrction not implemented: {}", num);
            panic!("Not an instruction!")
        }
    };

    &str
}

fn parse_instruction(program: &Vec<u16>, instr_ptr: usize) -> usize {
    let mut new_instr_ptr = instr_ptr;
    let instr = get_instruction(program[new_instr_ptr]);

    match instr {
        "noop" => {
            // We can just advance to next instr and continue
            new_instr_ptr += 1;
        }
        "out" => {
            // We want to print the next byte
            new_instr_ptr += 1;
            instrs::out(program[new_instr_ptr]);
            new_instr_ptr += 1;
        }
        "halt" => {
            // Exit the program
            exit(0)
        }
        "jmp" => {
            // Get num and set new_instr_ptr to that
            println!("{}", new_instr_ptr);
            new_instr_ptr += 1;
            let new_loc: usize = program[new_instr_ptr] as usize;
            println!("{}", new_loc);
            new_instr_ptr = new_loc;
        }
        _ => {
            println!("Wut");
        }
    }

    new_instr_ptr
}

pub fn run_program(program: &Vec<u16>) {
    let mut instr_ptr = 0;
    loop {
        instr_ptr = parse_instruction(program, instr_ptr);
    }
}
