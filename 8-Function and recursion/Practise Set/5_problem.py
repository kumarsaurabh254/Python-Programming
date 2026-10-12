#Write a program to print the pattern 

def pattern(n):
    if(n==0):
        return 
    print("*"*n)
    pattern(n-1)


n =int(input("Enter the number:"))
pattern(n) #calling of function 