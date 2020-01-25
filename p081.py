def load_matrix():
    matrix = []
    for line in open('p081_matrix.txt', 'r'):
        L = []
        for string in line.replace('\n', '').split(','):
            L.append(int(string))
        matrix.append(L)
    return matrix

minimum_sum_memo = {}
def minimum_sum(matrix, i, j):
    if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        return matrix[i][j]

    if (i, j) in minimum_sum_memo:
        return minimum_sum_memo[(i, j)]

    if i == len(matrix) - 1:
        return matrix[i][j] + minimum_sum(matrix, i, j+1)

    if j == len(matrix[i]) - 1:
        return matrix[i][j] + minimum_sum(matrix, i+1, j)

    minimum_sum_memo[(i, j)] = matrix[i][j] + min([minimum_sum(matrix, i, j+1), minimum_sum(matrix, i+1, j)])
    return minimum_sum_memo[(i, j)]

matrix = load_matrix()
print(minimum_sum(matrix, 0, 0))
