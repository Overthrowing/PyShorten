import string
from math import floor


def encode(num, base=62):
    if base <= 0 or base > 62:
        return 0
    chars = string.digits + string.ascii_letters
    final = ""
    q = num

    while floor(q) > 0:
        r = q % base
        q = floor(q / base)
        res = chars[r]
        final = final + res

    return final[::-1]


def decode(num, base=62):
    chars = string.digits + string.ascii_letters
    res = int(chars.find(str(num)[0]))

    for char in str(num)[1:]:
        char = chars.find(char)
        res = res * base + char

    return res
