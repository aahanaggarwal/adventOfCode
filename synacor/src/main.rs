use std::fs;
use synacor_vm::parser;
use synacor_vm::runner;
use synacor_vm::storage;

fn main() {
    // Read file into bit array
    let file_path = "/home/aahan/adventOfCode/synacor/challenge.bin";
    let byte_vector = fs::read(file_path).unwrap();
    let mut program = parser::get_number_vec(&byte_vector);
    let mut state = storage::Storage::new();

    runner::run_program(&mut program, &mut state);
}
