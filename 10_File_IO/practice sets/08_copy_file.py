# WAAP to make a copy of a text file 'this.txt'
with open('08_this.txt','r') as f:
    data=f.read()

with open('08_copied.txt','w') as f:
    f.write(data)