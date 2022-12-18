# WAP to find greatest of four numbers entered by users.

a=int(input('Enter num: '))
b=int(input('Enter num: '))
c=int(input('Enter num: '))
d=int(input('Enter num: '))

if(a>b and a>c and a>d):
    print(a , ' is greatest')
elif(b>a and b>c and b>c):
    print(b , ' is greatest')
elif(c>a and c>b and c>d):
    print(c, ' is greatest')
else:
    print(d,' is greatest')
    
    

