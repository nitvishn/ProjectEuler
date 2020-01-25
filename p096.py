from copy import copy, deepcopy
import random
import time

nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

def getBoards():
    file = open("p096_sudoku.txt", 'r')
    boards = []
    current = []
    for line in file:
        if line[0] == 'G':
            boards.append(current)
            current = []
            continue
        line = line.replace('\n', '')
        row = []
        for char in line:
            row.append(char)
        current.append(row)
    boards.append(current)
    boards.remove([])
    return boards
def getColumns(board):
    columns = []
    for i in range(len(board)):
        columns.append("")
    for row in board:
        for i in range(len(row)):
            columns[i] += row[i]
    return columns
def getGrids(board):
    grids = []
    for i in range(9):
        grids.append("")
    for i in range(len(board)):
        for j in range(len(board)):
            grids[3 * (i // 3) + (j // 3)] += board[i][j]
    return grids
def drawBoard(board):
    juan = ' ------------------------------------- '
    for row in board:
        print(juan)
        print(' | ', end='')
        for item in row:
            if item == '0':
                item = ' '
            print(item, end='')
            print(' | ', end='')
        print()
    print(juan)
def getPossibilities(board, columns, grids, r, c):
    if board[r][c] != '0':
        return set()
    poss = copy(nums)
    for item in columns[c]:
        if item in poss:
            poss.remove(item)
    for item in board[r]:
        if item in poss:
            poss.remove(item)
    for item in grids[3 * (r // 3) + (c // 3)]:
        if item in poss:
            poss.remove(item)
    return poss
def testWin(board, columns, grids):
    for row in board:
        if set(row) != nums:
            return False
    for column in columns:
        if set(column) != nums:
            return False
    for grid in getGrids(board):
        if set(grid) != nums:
            return False
    return True
def testValidity(board, columns, grids, possibilities):
    def testUnique(row):
        found = set()
        for item in row:
            if item in found:
                return False
            if item == '0':
                continue
            found.add(item)
        return True

    # Test for uniqueness
    for row in board:
        if not testUnique(row):
            return False

    for column in columns:
        if not testUnique(column):
            return False

    for grid in grids:
        if not testUnique(grid):
            return False

    # Test for solvability
    for r in range(len(board)):
        row = board[r]
        should = copy(nums)
        for c in range(len(row)):
            if board[r][c] == '0':
                continue
            should.remove(board[r][c])
        poss = set()
        for c in range(len(row)):
            for p in possibilities[(r, c)]:
                poss.add(p)
        for p in should:
            if p not in poss:
                return False

    for c in range(len(columns)):
        column = columns[c]
        should = copy(nums)
        for r in range(len(column)):
            if board[r][c] == '0':
                continue
            should.remove(board[r][c])
        poss = set()
        for r in range(len(column)):
            for p in possibilities[(r, c)]:
                poss.add(p)
        for p in should:
            if p not in poss:
                return False

    for g in range(len(grids)):
        grid = grids[g]
        should = copy(nums)
        for i in range(len(grid)):
            (r, c) = ((i // 3) + (3 * (g // 3)), (i % 3) + (3 * (g % 3)))
            if board[r][c] == '0':
                continue
            should.remove(board[r][c])
        poss = set()
        for i in range(len(grid)):
            (r, c) = ((i // 3) + (3 * (g // 3)), (i % 3) + (3 * (g % 3)))
            for p in possibilities[(r, c)]:
                poss.add(p)
        for p in should:
            if p not in poss:
                return False

    return True
def computePossibilities(board, grids, columns):
    possibilities = {}
    columns = getColumns(board)
    grids = getGrids(board)
    for r in range(len(board)):
        for c in range(len(board[r])):
            # if board[r][c] != '0'
            possibilities[(r, c)] = getPossibilities(
                board, columns, grids, r, c)
    return possibilities
def play(board):
    board = deepcopy(board)
    columns = getColumns(board)
    grids = getGrids(board)
    possibilities = {}
    altered = False
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != '0':
                continue
            poss = getPossibilities(board, columns, grids, r, c)
            possibilities[(r, c)] = poss
            if len(poss) == 1:
                altered = True
                board[r][c] = poss.pop()

    columns = getColumns(board)
    grids = getGrids(board)
    possibilities = computePossibilities(board, grids, columns)

    for g in range(len(grids)):
        grid = grids[g]
        posses = {}
        for i in range(len(grid)):
            (r, c) = ((i // 3) + (3 * (g // 3)), (i % 3) + (3 * (g % 3)))
            if board[r][c] == '0':
                for p in possibilities[(r, c)]:
                    posses[p] = posses.get(p, [])
                    posses[p].append((r, c))
        for p in posses:
            if len(posses[p]) == 1:
                altered = True
                # print(p, posses[p], posses[p][0][0], posses[p][0][1], possibilities[posses[p][0]])
                board[posses[p][0][0]][posses[p][0][1]] = p

    columns = getColumns(board)
    grids = getGrids(board)
    possibilities = computePossibilities(board, grids, columns)

    for c in range(len(columns)):
        column = columns[c]
        posses = {}
        for r in range(len(column)):
            if board[r][c] == '0':
                for p in possibilities[(r, c)]:
                    posses[p] = posses.get(p, [])
                    posses[p].append((r, c))
        for p in posses:
            if len(posses[p]) == 1:
                altered = True
                # print(p, posses[p], posses[p][0][0], posses[p][0][1], possibilities[posses[p][0]])
                board[posses[p][0][0]][posses[p][0][1]] = p

    columns = getColumns(board)
    grids = getGrids(board)
    possibilities = computePossibilities(board, grids, columns)

    for r in range(len(board)):
        row = board[r]
        posses = {}
        for c in range(len(row)):
            if board[r][c] == '0':
                for p in possibilities[(r, c)]:
                    posses[p] = posses.get(p, [])
                    posses[p].append((r, c))
        for p in posses:
            if len(posses[p]) == 1:
                altered = True
                # print(p, posses[p], posses[p][0][0], posses[p][0][1], possibilities[posses[p][0]])
                board[posses[p][0][0]][posses[p][0][1]] = p

    columns = getColumns(board)
    grids = getGrids(board)
    possibilities = computePossibilities(board, grids, columns)

    if testWin(board, columns, grids) == True:
        return board

    if altered == True:
        return play(board)
    valid = testValidity(board, columns, grids, possibilities)
    if not valid:
        return None

    picked = None
    picked_poss = nums
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != '0':
                continue
            if len(possibilities[(r, c)]) > 1 and len(possibilities[(r, c)]) <= len(picked_poss):
                picked = (r, c)
                picked_poss = possibilities[(r, c)]

    children = []
    for p in picked_poss:
        child = copy(board)
        child[picked[0]][picked[1]] = p
        k = play(child)
        if not (k is None):
            return k

s = time.time()
boards = getBoards()
# print(len(boards))
# drawBoard(boards[-1])
acc = 0
for board in boards:
    board = play(board)
    num = ""
    for char in board[0][:3]:
        num += char
    # print(num)
    acc += int(num)
print(acc)
print("Program terminated in", time.time() - s, "seconds.")
