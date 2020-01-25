def f(b, x):
    return b**x


a=5
b=10
epsilon=2

#0.6989700043

def bisectionSearch(epsilon, upper, lower, target):
    x = (upper + lower) / 2
    if(round(target, epsilon)==round(f(b, x), epsilon)):
        return x
    print(x)
    if(round(f(b, x), epsilon)>round(target, epsilon)):
        upper=x
        return bisectionSearch(epsilon, upper, lower, target)
    elif(round(f(b, x), epsilon)<round(target, epsilon)):
        lower=x
        return bisectionSearch(epsilon, upper, lower, target)

print(bisectionSearch(epsilon, b**a, b**-a, a))