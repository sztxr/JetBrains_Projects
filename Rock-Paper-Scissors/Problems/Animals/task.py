# read animals.txt
# and write animals_new.txt
file = open('animals.txt', 'r')
file_copy = open('animals_new.txt', 'w')

file_copy.write(file.read().replace('\n', ' '))

file.close()
file_copy.close()
