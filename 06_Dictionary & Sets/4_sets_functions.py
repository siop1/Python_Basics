# note one very very important thing
a={} # create empty dictionary
print(type(a))
b=set() # create empty sets
print(type(b))
b.add(2) # add 2 to set b
print(b)
print(len(b)) # print length of set b i.e no. of elements 

# Some of the functions/methods of set
# We can use this methods to empty set as well as non empty set
print('=================================')
s={1,2,9,3,4,4}
print(len(s)) # show length of set s
s.remove(2) # remove 2 from set s but return error if 2 is not present
print(s)
a=s.union({2,9,10}) # union like in set
print(a)
a=s.intersection({2,4,6,8}) # intersection like in set
print(a)
s.pop() # since set is unordered it can removes arbitary elements
print(s)
s.clear() # empties the set and return empty set i.e set()
print(s)


