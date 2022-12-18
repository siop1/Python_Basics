# WAP to input eight numbers from user and display all unique numbers

# approach to solve who know about loop
_set=set() # empty set

for i in range(8):
    num=int(input('Enter a number: '))
    _set.add(num)

print(_set)

# if you don't know about loops yet then make a separate 8 variables to take user input eight times
