import operator
from functools import lru_cache

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

def move(array: tuple, moves: str):
    moves = moves.split()
    return tuple(tuple([ops[i[0]](array[0], int(i[1])), array[1]]) for i in moves) + tuple(tuple([array[0], ops[i[0]](array[1], int(i[1]))]) for i in moves)

@lru_cache(None)
def game_two_players(array: tuple, fin_value: int, fin_pos: str, moves: str, player = 1, step = 1):
    if sum(array) >= fin_value and str(step) in fin_pos:
        return True
    if (sum(array) < fin_value and step == fin_pos[-1]) or (sum(array) >= fin_value and step != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_two_players(i, fin_value, fin_pos, moves, player, step + 1) for i in move2(array, moves))
    return all(game_two_players(i, fin_value, fin_pos, moves, player, step + 1) for i in move2(array, moves))

def move2(array: tuple, moves: str):
    moves = moves.split()
    fin_array = list(list(array) for i in range(len(array) * len(moves)))
    for i in range(len(fin_array)):
        fin_array[i][i // len(moves)] = ops[moves[i % len(moves)][0]](fin_array[i][i // len(moves)], int(moves[i % len(moves)][1]))
    fin_array = tuple(set(tuple(tuple(i) for i in fin_array)))
    return fin_array

for i in range(1, 43):
    if game_two_players(tuple([5, i]), 49, '4', '+1 *3', 1):
        print(i)
