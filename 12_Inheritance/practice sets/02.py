'''
Create a class pets from a class Animals and further create a class Dog from Pets. Add a method bark to class Dog.
'''

class Animals:
    animal_type='Mammal'

class Pets(Animals):
    pets_type='four legged'

class Dog(Pets):

    def bark(self):
        print("vow vow !!")

a=Dog()
print(a.animal_type)
print(a.pets_type)
a.bark()

# This is called multilevel inheritance
