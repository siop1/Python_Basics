'''
Write a class calculator capable  of finding square, 
cube and square root of a number.
'''
# 1st method
class Calculator1:
    def square(self,num):
        print(f"Square of {num} is {num**2}")
    def cube(self,num):
        print(f"Cube of {num} is {num**3}")
    def square_root(self,num):
        print(f"Square root of {num} is {num**0.5}")

a=Calculator1()
num=4
print("1st method: ")
a.square(num)
a.cube(num)
a.square_root(num)
print("\n")

# 2nd method
class Calculator2:
    def __init__(self,num):
        self.num=num
    def square(self):
        print(f"Square of {self.num} is {self.num**2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num**3}")
    def square_root(self):
        print(f"Square root of {self.num} is {self.num**0.5}")

print("2nd method: ")
a=Calculator2(4)
a.square()
a.cube()
a.square_root()