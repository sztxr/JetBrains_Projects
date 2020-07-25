# Save the input in this variable
ticket = input()
half = int(len(ticket) / 2)

# Add up the digits for each half
half1 = sum(int(x) for x in ticket[:half])
half2 = sum(int(y) for y in ticket[half:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")