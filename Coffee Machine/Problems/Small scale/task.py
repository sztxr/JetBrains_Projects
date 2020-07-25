numbers = []
x = input()

while x != '.':
    numbers.append(float(x))
    x = input()

print(min(numbers))
