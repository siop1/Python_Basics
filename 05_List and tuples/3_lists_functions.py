# here we will see some of the functions or methods of lists
# for more functions you can search online on how to use them
# list functions can change the original list value
_list=[True,False]
_list=['one','two','four']
_list=[1,2,True,"Hello",'man']
_list=[1,2,9,3]

# for sorting, list should contain value of similar datatype
# for ex: _list=[1,2,3] or _list=['one','two'] or _list=[True,False]
# note: if you use mix datatypes value it will throw error

_list.sort() # sort in ascending order
# _list.reverse() # changes value from last to first
# _list.append(5) # adds 5 to the end of list
# _list.insert(3,9) # inserts 9 at index 3 without changing previous data
# _list.pop(0) # deletes element at index 0 
# _list.remove(5) # removes 5 that comes first from list and if there is not
                # not any 5 then throws an error
# _list.clear() # clears all data from list 
print(_list)

print(sum(_list)) # sum method is used to find sum of numbers of list

# uncomment and run every function one by one 
# and also try to run sort() function with:
# string types like  _list=['one','two','four']
# boolean types like _list=[True,False]
# mixed datatypes like _list=[1,2,True,"Hello",'man'] and see the error