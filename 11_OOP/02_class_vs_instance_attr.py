class Employee:
    salary=1000 # this is class attribute

ram=Employee()
hari=Employee()

# creating instance attribute
ram.salary=200
# hari.salary=500
print(ram.salary)
print(hari.salary)


# note: instance attribute get first priority than class attribute