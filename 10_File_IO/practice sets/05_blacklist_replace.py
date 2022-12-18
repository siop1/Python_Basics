'''
Repeat program 4 for a list of such words to be cesored.
'''
blacklist=['donkey','monkey','dog','kutta','boka']
with open('04_replace.txt','r') as f:
    data=f.read()

for word in blacklist:
    data=data.replace(word,'%$^#%@%$$')
    with open('04_replace.txt','w') as f:
        f.write(data)