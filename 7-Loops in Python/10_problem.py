#Write a program to print the multiplication of table using the for loop in reverse order

n =int(input("Enter the number for which you want to print the multipliaction of a table:"))


print("The multiplication table in reverse order:")
for i in range(1,11):
    result=n * (11-i)

    print(f"{n}X{11-i}={result}")