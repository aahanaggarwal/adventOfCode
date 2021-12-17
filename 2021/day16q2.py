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


def get_n_bit_number(n):
    global index
    num_str = ''
    for i in range(index, index + n):
        num_str += str(bits[i])
    index += n
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
        return int(values[0] > values[1])
    elif type == 6:
        return int(values[0] < values[1])
    elif type == 7:
        return int(values[0] == values[1])


index = 0
def parse_packet():
    global index
    _ = get_n_bit_number(3)
    type = get_n_bit_number(3)

    if type == 4:
        bitlist = bits[index + 1:index + 5]
        while bits[index] != 0:
            index += 5
            bitlist.extend(bits[index + 1:index + 5])

        number = 0
        for bit in bitlist:
            number = (number << 1) | bit
        index += 5
        return number

    else:
        operator_encoding = bits[index]
        index += 1
        packet_values = []
        if operator_encoding == 0:
            sub_packets_length = get_n_bit_number(15)
            end_index = index + sub_packets_length
            while index < end_index:
                packet_values.append(parse_packet())

        else:
            num_sub_packets = get_n_bit_number(11)
            for _ in range(num_sub_packets):
                packet_values.append(parse_packet())

        value = compute_value(type, packet_values)

        return value


print(parse_packet())
