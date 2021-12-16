file = open("inputs/day16.txt", 'r')
test_file = open("inputs/day16_test1.txt", 'r')
# file = test_file

bits = []
for digit in file.readline():
    integer = int(digit, 16)
    bin_digits = format(integer, '0>4b')
    bits.extend([int(x) for x in bin_digits])


def get_n_bit_number(packet, index, n):
    num_str = ''
    for i in range(index, index + n):
        num_str += str(packet[i])

    return int(num_str, 2)

def parse_packet(packet: list):
    index = 0
    n = len(packet)

    while index < n:
        # get version
        total_version = get_n_bit_number(packet, index, 3)
        index += 3

        # get type
        type = get_n_bit_number(packet, index, 3)
        index += 3

        if type == 4:
            while packet[index] != 0:
                index += 5
            index += 5
            return total_version, index

        else:
            operator_encoding = packet[index]
            index += 1
            if operator_encoding == 0:
                sub_packets_length = get_n_bit_number(packet, index, 15)
                index += 15

                offset = 0

                while offset < sub_packets_length:

                    version, offset_diff = parse_packet(packet[index + offset:])
                    total_version += version
                    offset += offset_diff

                return total_version, index + offset

            else:
                num_sub_packets = get_n_bit_number(packet, index, 11)
                index += 11

                offset = 0

                for _ in range(num_sub_packets):
                    version, offset_diff = parse_packet(packet[index + offset:])
                    total_version += version
                    offset += offset_diff

                return total_version, index + offset


print(parse_packet(bits))
