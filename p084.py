import random

random.seed(10)

board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", 'U1', "C2", "C3", "R2", "D1", "CC2", "D2",
         "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']


def next_type(tile, type):
    i = board.index(tile)
    while(board[i][0] != type):
        i += 1
        if i >= len(board):
            i = 0
    return board[i]


def squares_after(tile, num):
    i = board.index(tile)
    i += num
    if i >= len(board):
        i -= len(board)
    return board[i]


def roll_dice(dice_faces=4):
    return (random.randint(1, dice_faces), random.randint(1, dice_faces))


def tile_number(tile):
    i = board.index(tile)
    string = str(i)
    if len(str(i)) == 1:
        string = '0' + string
    return string


def redirect(tile):
    if "CC" in tile:
        possible = ["GO", "JAIL"]
        possible_prob = 2 / 16
        if random.random() > possible_prob:
            return tile
        choice = random.choice(possible)
    elif "CH" in tile:
        possible = ["GO", "JAIL", "C1", 'E3', 'H2', 'R1', next_type(
            tile, 'R'), next_type(tile, 'R'), next_type(tile, 'U'), squares_after(tile, -3)]
        possible_prob = 10 / 16
        if random.random() > possible_prob:
            return tile
        choice = random.choice(possible)
    elif tile == "G2J":
        choice = "JAIL"
    else:
        choice = tile
    return choice


def sort_key(n):
    return tile_visits[n]


tile_visits = {}
turns = 100000
current = "GO"
double_row = 0
for i in range(turns):
    print(i)
    roll = roll_dice()
    if roll[0] == roll[1]:
        double_row += 1
    else:
        double_row = 0
    if double_row == 3:
        current = "JAIL"
    else:
        current = redirect(squares_after(current, sum(roll)))
    tile_visits[current] = tile_visits.get(current, 0) + 1

highest_probs = list(tile_visits.keys())
highest_probs.sort(key=sort_key, reverse=True)

modal = ""
for best in highest_probs[:3]:
    modal += tile_number(best)

print(highest_probs)
print(modal)
