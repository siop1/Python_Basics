'''
Can you change the self parameter inside a class to something else (say 'ram'). Try changing self to 'slf' or 'ram'. Seet the effects
'''

class Employee:
    name="Ram"
    def a(self):
        print('Hello',self.name)

    def b(ram):
        print('Hello',ram.name)

    def c(slf):
        print('Hello',slf.name)

    def greet(slf):
        print('Hi')

emp=Employee()
emp.a()
emp.b()
emp.c()
emp.greet()

# Conclusion: Yes it it possible. But we shoudn't use it as it may confuse other programmer while reading such code. So as a general rule of thumb we should use self.