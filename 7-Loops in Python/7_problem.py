#Write a program to print the star *
# *
# ***
# *****

n =int(input("Enter the value of n:"))

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

    

