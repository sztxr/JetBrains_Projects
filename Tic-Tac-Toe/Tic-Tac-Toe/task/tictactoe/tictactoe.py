table = [[' ' for j in range(3)] for i in range(3)]

state = {
    'X': False,
    'O': False,
    'is_empty': False,
    'finished': False,
    'turn': 0
}


def print_table():
    print('-' * 9)
    for row in table:
        print('|', ' '.join([el for el in row]), '|')
    print('-' * 9)


def check(v0, v1, v2):
    return v1 == v0 == v2 and v0 != ' '


def game_state(state_):
    for k in range(3):
        # rows
        if check(table[k][0], table[k][1], table[k][2]):
            state[f'{table[k][0]}'] = True
        # columns
        if check(table[0][k], table[1][k], table[2][k]):
            state[f'{table[0][k]}'] = True
        # empty
        state['is_empty'] = table[k][0] == '_' or table[k][1] == '_' or table[k][2] == '_'

    # diagonals
    if check(table[0][0], table[1][1], table[2][2]) or check(table[0][2], table[1][1], table[2][0]):
        state[f'{table[1][1]}'] = True

    if state['X']:
        print('X wins')
        state['finished'] = True
    elif state['O']:
        print('O wins')
        state['finished'] = True
    elif state['turn'] == 9:
        print('Draw')
        state['finished'] = True

    return state


def make_move(state_):
    turn = 'X'
    while not state['finished']:
        move = input('Enter the coordinates:').split()

        if len(move) == 2 and move[0].isnumeric() and move[1].isnumeric():
            x, y = int(move[0]) - 1, int(move[1]) - 1
        else:
            print('You should enter numbers!')
            continue

        if x not in range(3) or y not in range(3):
            print('Coordinates should be from 1 to 3!')
            continue

        if table[2 - y][x] == 'X' or table[2 - y][x] == 'O':
            print('This cell is occupied! Choose another one!')
            continue
        elif turn == 'X':
            turn = 'O'
            state['turn'] += 1
            table[2 - y][x] = 'X'
        else:
            turn = 'X'
            state['turn'] += 1
            table[2 - y][x] = 'O'

        print_table()
        print(state)
        game_state(state_)


print_table()
make_move(state)
