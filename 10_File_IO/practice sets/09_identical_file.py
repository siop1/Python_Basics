# WAP to find out whether a file is identical and matches the content of another file.

with open('08_this.txt','r') as f:
    data1=f.read()

with open('08_copied.txt','r') as f:
    data2=f.read()

if data1==data2:
    print("Identical file")
else:
    print("Non identical file")