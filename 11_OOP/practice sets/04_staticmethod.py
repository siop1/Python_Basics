'''
Add a static method to problem 2 to greet the user with hello
'''
class Calculator2:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def square_root(self):
        print(f"Square root of {self.num} is {self.num**0.5}")
    @staticmethod    
    def greet():
        print('Hello')

print("2nd method: ")
a=Calculator2(4)
a.square()
a.cube()
a.square_root()
a.greet()