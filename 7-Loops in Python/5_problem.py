#Write a program to print the sum of first n natural number 

n=int(input("Enter the value of n:"))


i=1
sum =0 

while(i<=n):
    
        sum= sum +i
        i+=1

print("The sum of first n natural number is ")
print(sum)    


#sum of n natural number using for loop

n=int(input("Enter the value of n:"))

sum = 0
i=1 

for i in range(i,n+1):
        sum =sum + i 
        i+=1

print(sum)

        