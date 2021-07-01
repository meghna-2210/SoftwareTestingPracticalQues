# OBJECT ORIENTED
# PARENT CLASS ->                       VEHICLE                             ->(-getEndingDate())
#                            |               |                |
#CHILD CLASSES->            CAR            TRUCK           MOTORCYCLE         ->(+name,
#                                                                                +years_allowed,
#                                                                                +tyres_count,
#                                                                                -getEndingDate())
#

# importing the modules
from datetime import date
from dateutil.relativedelta import relativedelta

# base class


class Vehicle:

    name = ""

    # printing the class in the constructor
    def __init__(self):
        print("I AM THE SUPER CLASS - VEHICLE")

    def getEndingDate():

        print("Vehicle Expiry date is:")
        pass


# derived class 1
class Car(Vehicle):

    #tyres_count = 4
    years_allowed = 15

    # constructor - initializing variables
    def __init__(self, name, tyres_count):
        self.name = name
        self.tyres_count = tyres_count

    # prints the product details
    def printDetails(self):
        print("name : " + self.name)
        print("tyres_count : " + str(self.tyres_count))
        print("End_date : " + str(self.years_allowed) + "years")

# calculates the expiry date using relativedelta library and returns

    def getEndingDate(self, registration_date):
        endDate = registration_date + relativedelta(years=self.years_allowed)
        return endDate


# derived class 2
class Truck(Vehicle):

    #tyres_count = 18
    years_allowed = 20

    # constructor - initializing variables
    def __init__(self, name, tyres_count):
        self.name = name
        self.tyres_count = tyres_count

# prints the Bevertyres_count product details

    def printDetails(self):
        print("name : " + self.name)
        print("tyres_count : " + str(self.tyres_count))
        print("Expiry_date : " + str(self.years_allowed) + "years")

    def getEndingDate(self, registration_date):
        endDate = registration_date + relativedelta(years=self.years_allowed)
        return endDate


# derived class 3
class Motorcycle(Vehicle):

    #tyres_count = 2
    years_allowed = 15

    # constructor - initializing variables
    def __init__(self, name, tyres_count):
        self.name = name
        self.tyres_count = tyres_count

# prints the Staples product details

    def printDetails(self):
        print("name : " + self.name)
        print("tyres_count : " + str(self.tyres_count))
        print("Expiry_date : " + str(self.years_allowed) + "years")


# calculates the expiry date using relativedelta
# library and returns

    def getEndingDate(self, registration_date):
        endDate = registration_date + relativedelta(years=self.years_allowed)
        return endDate


def main():
    c = Car('Lamborghini Veneno Roadster', 4)
    c.printDetails()
    print(c.name + " will run on road till " +
          str(c.getEndingDate(date(2019, 10, 3))) + "years")

    a = Vehicle()

    t = Truck('Mahindra Truxo', 18)
    t.printDetails()
    print(t.name + " will run on road till " +
          str(c.getEndingDate(date(2020, 1, 23))) + "years")

    m = Motorcycle('Royal Enfield Bullet 350', 2)
    m.printDetails()
    print(m.name + " will run on road till " +
          str(m.getEndingDate(date(2018, 12, 17))) + "years")


if __name__ == '__main__':
    main()
