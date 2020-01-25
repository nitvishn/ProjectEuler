roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
precedence = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def prec(d):
    return precedence.index(d)

def parse_roman(s):
    def value(block):
        if len(block) == 2 and precedence.index(block[0]) < precedence.index(block[1]):
            return roman_map[block[1]] - roman_map[block[0]]
        Total = 0
        for num in block:
            Total += roman_map[num]
        return Total

    blocks = []
    current_block = ""
    prev = len(precedence) + 1
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            blocks.append(s[i])
            break
        if prec(s[i]) < prec(s[i+1]):
            blocks.append(current_block)
            blocks.append(s[i] + s[i + 1])
            current_block = ""
            i += 2
        else:
            current_block += s[i]
            i += 1

    blocks.append(current_block)

    Total = 0
    for block in blocks:
        Total += value(block)

    return Total


def convert_to_roman(n):
    roman = ""
    while n >= 1000:
        roman += 'M'
        n -= 1000
    if n >= 900:
        roman += 'CM'
        n -= 900
    if n >= 500:
        roman += 'D'
        n -= 500
    if n >= 400:
        roman += 'CD'
        n -= 400
    while n >= 100:
        roman += 'C'
        n -= 100
    if n >= 90:
        roman += 'XC'
        n -= 90
    if n >= 50:
        roman += 'L'
        n -= 50
    if n >= 40:
        roman += 'XL'
        n -= 40
    while n >= 10:
        roman += 'X'
        n -= 10
    if n >= 9:
        roman += 'IX'
        n -= 9
    if n >= 5:
        roman += 'V'
        n -= 5
    if n >= 4:
        roman += 'IV'
        n -= 4
    while n >= 1:
        roman += 'I'
        n -= 1
    return roman


def parse_file():
    file = open('p089_roman.txt', 'r')
    outfile = open('p089_outfile.txt', 'w')
    input_chars = 0
    output_chars = 0
    for line in file:
        line = line.replace('\n', '')
        input_chars += len(line)
        output_chars += len(convert_to_roman(parse_roman(line)))
    return input_chars - output_chars

print(parse_file())
