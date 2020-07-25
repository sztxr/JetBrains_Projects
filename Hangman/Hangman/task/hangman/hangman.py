import random


def choose_random_word():
    dictionary = ('python', 'java', 'kotlin', 'javascript')
    return random.choice(dictionary)


def is_valid(letter, used_letters):
    if len(letter) != 1:
        print('You should print a single letter')
        return False
    elif not letter.islower():
        print('It is not an ASCII lowercase letter')
        return False
    elif letter in used_letters:
        print('You already typed this letter')
        return False
    else:
        used_letters.add(letter)
        return True


def play():
    random_word = choose_random_word()
    hint = list('-' * (len(random_word)))

    tries = 8

    used_letters = set()

    while tries:
        print()
        print(''.join(hint))
        guess = input('Input a letter:>')

        if is_valid(guess, used_letters):
            if guess not in random_word:
                print('No such letter in the word')
                tries -= 1
            elif guess in hint:
                print('No improvements')
                tries -= 1
            else:
                for i in range(len(random_word)):
                    if random_word[i] == guess:
                        hint[i] = guess

        if ''.join(hint) == random_word:
            print()
            print(''.join(hint))
            print('You guessed the word!')
            print('You survived!')
            break
        elif tries == 0:
            print('You are hanged!')
        print()


def menu():
    while True:
        option = input('Type "play" to play the game, "exit" to quit:')
        if option == 'exit':
            break
        elif option == 'play':
            play()


print('H A N G M A N')
menu()
