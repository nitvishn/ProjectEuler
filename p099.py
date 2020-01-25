import math

def higher(eh, bh, ec, bc):
    if eh < ec * math.log(bc, bh):
        return True
    return False


file = open('p099_base_exp.txt')
highestB = None
highestE = None
n = 0
i = 1
for line in file:
    line = line.split(',')
    b = int(line[0])
    e = int(line[1])
    if highestB == None or e*math.log(b, highestB) > highestE:
        highestB = b
        highestE = e
        n = i
    i += 1
print(n)
