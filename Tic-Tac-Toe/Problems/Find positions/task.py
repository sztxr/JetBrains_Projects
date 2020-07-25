num_list = input().split()
num = input()

pos = [str(i) for (i, item) in enumerate(num_list) if num_list[i] == num]
print(' '.join(pos) or 'not found')
