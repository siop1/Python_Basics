'''
WAP to find out whether a student is pass or fail, if it requires total 40 percent and atleast 33 percent in each subject to pass.Assume 3 subjects and full marks is 100 for each and take marks as input from the user.

'''
a=int(input('Enter marks in Physics: '))
b=int(input('Enter marks in Chemistry: '))
c=int(input('Enter marks in Mathematics: '))

if(a>=33 and b>=33 and c>=33 and (a+b+c)/3>=40):
    print("status: pass")
else:
    print('status:fail')