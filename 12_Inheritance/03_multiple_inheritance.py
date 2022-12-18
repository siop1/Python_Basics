class BaseClass1:
    def intro(self):
        print("I am from BaseClass1")
    def health(self):
        print('Health is good')

class BaseClass2:
    def intro(self):
        print("I am from BaseClass2")
    
    
# Single inheritance
class ChildClass(BaseClass2, BaseClass1): # first parent class get more priority
    def greet(self):
        print("Good morning")
    # def intro(self):
    #     print("I am from ChildClass")

a=ChildClass()
a.greet()
a.intro()
a.health()

'''
In inheritance the attributes and methods get priority as below.
child class > first parent class in child class argument> second parent clas ....ss 
'''