thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 196,
}

# printing dictionary keys and values separately
a=thisdict.keys()
b=thisdict.values()
c=thisdict.items()
thisdict.update({'color':'red'}) # updates dictionary with color:red
e=thisdict.get('brand') # You may ask if thisdict['brand'] is equivalent to it then why should i use get() functio
# if you add something like thisdict['house'] which is not in dictionary then it will throw error but get() don't  
print(a)
print(type(a)) # its type is dict_keys
print(b)
print(type(b)) # its type is dict_values
print(c)
print(type(c)) # its type is dict_items
print(e)
print('--------------------------')
# Example to show why to use get()
print(thisdict.get('man')) # returns none but no error
print(thisdict['man']) # it will throw error

# more methods/functions are available in docs.python.org


