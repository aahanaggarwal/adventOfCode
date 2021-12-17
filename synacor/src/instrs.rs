use std::io::{self, Read};
use std::process::exit;

use crate::{
    storage::{self, Storage},
    utils,
};

pub fn out(mut instr_ptr: usize, program: &Vec<u16>, state: &Storage) -> usize {
    instr_ptr += 1;
    let num = storage::get_value(instr_ptr, &program, &state);
    let byte_to_print = utils::convert_to_ascii(num);
    print!("{}", byte_to_print);
    instr_ptr + 1
}

pub fn jmp(mut instr_ptr: usize, program: &Vec<u16>, state: &Storage) -> usize {
    instr_ptr += 1;
    let a = storage::get_value(instr_ptr, &program, &state);

    a as usize
}

pub fn jt(mut instr_ptr: usize, program: &Vec<u16>, state: &Storage) -> usize {
    instr_ptr += 1;
    let a = storage::get_value(instr_ptr, &program, &state);
    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, &program, &state);

    if a != 0 {
        b as usize
    } else {
        instr_ptr + 1
    }
}

pub fn jf(mut instr_ptr: usize, program: &Vec<u16>, state: &Storage) -> usize {
    instr_ptr += 1;
    let a = storage::get_value(instr_ptr, &program, &state);
    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, &program, &state);

    if a == 0 {
        b as usize
    } else {
        instr_ptr + 1
    }
}

pub fn set(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    state.registers[reg_num] = b;
    instr_ptr + 1
}

pub fn add(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let sum = (b + c) % 32768;
    state.registers[reg_num] = sum;
    instr_ptr + 1
}

pub fn eq(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let val = if b == c { 1 } else { 0 };
    state.registers[reg_num] = val;
    instr_ptr + 1
}

pub fn push(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let a = storage::get_value(instr_ptr, program, state);

    state.stack.push(a);
    instr_ptr + 1
}

pub fn pop(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    let val = state.stack.pop();
    match val {
        Some(x) => state.registers[reg_num] = x,
        None => panic!("Empty stack pop!"),
    }

    instr_ptr + 1
}

pub fn gt(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let val = if b > c { 1 } else { 0 };
    state.registers[reg_num] = val;
    instr_ptr + 1
}

pub fn and(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let sum = b & c;
    state.registers[reg_num] = sum;
    instr_ptr + 1
}

pub fn or(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let sum = b | c;
    state.registers[reg_num] = sum;
    instr_ptr + 1
}

pub fn not(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    let fifteen_bit_inv = (!(b << 1)) >> 1;

    state.registers[reg_num] = fifteen_bit_inv;
    instr_ptr + 1
}

pub fn call(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let a = storage::get_value(instr_ptr, program, state);

    state.stack.push((instr_ptr + 1) as u16);
    a as usize
}

pub fn mult(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let mut prod = 0;
    // lets hope rustc is good :)
    for _ in 0..c {
        prod = (prod + b) % 32768;
    }
    state.registers[reg_num] = prod;
    instr_ptr + 1
}

pub fn mod_(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    instr_ptr += 1;
    let c = storage::get_value(instr_ptr, program, state);

    let mod_ = b % c;
    state.registers[reg_num] = mod_;
    instr_ptr + 1
}

pub fn rmem(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    instr_ptr += 1;
    let address = storage::get_value(instr_ptr, program, state);

    if (address as usize) < program.len() {
        state.registers[reg_num] = program[address as usize];
    } else {
        state.registers[reg_num] = state.memory[&address];
    }

    instr_ptr + 1
}

pub fn wmem(mut instr_ptr: usize, program: &mut Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let address = storage::get_value(instr_ptr, program, state) as usize;

    instr_ptr += 1;
    let b = storage::get_value(instr_ptr, program, state);

    if address < program.len() {
        program[address] = b;
    } else {
        state.memory.insert(address as u16, b);
    }

    instr_ptr + 1
}

pub fn ret(mut _instr_ptr: usize, _program: &Vec<u16>, state: &mut Storage) -> usize {
    let address = state.stack.pop();
    match address {
        Some(a) => a as usize,
        _ => exit(0),
    }
}

pub fn in_(mut instr_ptr: usize, program: &Vec<u16>, state: &mut Storage) -> usize {
    instr_ptr += 1;
    let reg_num = utils::get_reg_num(program[instr_ptr]);

    let mut buffer = [0; 1];
    let _ = io::stdin().read(&mut buffer);
    let val = buffer[0] as u16;
    state.registers[reg_num] = val;

    instr_ptr + 1
}
