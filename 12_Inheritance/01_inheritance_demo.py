'''
Inheritance is a way of creating a new class from an existing class
'''

# Base class
class BaseClass:
    def greet(self):
        print("Good morning")

# Derived or Child class
class ChildClass(BaseClass):
    def intro(self):
        print("I am anonymous")

    # run with greet function below and run without this and see the difference you will found that if base and child class has same attribute then child class attributes get first priority

    # def greet(self):
    #     print("Good afternoon")

b=BaseClass()
b.greet()

c=ChildClass()
c.greet() # I am inherited from BaseClass
c.intro() # I am attribute of ChildClass
