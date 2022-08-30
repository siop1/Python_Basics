# Slicing is the act of taking a certain part of the given string
# note: indexing start from and first element of string has index 0
'''
                            a   p   p   l   e
 positive index:            0   1   2   3   4
 negative index:           -5  -4  -3  -2  -1

 both type of index is valid 
 '''
a="apple"
b=a[0] # first index
# a[0]="m" --> this will not work bcoz you cannot change string value like this
c=a[-5] # this is also first index
d=a[4] # this is last index
e=a[-1] # this is also last index. When we dont know the length of string then we cant know its last index
# so we can use negative index -1 for last index

f=a[0:3] # it will start from 0 to 2 and doesnot include index 3
g=a[0:] # automatically start from given index to remaining index (same as a[0:5])
h=a[1:] # automatically start from given index to remaining index (same as a[1:5])
i=a[:4] # automatically start from 0 (same as a[0:4])
j=a[-3:-1] # same as a[2:4]

print(a) # gives apple
print(b) # gives a
print(c) # gives a
print(d) # gives e
print(e) # gives e
print(f) # gives app
print(g) # gives apple
print(h) # gives pple
print(i) # gives appl
print(j) # gives pl

# run this program and try to practice and understand...
