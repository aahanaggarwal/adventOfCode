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
