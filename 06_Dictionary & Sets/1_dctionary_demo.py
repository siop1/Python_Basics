# Dictionary are in the form of key:value pair
# Duplicate values are not allowed but if you put duplicates then no error is thrown rather first duplicate value is removed
# automatically
# items can be reassigned
# dictionary can contain any values. main thing is that they should contain key value pair
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "status":True,
  'gpa':3.5,
  "year": 196,
  "year": 1960,
  "list":[1,2,3],
  "tuple":(2,3),
  "another_dict":{'hello':'hi'},
  "set":{1,2,3}
}
# first duplicate is replaced by later on in this case year=196 is override by 1960 and again override by reassigned
thisdict['year']=6
# append can be done
thisdict['cat']='dog'
print(thisdict)

# note: although automatically repeated values are removed it is not good habit to put multiple value on
# dicionary. Think yourself do you get mutliple words with same name in dictionary so dont make it messy

# one more thing
a={} # empty dictionary
print(a)
print(type(a))