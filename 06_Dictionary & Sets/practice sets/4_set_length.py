# What will be the length of following set s ?
'''
s=set()
s.add(20)
s.add(20.0)
s.add("20")

'''

s=set()
s.add(20)
s.add(20.0) # it is considered as 20 so int
s.add("20")
print(len(s))

# conclusion: length is 2