numbers = []
x = input()

while x != '.':
    numbers.append(int(x))
    x = input()

print(sum(numbers) / len(numbers))
