'''
Base class == Parent class
Derived class == Child class
'''
# super() can be used to run the methods of base class.
class Parent:
    def intro(self):
       print('I am from Parent Class')

class Child1(Parent):
    def intro(self):
        print("I am from Child1")

class Child2(Child1):
    def intro(self):
        # super() can be used to run the methods of base class.
        super().intro()
        print("I am from Child2")

# Object of Child1 Class
c2=Child2()
c2.intro()