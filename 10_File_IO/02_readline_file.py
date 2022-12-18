f=open("10_File_IO//read.txt",'r')
# read first line
content=f.readline()
print(content)

# read second line
content=f.readline()
print(content)

# read third line and so on...
content=f.readline()
print(content)

f.close()