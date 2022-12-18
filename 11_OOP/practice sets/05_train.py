'''
Write a class Train chich has methods to book a ticket, get status [no. of seats] and get fare information of trains running under Nepalese Railways.
'''

class Train:
    seats=20
    def book_ticket(self):
        if self.seats>0:
            print('Ticket is booked successfully')
            self.seats=self.seats-1
        else:
            print('Sorry,the train is full')
    def get_status(self):
        print(f"No. of seats available is {self.seats}")
    def get_fare_info(self):
        print('Chormara to Bharatpur: 200 rupees')
        print('Kathmandu to Jhapar: 2000 rupees')
        print('Surkhet to Pokhara: 1500 rupees')

a=Train()
a.book_ticket()
a.book_ticket()
a.get_status()
a.get_fare_info()
print('*****************')

b=Train()
b.get_status()