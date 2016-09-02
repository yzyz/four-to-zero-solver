from constants import LOSE, UNDECIDED

def initial_position():
    return 4

def primitive(pos):
    if pos == 0:
        return LOSE
    return UNDECIDED

def gen_moves(pos):
    if pos == 0:
        return []
    elif pos == 1:
        return [1]
    else:
        return [1,2]

def do_moves(pos, move):
    return pos - move
