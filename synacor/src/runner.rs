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
        9 => "add",
        4 => "eq",
        2 => "push",
        3 => "pop",
        5 => "gt",
        12 => "and",
        13 => "or",
        14 => "not",
        17 => "call",
        10 => "mult",
        11 => "mod",
        15 => "rmem",
        16 => "wmem",
        18 => "ret",
        20 => "in",
        _ => {
            println!("Instrction not implemented: {}", num);
            panic!("Not an instruction!")
        }
    };

    &str
}

fn exec_instr(program: &mut Vec<u16>, state: &mut Storage, instr_ptr: usize) -> usize {
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
        "add" => instrs::add(instr_ptr, program, state),
        "eq" => instrs::eq(instr_ptr, program, state),
        "push" => instrs::push(instr_ptr, program, state),
        "pop" => instrs::pop(instr_ptr, program, state),
        "gt" => instrs::gt(instr_ptr, program, state),
        "and" => instrs::and(instr_ptr, program, state),
        "or" => instrs::or(instr_ptr, program, state),
        "not" => instrs::not(instr_ptr, program, state),
        "call" => instrs::call(instr_ptr, program, state),
        "mult" => instrs::mult(instr_ptr, program, state),
        "mod" => instrs::mod_(instr_ptr, program, state),
        "rmem" => instrs::rmem(instr_ptr, program, state),
        "wmem" => instrs::wmem(instr_ptr, program, state),
        "ret" => instrs::ret(instr_ptr, program, state),
        "in" => instrs::in_(instr_ptr, program, state),
        _ => {
            panic!("Wut");
        }
    }
}

pub fn run_program(program: &mut Vec<u16>, state: &mut Storage) {
    let mut instr_ptr = 0;
    loop {
        instr_ptr = exec_instr(program, state, instr_ptr);
    }
}
