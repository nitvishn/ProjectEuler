import random

def determine(n):
    n *= 10
    return int(n)

while(True):
    for i in range(random.randint(100, 110)):
        print(determine(random.random()), end = '')
    print()
