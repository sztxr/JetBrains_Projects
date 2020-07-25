from math import log
# natural log - log(x)
# logarithm base - log(x, base)

x = int(input())
base = int(input())

print(round(log(x, base) if base > 1 else log(x), 2))
