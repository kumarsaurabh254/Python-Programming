# Create the empty dictionary.Allow 4 friends to enter their favourite language as value and use keys
# as their names.Assume that the name are unique.

dic={}  # empty dictionary

Friend1 =input("Enter friend 1 name:")
dic[Friend1] = input("Enter your favorite language:")

Friend2 =input("Enter friend 2 name:")
dic[Friend2] = input("Enter your favorite language:")

Friend3 =input("Enter friend 3 name:")
dic[Friend3] = input("Enter your favorite language:")

Friend4 =input("Enter friend 4 name:")
dic[Friend4] = input("Enter your favorite language:")

# d.update({name:lang})
print(dic)