'''
A file contains a word "Donkey" multiple times. You need to write  program which replaces this word with %$^#%@%$$ by updating the same file.
'''

with open('04_replace.txt','r') as f:
    data=f.read()

data=data.replace('donkey','%$^#%@%$$')
# data=data.replace('%$^#%@%$$','donkey')

with open('04_replace.txt','w') as f:
    f.write(data)