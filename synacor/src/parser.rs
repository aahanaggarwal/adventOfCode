pub fn get_number_vec(bytes: &Vec<u8>) -> Vec<u16> {
    let mut nums: Vec<u16> = vec![];

    let mut index = 0;
    while index < bytes.len() {
        let low_byte = bytes[index] as u16;
        let high_byte = bytes[index + 1] as u16;

        nums.push((high_byte << 8) | low_byte);

        index += 2;
    }

    nums
}
