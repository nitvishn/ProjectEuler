N = 1000
for a in range(1, N):
    for b in range(1, N):
        c = (a * a + b * b)**(1 / 2)
        if int(c) != c:
            continue
        if a + b + c > N:
            break
        elif a + b + c < N:
            continue
        print(int(a*b*c))
        exit()
