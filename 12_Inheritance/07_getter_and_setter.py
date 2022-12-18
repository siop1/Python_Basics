'''
@property is used as getter.It is used when we want to treat method as attribute
'''
class Employee1:
    salary=5000
    bonus=1000

    @property
    def total_salary(self):
        return self.salary + self.bonus

e1=Employee1()
print(e1.total_salary)

'''
If we want to do something like this in above program
e.total_salary=8000 then this will give an error

So when we use getter to use methods as property then we must use setter to change its like normal attribute.
'''

class Employee2:
    salary=5000
    bonus=1000

    @property
    def total_salary(self):
        return self.salary + self.bonus

    @total_salary.setter
    def total_salary(self,val):
        self.salary=val-self.bonus


    

e2=Employee2()
print(e2.total_salary)
e2.total_salary=8000
print(e2.total_salary)