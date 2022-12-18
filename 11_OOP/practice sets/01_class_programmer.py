'''
Create a class programmer for storing information of few programmers working at microsoft.
'''

class Programmer:
    company='Microsoft'
    def __init__(self, name, age, language):
        print(f'Name: {name}')
        print(f'Age: {age}')
        print(f'Language: {language}')
        print(f'Company: {self.company}')
        print("\n")

hari=Programmer('Hari',20,'python')
ram=Programmer('Ram',22,'java')
shyam=Programmer('Shyam',19,'php')

