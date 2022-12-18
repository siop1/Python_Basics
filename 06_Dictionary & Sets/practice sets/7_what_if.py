'''
What will happen to program in problem 6 if:
1. names of 2 friends are same,
2. languages of two friends are same,  
'''

_dict={}

for i in range(0,4):
    name=input('Enter your name: ')
    lang=input("Your fav language: ")
    _dict.update({name:lang})

print(_dict)

# conclusion1: the later key:value will be considered
# conclusion2: nothing will happen

