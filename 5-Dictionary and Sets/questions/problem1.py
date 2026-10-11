#Write a program to create a dictionary of hindi word with values as their English translation.
#provide user with an option to look it up

meaning={
    "सेब":"Apple",# first one key and other is meaning is value
    "संतरा":"Orange",
    "खरबूजा":"Muskmelon",
    "लीची":"litchi"


}
word=input("Enter the fruit name:")

print(meaning[word])
    