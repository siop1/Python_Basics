# WAP to fill in a letter template given below with name and date entered by user
# letter=''' Dear <NAME>,
#                 You are selected !
#                 Date: <DATE>'''

letter=''' Dear <NAME>,
                You are selected !
                Date: <DATE>'''

name=input("Enter the name: ")
date=input("Enter the date: ")
letter=letter.replace("<NAME>",name)
letter=letter.replace("<DATE>",date)
print(letter)