'''
a= "A very long string with email"

RAM -> volatile-- temporary stored
HDD-> Non volatile -> permanent store

file are 2 type
1 -> text.files(.txt,.c,.py, etc..)
2 -> Binary file(.jpg,.dat, etc...)

'''

f = open("9-file input and output/file.txt", "r")# this is to be done because 

data = f.read()
print(data)

f.close()

# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()