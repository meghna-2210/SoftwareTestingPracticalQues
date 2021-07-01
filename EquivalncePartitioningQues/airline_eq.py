'''
EQUIVALENCE PARTIONING

'''
import math


class Error(BaseException):
    pass


class OutOfRangeError(Error):
    def __init__(self, message):
        self.message = message


class InvalidTypeError(Error):
    def __init__(self, message):
        self.message = message


class InvalidNameError(Error):
    def __init__(self, message):
        self.message = message


def checkRange(Memb_ID, Ticket_Count):
    if Ticket_Count < 1 or Ticket_Count > 10:
        raise OutOfRangeError('Ticket Count is out of the given range')
    if Memb_ID < 1111111 or Memb_ID > 9999999:
        raise OutOfRangeError('Membership ID is out of the given range')


def isValidName(Cust_Name):
    if Cust_Name[0:1].isalpha() != True:
        raise InvalidNameError('Invalid Name, should be alpha at start')


def isValidMembType(Memb_Type):
    if Memb_Type != "P" and Memb_Type != "G" and Memb_Type != "S":
        raise InvalidTypeError('Invalid Memb_Type , should be : P or G or S')


def isValidTicketType(Ticket_Type):
    if Ticket_Type != "E" and Ticket_Type != "B":
        raise InvalidTypeError('Invalid Ticket_Type , should be : E or B ')


def CalcTicketPrice(Cust_Name, Memb_ID, Memb_Type, Ticket_Count, Ticket_Type):
    checkRange(Memb_ID, Ticket_Count)
    isValidName(Cust_Name)
    isValidMembType(Memb_Type)
    isValidTicketType(Ticket_Type)
    Initial_price = 0
    if (Ticket_Type == 'B'):
        Initial_price = 15000 * Ticket_Count
    elif (Ticket_Type == 'E'):
        Initial_price = 15000 * Ticket_Count

    if (Memb_Type == 'P'):
        Initial_price -= 0.1 * Initial_price
    elif (Memb_Type == 'G'):
        Initial_price -= 0.05 * Initial_price
    elif (Memb_Type == 'S'):
        Initial_price -= 0.03 * Initial_price

    if (Initial_price > 500000 and Memb_Type == 'P'):
        Initial_price -= 0.05 * Initial_price

    return Initial_price


# if __name__ == "__main__":
#     try:
#         Cust_Name = input(input('Enter name (must start with alpha):'))
#         Memb_ID = int(input('Enter price (between 1111111 & 9999999): '))
#         Ticket_Count = int(input('Enter no of tickets (between 1 and 10): '))
#         Memb_Type = input('enter type of member (P , G , S): ')
#         Ticket_Type = input('Enter ticket type (E,B): ')
#     except ValueError as v:
#         print(v + " Raised :Input is not an integer.")
#         exit(0)
#     try:
#         checkRange(Memb_ID, Ticket_Count)
#     except OutOfRangeError as e:
#         print("Out of range error: " + e.message)
#     try:
#         isValidMembType(Memb_Type)
#     except InvalidTypeError as e:
#         print("Invalid  Type Error: " + e.message)
#     try:
#         isValidName(Cust_Name)
#     except InvalidNameError as i:
#         print("Invalid Name: " + e.message)
# # try:
# #     isValidTicketType(Ticket_Type)
# # except InvalidTypeError as t:
# # 	print("Invalid  Type Error: " + t.message)
#     totalPrice = CalcTicketPrice(Cust_Name, Memb_ID, Memb_Type, Ticket_Count,
#                                  Ticket_Type)
#     print("Total price = " + str(totalPrice))
