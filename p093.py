import itertools

def arrange_brackets(perm, operand_perm):
    perm_copy = []
    for value in perm:
        perm_copy.append(str(value))
    perm = perm_copy
    brackets_operations = []

    # brackets_operations.append(perm[0] + operand_perm[0] + perm[1] + operand_perm[1] + perm[2] + operand_perm[2] + perm[3])

    brackets_operations.append('(' + perm[0] + operand_perm[0] + perm[1] + ')' + operand_perm[1] + perm[2] + operand_perm[2] + perm[3])
    brackets_operations.append(perm[0] + operand_perm[0] + '(' +  perm[1] + operand_perm[1] + perm[2] + ')' + operand_perm[2] + perm[3])
    brackets_operations.append(perm[0] + operand_perm[0] + perm[1] + operand_perm[1] + '(' + perm[2] + operand_perm[2] + perm[3] + ')')
    brackets_operations.append('(' + perm[0] + operand_perm[0] + perm[1] + operand_perm[1] + perm[2] + ')' + operand_perm[2] + perm[3])
    brackets_operations.append('((' + perm[0] + operand_perm[0] + perm[1] + ')' + operand_perm[1] + perm[2] + ')' + operand_perm[2] + perm[3])
    brackets_operations.append('(' + perm[0] + operand_perm[0] + '(' + perm[1] + operand_perm[1] + perm[2] + '))' + operand_perm[2] + perm[3])
    brackets_operations.append(perm[0] + operand_perm[0] + '(' + perm[1] + operand_perm[1] + perm[2] + operand_perm[2] + perm[3] + ')')
    brackets_operations.append(perm[0] + operand_perm[0] + '((' + perm[1] + operand_perm[1] + perm[2] + ')' + operand_perm[2] + perm[3] + ')')
    brackets_operations.append(perm[0] + operand_perm[0] + '(' + perm[1] + operand_perm[1] + '(' + perm[2] + operand_perm[2] + perm[3] + '))')
    return brackets_operations

def longest_consecutive_run(L):
    L.sort()
    prev = 0
    for i in range(len(L)):
        if L[i] != prev + 1:
            break
        prev += 1
    return prev

def consecutive(selection):
    assert len(selection) == 4
    operand_set = {'+', '/', '-', '*'}
    combo_set = set(selection)
    reached = set()
    for perm in itertools.permutations(combo_set):
        for operand_combo in itertools.combinations_with_replacement(operand_set, 3):
            for operand_perm in itertools.permutations(operand_combo):
                for item in arrange_brackets(perm, operand_perm):
                    try:
                        k = eval(item)
                        if int(k) == k and k > 0:
                            reached.add(k)
                    except ZeroDivisionError:
                        continue
    return longest_consecutive_run(list(reached))

bestString = None
bestValue = 0
for a in range(10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                k = consecutive([a, b, c, d])
                if k > bestValue:
                    bestString = str(a) + str(b) + str(c) + str(d)
                    bestValue = k
print(bestValue)
print(bestString)
