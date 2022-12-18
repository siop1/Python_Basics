'''
Create a class vector_2d and use it to create another class representing a 3d vector.
'''

class Vector_2d:
    i=10
    j=6

class Vector_3d(Vector_2d):
    k=20
    
    def get_vector(self):
        print(f'{self.i}i + {self.j}j + {self.k}k')

v=Vector_3d()
v.get_vector()