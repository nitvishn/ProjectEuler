import math

limit = 12000
count = 0
fracs = set()
for d in range(2, limit + 1):
    for n in range(int(d/3), math.ceil(d/2)):
        if n/d in fracs:
            continue
        if not (1/3 < n/d < 1/2):
            continue
        fracs.add(n/d)
        count += 1
print(count)
