'''
Recursion -> Recursion in function that calling itself
'''

#Factorial by recursion

n =int (input("Enter the number:"))

def fact(n):
    if(n==1 or n==0):
        return 1 
    else:
        return n * fact(n-1)
print(f"The factorial of a given number is:{fact(n)}")
print(fact(n))
       