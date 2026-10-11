#write a python to print the contents of  a directory using os module.
#search online for the function which does not

import os

directory = "."

for item in os.listdir(directory):
    print(item)