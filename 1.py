import operator
from functools import lru_cache

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.pow,
}

def move(array: tuple, moves: str):
    moves = moves.split()
    fin_array = list(list(array) for i in range(len(array) * len(moves)))
    for i in range(len(fin_array)):
        fin_array[i][i // len(moves)] = ops[moves[i % len(moves)][0]](fin_array[i][i // len(moves)], int(moves[i % len(moves)][1]))
    fin_array = tuple(set(tuple(tuple(i) for i in fin_array)))
    return fin_array

@lru_cache(None)
def game_sum(array: tuple, fin_value: int, fin_pos: str, moves: str, player = 1, step = 1):
    if sum(array) >= fin_value and str(step) in fin_pos:
        return True
    if (sum(array) < fin_value and step == fin_pos[-1]) or (sum(array) >= fin_value and step != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return all(game_sum(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))

@lru_cache(None)
def game_any(array: tuple, fin_value: int, fin_pos: str, moves: str, player = 1, step = 1):
    if any(i >= fin_value for i in array) and str(step) in fin_pos:
        return True
    if (all(i < fin_value for i in array) and step == fin_pos[-1]) or (any(i >= fin_value for i in array) and step != fin_pos[-1]):
        return False
    if step % 2 == player % 2:
        return any(game_any(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))
    return all(game_any(i, fin_value, fin_pos, moves, player, step + 1) for i in move(array, moves))

for i in range(2, 43):
    if game_any(tuple([3, i]), 49, '2', '+1 ^3', 1):
        print(i)
