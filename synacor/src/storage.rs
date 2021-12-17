use std::collections::HashMap;

use crate::utils;
pub struct Storage {
    pub memory: HashMap<u16, u16>,
    pub registers: Vec<u16>,
    pub stack: Vec<u16>,
}

impl Storage {
    pub fn new() -> Storage {
        let mut registers: Vec<u16> = vec![0, 0, 0, 0, 0, 0, 0, 0];
        Storage {
            memory: HashMap::new(),
            registers: registers,
            stack: Vec::new(),
        }
    }
}

pub fn get_value(instr_ptr: usize, program: &Vec<u16>, state: &Storage) -> u16 {
    let val = program[instr_ptr];
    if val <= 32767 {
        return val;
    }
    if val <= 32775 {
        return state.registers[utils::get_reg_num(val)];
    }
    println!("{}", program[instr_ptr]);
    panic!("hello")
}
