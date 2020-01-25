def self_power(n):
    return n**n

string=0
for i in range(1, 1001):
    string+=self_power(i)

print(str(string)[-10:])

