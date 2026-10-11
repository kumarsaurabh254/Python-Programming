#Write a program to find the number is prime nuber or not 

n=int(input("Enter the number:"))

for i in range(2,n):
    if n%i == 0:
        print("Number is not prime number.")
        break

else:
    print("Number is prime number.")
   