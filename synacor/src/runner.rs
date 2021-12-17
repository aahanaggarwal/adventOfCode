use std::process::exit;

use crate::{instrs, storage::Storage};

fn get_instruction(num: u16) -> &'static str {
    if num > 21 {
        panic!("Not an instruction: {}", num);
    }
    let str = match num {
        0 => "halt",
        21 => "noop",
        19 => "out",
        6 => "jmp",
        7 => "jt",
        8 => "jf",
        1 => "set",
        _ => {
            println!("Instrction not implemented: {}", num);
            panic!("Not an instruction!")
        }
    };

    &str
}

fn exec_instr(program: &Vec<u16>, state: &mut Storage, instr_ptr: usize) -> usize {
    let instr = get_instruction(program[instr_ptr]);

    match instr {
        "noop" => instr_ptr + 1,
        "out" => instrs::out(instr_ptr, program, state),
        "halt" => {
            exit(0);
        }
        "jmp" => instrs::jmp(instr_ptr, program, state),
        "jt" => instrs::jt(instr_ptr, program, state),
        "jf" => instrs::jf(instr_ptr, program, state),
        "set" => instrs::set(instr_ptr, program, state),
        _ => {
            panic!("Wut");
        }
    }
}

pub fn run_program(program: &Vec<u16>, state: &mut Storage) {
    let mut instr_ptr = 0;
    loop {
        instr_ptr = exec_instr(program, state, instr_ptr);
    }
}
