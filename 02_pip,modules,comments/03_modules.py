''' Module is a file that contains the python code made by other people.It is used to make our 
programmng faster and easier. If someone has already made our job easier then there is 
no sense to write the same program

Types of modules:
1. Built in module -- pre installed in python
These modules are already developed by creator of python

2. External module -- need to be installed using pip
These modules are developed by other programmers like you and me.

We can make our own module and import it to use it. 
Inorder to use the external module we have to download it first then import it.'''

import platform # importing module name platform. No need to download this as it is built in module
x = platform.system() # store value of system in x
print(x) # print the value of x in console

# if you don't want to import whole module but want just a function of module. use this:

# from module_name import function_name 
# x=function_name()
# print(x)

# for ex:lets take platform module
from platform import system
x=system()
print(x)

# If you want to give alias to your module while importing then again consider previous example as:

import platform as pl # you can give any alias like pl,cat ,dog,etc.
x=pl.system()
print(x) 

# All the above three example do the same thing

"""You can also import all functions inside a module like this:
from platform import * 
x=system()
print(x)

But this is not a good idea if we use multiple modules because they may have same functions name
for ex: if two modules contain same function name like add() then compiler will be confused which add() function
we are talking about.""" 

