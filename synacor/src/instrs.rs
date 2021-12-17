use crate::utils;

pub fn out(num: u16) {
    let byte_to_print = utils::convert_to_ascii(num);
    print!("{}", byte_to_print);
}
