# read sums.txt
with open('sums.txt') as file:
    for line in file:
        line = line.split()
        results = [int(i) for i in line]
        print(sum(results))
file.close()
