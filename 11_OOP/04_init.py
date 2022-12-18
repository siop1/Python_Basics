class Employee:
    # it runs automatically after object is created
    # def __init__(self):
    #     print("I run automatically as soon as object is created")
    name='hari'
    def __init__(self, name):
        print(f"I am {name} ")
        print(f"I am {self.name} ")
    def greet(self):
        print("Good morning")

    @staticmethod
    def drink():
        print("I like coffee")

a=Employee("Anonymous")



