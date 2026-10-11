#Write a program to find out wheather a student has passed or failed
#if it is required a total of 40% and atleast 33% in each subject to pass.Assume 
#3 subject and take marks as an input from the user

sub1=float(input("Enter the marks of subject 1:"))
sub2=float(input("Enter the marks of subject 2:"))
sub3=float(input("Enter the marks of subject 3:"))

sum = sub1 +sub2 + sub3
print("The marks obtained by student out of 300 is:",sum)

total = 300
percentage=(sum/total)*100

print("The total percentage of student is:",percentage)

per1=(sub1/100)*100
per2=(sub2/100)*100
per3=(sub3/100)*100

if(per1 >= 33):
    print("Student pass in subject 1.",per1)

else:
    print("Student is fail in subject 1",per1)
if(per2 >= 33):
    print("Student pass in subject 2.",per2)

else:
    print("Student is fail in subject 2",per2)


if(per3 >= 33):
    print("Student pass in subject 3.",per3)

else:
    print("Student is fail in subject 3",per3)

if(percentage >= 40 and per1>= 33 and per2 >= 33 and per3>= 33):
    print("Student has passed the exam.",percentage)

else:
    print("Student has failed the exam.",percentage)

