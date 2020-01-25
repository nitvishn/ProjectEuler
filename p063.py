def num_digits(n):
    return len(str(n).replace('.', ''))


count = 0
n = 1
i = 0
newcount = 1
while(newcount != 0):
    i = 0
    while(num_digits(i**n) <= n):
        newcount = 0
        if num_digits(i**n) == n:
            newcount += 1
        i += 1
    n += 1
    count += newcount
print(count)
