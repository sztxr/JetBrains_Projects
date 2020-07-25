# put your python code here
number = int(input())
print(sum(map(int, str(number))))

# str(num) return a string version of your number
# map(int,string) applies an integer cast to your list
# Now your list includes all the single integers of your number, so you can use your sum() function