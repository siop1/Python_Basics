# Tuple is the collection of values of any datatypes inside () bracket .Its features are:
# 1. values cannot be changed
# 2. duplicates are allowed

tuple_1=() # empty tuple
tuple_2=(1,) # tuple with only one element needs comma otherwise it will be considered int type
tuple_3=("apple","got",4,"gpa",True,4) # tuple with mixed datatypes
tuple_4=(1,5,7,2) 
tuple_5=('hi','man') 
tuple_6=(True,False)
not_tuple=(1) # this is not tuple because comma is missing 


print(tuple_1,type(tuple_1))
print(tuple_2,type(tuple_2))
print(tuple_3,type(tuple_3))
print(tuple_4,type(tuple_4))
print(tuple_5,type(tuple_5))
print(tuple_6,type(tuple_6))
print(not_tuple,type(not_tuple))
