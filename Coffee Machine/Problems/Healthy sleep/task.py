A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print('Normal')
elif H >= B:
    print('Excess')
elif H <= B:
    print('Deficiency')
