from game import initial_position, primitive, gen_moves, do_moves
from constants import WIN, LOSE, TIE, UNDECIDED

def solve(pos):
    if primitive(pos) != UNDECIDED:
        return primitive(pos)
    return max(-solve(do_moves(pos,move)) for move in gen_moves(pos))

res = solve(initial_position())

if res == WIN:
    print "win"
elif res == LOSE:
    print "lose"
elif res == TIE:
    print "tie"

