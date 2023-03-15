# name = input("Enter your name : ")
# print ("Good morning, " + name)

letter = '''dear  <|NAME|>,

greetings from ABC ltd. i am Happy to infrom you about selection

you are selected !

Have  a nice Day

Thanks
ABC ltd
Date: <|DATE|>
'''
name = input("Enter name : ")
date = input("Enter date : ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

# doublespaces = letter.find("  ")
# print(doublespaces) # to fine double spaces in letter