'''
WAP to read the text from a given file 'poems.txt' and find out whether
it contains the word 'twinkle'.

'''

with open('01_poems.txt','r') as f:
    data=f.read()
print(data)
# first approach with find()
a=data.find('twinkle')
if a>=0:
    print('present')
else:
    print('not present')

# second approach with in
if 'twinkle' in data:
    print('present')   
else:
    print("not present") 
    