#Write a program to convert the degree celcius to farenheit

# f=float(input("Enter the temperature in farenheit:"))

# c= 5*(f-32)/9

# print(c)

# By using the function 

f=float(input("Enter the temperature in farenheit:"))
def tempconversion(f):
    c= 5*(f-32)/9
    return c

print(tempconversion(f))