f=open('write.txt','w')
f.write("I am a good boy cat gun fan")
f.close()


f=open('write.txt','r')
data=f.read()
print(data)
f.close()