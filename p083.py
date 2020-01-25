def load_matrix():
    matrix = []
    for line in open('p083_matrix.txt', 'r'):
        L = []
        for string in line.replace('\n', '').split(','):
            L.append(int(string))
        matrix.append(L)
    return matrix


def find_infinity(matrix):
    tot = sum(matrix[0])
    for i in range(len(matrix)):
        tot += matrix[i][-1]
    return tot + 1


def getMoves(matrix, i, j, past):
    moves = []
    if i > 0:
        moves.append((-1, 0))
    if i < len(matrix) - 1:
        moves.append((1, 0))
    if j < len(matrix[i]) - 1:
        moves.append((0, 1))
    if j > 0:
        moves.append((0, -1))
    if (past[0] - i, past[1] - j) in moves:
        moves.remove((past[0] - i, past[1] - j))
    return moves

minimum_sum_memo = {}


def minimum_sum(matrix, i, j, past):
    #base case
    if i == 0 and j == 0:
        minimum_sum_memo[(i, j)] = matrix[i][j]

    moves = getMoves(matrix, i, j, past)
    goFurther = []

    for move in moves:
        key = (i + move[0], j + move[1])
        current = minimum_sum_memo.get(key, INFINITY)
        checkVal = minimum_sum_memo[(i, j)] + matrix[key[0]][key[1]]
        if checkVal < current:
            goFurther.append(key)
            minimum_sum_memo[key] = checkVal

    for tile in goFurther:
        minimum_sum(matrix, tile[0], tile[1], (i, j))


# matrix = [
#     [1, 8, 2],
#     [9, 7, 6],
#     [4, 5, 10]
# ]
# matrix = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ]
matrix = load_matrix()

INFINITY = find_infinity(matrix)
below = INFINITY

print("Warning: Will take around two minutes. Run at your own discretion. If your machine blows up due to overheating, it's not on me. Okay?")
minVal = minimum_sum(matrix, 0, 0, (0, 0))
print(minimum_sum_memo[(len(matrix) - 1, len(matrix[0]) - 1)])
