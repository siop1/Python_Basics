# WAP to sum a list with 4 numbers

l=[1,2,3,4] # list with four numbers

# first way to solve
_sum=l[0]+l[1]+l[2]+l[3]
print(_sum)

# second and best way to solve
print(sum(l)) # sum() is used to find sum of numbers in a list

# third way to solve using loop
_sum=0
for i in range(0,4):
    _sum=_sum+l[i]
print(_sum)
