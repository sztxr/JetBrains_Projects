names = []
num = []
x = input()

while x != 'MEOW':
    temp_list = x.split()
    names.append(temp_list[0])
    num.append(int(temp_list[1]))
    x = input()

i = num.index((max(num)))
print(names[i])
