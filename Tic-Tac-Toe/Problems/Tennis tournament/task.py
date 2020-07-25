n = int(input())
winners = []

for i in range(n):
    player = input().split()
    if player[1] == 'win':
        winners.append(player[0])

print(winners)
print(len(winners))
