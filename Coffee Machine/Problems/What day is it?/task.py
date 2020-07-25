user_utc = int(input())

if user_utc < 0:
    print('Monday')
elif user_utc == 0:
    print('Tuesday')
else:
    print('Wednesday')