'''
Create a class Employee and add salary and increment properties to it.
Write a method salary_after_increment method with a @property decorator with a setter which changes the value of increment based on the salary.
'''

class Employee:
    salary=1000
    increment=1.5

    @property
    def salary_after_increment(self):
        return self.salary * self.increment

    @salary_after_increment.setter
    def salary_after_increment(self,sai):
        self.increment=sai/self.salary


e=Employee()
print(e.increment)
print(e.salary_after_increment)
e.salary_after_increment=2000    
print(e.increment)
print(e.salary_after_increment)
