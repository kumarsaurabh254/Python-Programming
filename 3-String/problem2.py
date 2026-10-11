#Write a progrsm to fill in a letter template given below with name and date


letter = '''Dear <|Name|>
            You are selected!
            <|Date|>
'''
print(letter.replace("<|Name|>","Saurabh kumar").replace("<|Date|>","19 April 2006"))#by using the sting.replace function
#chaning of replace function

# print(letter.replace("<|Date|>","19 April 2006"))