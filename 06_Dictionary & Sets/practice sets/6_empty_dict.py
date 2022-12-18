'''
Create an empty dictionary. Allow 4 friends to enter
their favourite language as values and use keys as their
name. Assume that the names are unique.
'''
_dict={}

for i in range(0,4):
    name=input('Enter your name: ')
    lang=input("Your fav language: ")
    _dict.update({name:lang})

print(_dict)
