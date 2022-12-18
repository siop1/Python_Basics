'''
classmethod is used to change class attributes from object.
'''
# we couldnot change class attribute from object but it could only change instance attribute
class Employee1:
    salary=2000

    def change_salary(self,sal):
        self.salary=sal

# e=Employee1()
# print(e.salary)
# e.change_salary(5000)
# print(e.salary)
# print(Employee1.salary)  

# We can change class attribute from object using two methods
# 1. __class__
# 2. @classmethod

class Employee2:
    salary=2000

    # first method
    def change_salary1(self,sal):
        self.__class__.salary=sal

     # second method
    @classmethod
    def change_salary2(cls,sal):
        cls.salary=sal   

e=Employee2()
print(e.salary)
e.change_salary2(5000)
print(e.salary)
print(Employee2.salary)
