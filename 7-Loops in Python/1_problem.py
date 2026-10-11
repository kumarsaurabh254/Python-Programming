#Write a program to print multipliacation table of a given number using for loop.

n =int(input("Enter the number which you want to print the table:"))

for i in range(1,11):
    print(f"{n} x {i}={n*i}")
    