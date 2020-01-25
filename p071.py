N = 10**6
a = 3
b = 7
bestNum = 0
bestDenom = 1
for currDenom in range(2, N):
    currNum = (a*currDenom - 1) // b
    if bestNum*currDenom < currNum*bestDenom:
        bestNum = currNum
        bestDenom = currDenom
print(bestNum)
