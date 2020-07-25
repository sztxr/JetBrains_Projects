def plural(amount, animal_name):
    amount //= animals[animal_name]
    if animal_name == 'sheep':
        print(f'{amount} sheep')
    elif amount >= 2:
        print(f'{amount} {animal_name}s')
    else:
        print(f'{amount} {animal_name}')


animals = {
    'sheep': 6769,
    'cow': 3848,
    'pig': 1296,
    'goat': 678,
    'chicken': 23,
}

user_money = int(input())

if user_money < 23:
    print('None')
elif user_money >= 6769:
    plural(user_money, 'sheep')
elif 3848 <= user_money < 6769:
    plural(user_money, 'cow')
elif 1296 <= user_money < 3848:
    plural(user_money, 'pig')
elif 678 <= user_money < 1296:
    plural(user_money, 'goat')
elif 23 <= user_money < 678:
    plural(user_money, 'chicken')
