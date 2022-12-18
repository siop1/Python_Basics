'''
Base class == Parent class
Derived class == Child class
'''


class Parent:
    def intro1(self):
       print('I am from Parent Class')

class Child1(Parent):
    def intro2(self):
        print("I am from Child1")

class Child2(Child1):
    def intro3(self):
        print("I am from Child2")

# Object of Parent Class
p=Parent()
p.intro1()

# Object of Child1 Class
c1=Child1()
c1.intro1()
c1.intro2()

# Object of Child1 Class
c2=Child2()
c2.intro1()
c2.intro2()
c2.intro3()