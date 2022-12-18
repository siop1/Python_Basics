class BaseClass:
    def intro(self):
        print("I am from BaseClass")
    
# Single inheritance
class ChildClass(BaseClass):
    def greet(self):
        print("Good morning")

a=ChildClass()
a.greet()
a.intro()