class Employee:
    ''' if you don't use any parameter in method of class then you can self or @staticmethod. Both will do the same job
    '''
    def greet(self):
        print("Good morning")
    @staticmethod
    def drink():
        print("I like coffee")

    # you can use any no. of @staticmethod    
    @staticmethod
    def good_day():
        print("Have a good day")

a=Employee()
a.greet()
a.drink()
a.good_day()


