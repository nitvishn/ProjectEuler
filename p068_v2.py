import itertools


def partitions(n):
    possible = list(range(1, 11))
    parts = []
    for part in itertools.permutations(possible, 3):
        if 10 == part[1] or 10 == part[2]:
            continue
        if sum(part) == n:
            parts.append(part)
    return parts


def select_with_n(n, parts):
    return_parts = set()
    for part in parts:
        if n in part:
            return_parts.add(part)
    return return_parts


def all_solutions(S):
    parts = partitions(S)
    sols_2 = []
    for i in range(len(parts)):
        for j in range(len(parts)):
            if i == j:
                continue
            part1 = parts[i]
            part2 = parts[j]
            if part1[2] != part2[1]:
                continue
            if part1[0] in part2:
                continue
            if part2[0] in part1:
                continue
            if part2[2] in part1:
                continue
            sols_2.append(part1 + part2)
    sols_4 = []
    for part1 in sols_2:
        for part2 in sols_2:
            if part1[0] != 10:
                continue
            if part1[0] in part2 or part1[3] in part2 or part2[0] in part1 or part2[3] in part1:
                continue
            if part1[-1] != part2[1]:
                continue
            combined = part1 + part2
            for i in range(0, len(combined)):
                if i % 3 == 0 and combined.count(combined[i]) != 1:
                    continue
                if i % 3 != 0 and combined.count(combined[i]) > 2:
                    continue
            sols_4.append(part1 + part2)
    sols = []
    for part1 in sols_4:
        for part2 in parts:
            if part1[-1] != part2[1] or part2[-1] != part1[1]:
                continue
            combined = part1 + part2
            accepted = True
            for i in range(0, len(combined)):
                if i % 3 == 0 and combined.count(combined[i]) != 1:
                    accepted = False
                    break
                if i % 3 != 0 and combined.count(combined[i]) != 2:
                    accepted = False
                    break
            if accepted:
                sols.append(combined)
    return sols


def arrange(solution):
    lowest_index = 0
    lowest_node = solution[0]
    for i in range(0, len(solution), 3):
        if solution[i] < lowest_node:
            lowest_index = i
            lowest_node = solution[i]
    first_bit = solution[lowest_index:]
    rest_bit = solution[:lowest_index]
    return first_bit + rest_bit


def value(solution):
    S = ""
    for n in solution:
        S += str(n)
    return int(S)


sols = []
for i in range(1, 27):
    sols.extend(all_solutions(i))
for i in range(len(sols)):
    sols[i] = value(arrange(sols[i]))

print(max(sols))
