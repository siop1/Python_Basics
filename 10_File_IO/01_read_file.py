f=open('read.txt','r')
# f=open("10_File_IO\read.txt")# by default mode is r
content=f.read()
print(content)
f.close()