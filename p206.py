import math

format = "1_2_3_4_5_6_7_8_9_0"


def fits_format(n):
    n = str(n)
    if len(n) != len(format):
        return False
    for i in range(len(n)):
        if format[i] == '_':
            continue
        if format[i] != n[i]:
            return False
    return True

checkpoints = []
for i in range(10):
    string = ""
    for char in format:
        if char == '_':
            string += '0'
        else:
            string += char
    string = string[0] + str(i) + string[2:]
    checkpoints.append(int(math.sqrt(int(string))))

check_index = 9
for n in range(checkpoints[check_index], checkpoints[check_index]*2):
    if fits_format(n**2):
        print(n)
        break
    if n % 1000 == 0:
        print(n**2)
