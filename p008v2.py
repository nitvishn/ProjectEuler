def getFuckingNumberInStringFormat():
    file = open('p008.txt', 'r')
    string = ""
    for line in file:
        string += line.replace('\n', '')
    return string

n = getFuckingNumberInStringFormat()

bestSum = 0
for i in range(0, len(n) - 13):
    sum = 1
    for m in range(0, 13):
        sum = (int(n[i+m])) * sum
    bestSum = max(sum, bestSum)

print(bestSum)
