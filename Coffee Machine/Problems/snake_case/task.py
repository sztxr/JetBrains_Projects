word = input()
snake_case = ''

for char in word:
    if char.isupper():
        snake_case += '_' + char.lower()
    else:
        snake_case += char

print(snake_case)
