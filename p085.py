partitions_previous = set()
def rectangular_partitions(width, height):
    return ((width)*(width+1)*(height)*(height+1))//4

n = 2000
m = 1
best = abs(2000000 - rectangular_partitions(n, m))
bestArea = 2000
for n in range(1, 2000):
    for m in range(1, 2000):
        parts = rectangular_partitions(n, m)
        if abs(parts - 2000000) < best:
            best = abs(parts - 2000000)
            bestArea = n*m
        if parts - 2000000 > best:
            break
print(bestArea)
