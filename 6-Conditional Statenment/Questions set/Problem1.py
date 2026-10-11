#Write a program to find the greatest of four number entered by the user 

a= int(input("Enter the value of a:"))
b= int(input("Enter the value of b:"))
c= int(input("Enter the value of c:"))
d= int(input("Enter the value of d:"))

if(a>b and a>c and a>d):
    print("a is greatest.",a)

elif(b>a and b>c and b > d):
    print("B is greatest.",b)

elif(c>a and c> b and c > d):
    print("C is greatest.",c)

else:
    print("D is greatest number.",d)