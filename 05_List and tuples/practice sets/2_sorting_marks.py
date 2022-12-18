# WAP to accept marks of 6 students and display in sorted manner

# We can make this problem short and easier using loop
# marks=[]
# for i in range(0,6):
#     user=input("Enter the marks: ")
#     marks.append(int(user))

# marks.sort()
# print(marks)

# Since we donot have learned loop yet we have used long way to solve this problem
m1=int(input("Enter mark of student 1: "))
m2=int(input("Enter mark of student 2: "))
m3=int(input("Enter mark of student 3: "))
m4=int(input("Enter mark of student 4: "))
m5=int(input("Enter mark of student 5: "))
m6=int(input("Enter mark of student 6: "))

_marks=[m1,m2,m3,m4,m5,m6]
_marks.sort()
print(_marks)