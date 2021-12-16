import sys
import numpy

file = open("inputs/day16.txt", 'r')
test_file = open("inputs/day16_test4.txt", 'r')
# file = test_file

bits = []

if len(sys.argv) > 1:
    bit_str = sys.argv[1]
else:
    bit_str = file.readline()

for digit in bit_str:
    integer = int(digit, 16)
    bin_digits = format(integer, '0>4b')
    bits.extend([int(x) for x in bin_digits])


def get_n_bit_number(packet, index, n):
    num_str = ''
    for i in range(index, index + n):
        num_str += str(packet[i])

    return int(num_str, 2)

def compute_value(type, values):
    if type == 0:
        return sum(values)
    elif type == 1:
        return numpy.prod(values)
    elif type == 2:
        return min(values)
    elif type == 3:
        return max(values)
    elif type == 5:
        return 1 if values[0] > values[1] else 0
    elif type == 6:
        return 1 if values[0] < values[1] else 0
    elif type == 7:
        return 1 if values[0] == values[1] else 0

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
            num_str = packet[index + 1:index + 5]
            while packet[index] != 0:
                index += 5
                num_str.extend(packet[index + 1:index + 5])

            number = int("".join([str(num) for num in num_str]), 2)
            index += 5
            return number, index

        else:
            operator_encoding = packet[index]
            index += 1
            if operator_encoding == 0:
                sub_packets_length = get_n_bit_number(packet, index, 15)
                index += 15

                offset = 0
                packet_values = []

                while offset < sub_packets_length:
                    value, offset_diff = parse_packet(packet[index + offset:])
                    packet_values.append(value)
                    offset += offset_diff

                value = compute_value(type, packet_values)

                return value, index + offset

            else:
                num_sub_packets = get_n_bit_number(packet, index, 11)
                index += 11

                offset = 0
                packet_values = []

                for _ in range(num_sub_packets):
                    value, offset_diff = parse_packet(packet[index + offset:])
                    packet_values.append(value)
                    offset += offset_diff

                value = compute_value(type, packet_values)

                return value, index + offset


print(parse_packet(bits)[0])
