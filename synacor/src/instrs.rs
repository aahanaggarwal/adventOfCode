use crate::utils;

pub fn out(mut instr_ptr: usize, program: &Vec<u16>) -> usize {
    instr_ptr += 1;
    let num = program[instr_ptr];
    let byte_to_print = utils::convert_to_ascii(num);
    print!("{}", byte_to_print);
    instr_ptr + 1
}

pub fn jmp(mut instr_ptr: usize, program: &Vec<u16>) -> usize {
    instr_ptr += 1;
    let a = program[instr_ptr];

    a as usize
}

pub fn jt(mut instr_ptr: usize, program: &Vec<u16>) -> usize {
    instr_ptr += 1;
    let a = program[instr_ptr];
    instr_ptr += 1;
    let b = program[instr_ptr];

    if a != 0 {
        b as usize
    } else {
        instr_ptr + 1
    }
}

pub fn jf(mut instr_ptr: usize, program: &Vec<u16>) -> usize {
    instr_ptr += 1;
    let a = program[instr_ptr];
    instr_ptr += 1;
    let b = program[instr_ptr];

    if a == 0 {
        b as usize
    } else {
        instr_ptr + 1
    }
}
