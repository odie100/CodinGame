import math


w, h = [int(i) for i in input().split()]
liste_pixel = []
for i in range(h):
    for j in input().split():
        liste_pixel.append(int(j))


def toBinary(number):
    return format(number, 'b').zfill(8)  # rjust(8, "0")


def bit_extractor(pixel_list):
    binary_list = []
    for pixel in pixel_list:
        binary_list.append(toBinary(pixel))

    return binary_list


def get_weak_bits(bin_list):
    _BYTE = 8
    bit_list, result, asci, final = [], [], [], []

    for byte in bin_list:
        bit_list.append(byte[len(byte) - 1])

    k = len(bit_list) / _BYTE  # n bytes

    for i in range(1, int(k) + 1):
        result.append("".join(bit_list[_BYTE*(i-1):_BYTE*i]))

    for value in result:
        asci.append(convert_to_decimal(value))

    for unicode in asci:
        final.append(chr(unicode))

    print("".join(final))


def convert_to_decimal(binary):
    digit = 0
    i = 0
    for x in binary[::-1]:
        digit += int(math.pow(2, i)) * int(x)
        i += 1

    return digit


get_weak_bits(bit_extractor(liste_pixel))
