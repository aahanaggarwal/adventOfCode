pub fn convert_to_ascii(num: u16) -> char {
    char::from_u32(num as u32).unwrap()
}
