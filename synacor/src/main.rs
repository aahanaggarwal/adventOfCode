use std::fs;
use synacor_vm::parser;
use synacor_vm::runner;

fn main() {
    // Read file into bit array
    let file_path = "/home/aahan/adventOfCode/synacor/challenge.bin";
    let byte_vector = fs::read(file_path).unwrap();
    let program = parser::get_number_vec(&byte_vector);

    runner::run_program(&program);
}
