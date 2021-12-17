use std::collections::HashMap;

struct Storage {
    memory: HashMap<u16, u16>,
    registers: Vec<u16>,
    stack: Vec<u16>,
}

pub fn get_value(instr_ptr: usize, program: &Vec<u16>) -> u16 {
    8
}
