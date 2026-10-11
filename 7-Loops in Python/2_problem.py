#Write a program to greet all the person names stored in a list L and which start with S

l=["Harry","Sohan","Sachin","Rahul"]

for name in l:
     if(name.startswith("S")):
          print(f"Hello {name}")