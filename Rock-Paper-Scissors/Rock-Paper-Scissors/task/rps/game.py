from random import choice

# rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
moves = ['rock', 'paper', 'scissors']
commands = ['!exit', '!rating']
score = 0

name = input('Enter your name:')
print('Hello,', name)

with open('rating.txt') as file:
    for line in file:
        u_name, u_score = line.split()
        if u_name == name:
            score = int(u_score)
            break
file.close()

game_mode = input().strip()
if len(game_mode):
    game_mode = game_mode.split(',')
    moves = game_mode


def define_rules(lst):
    list_len = len(lst)
    if list_len > 2 and list_len % 2 == 1:
        winning_moves_len = int((list_len - 1) / 2)
        winning_moves = dict()
        for i in range(list_len):
            temp_list = []
            temp_list.extend(lst[i + 1:])
            temp_list.extend(lst[:i])
            winning_moves[lst[i]] = temp_list[:winning_moves_len]
        return winning_moves


rules = define_rules(moves)

print('Okay, let\'s start')

while True:
    computer = choice(moves)
    player = input()

    if player not in moves and player not in commands:
        print('Invalid input')
        continue

    if player == '!exit':
        print('Bye!')
        break
    elif player == '!rating':
        print('Your rating:', score)
    elif computer == player:
        print(f'There is a draw ({computer})')
        score += 50
    elif computer in rules[player]:
        print(f'Sorry, but computer chose {computer}')
    else:
        print(f'Well done. Computer chose {computer} and failed')
        score += 100
