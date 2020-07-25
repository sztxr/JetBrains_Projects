# the variable "args" is already defined
# my_list = list(map(int, args[1:]))
my_list = [int(arg) for arg in args[1:]]
print(str(my_list))
