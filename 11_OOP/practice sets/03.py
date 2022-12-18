'''
Create a class witha a class attribute 'a'; create an object from it and set 'a' directly using object a=0. Does this change the class attribute ?
'''

# Lets' see this practically

class Employee:
    a='ram'
    def get_a(self):
        print(self.a)

first=Employee()
first.a=0
first.get_a() # 0

# 1st way to check
second=Employee()
second.get_a() # ram

# 2nd way to check
print(Employee.a)

# but if i do something like this then it will change class attribute a
Employee.a=0

# 1st way to check
second=Employee()
second.get_a() # ram

# 2nd way to check
print(Employee.a)

# conclusion: it changes only instance attribute for first
