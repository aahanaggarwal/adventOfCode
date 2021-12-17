pub fn convert_to_ascii(num: u16) -> char {
    char::from_u32(num as u32).unwrap()
}

pub fn get_reg_num(val: u16) -> usize {
    (val - 32768) as usize
}
