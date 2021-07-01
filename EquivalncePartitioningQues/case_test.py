from airline_eq import *
import pytest


# For Valid Classes I1,I2,I3,I4,I5
def test1():
    assert CalcTicketPrice("Meghna", 5555555, 'P', 8, 'E') == 10000


def test2():
    assert CalcTicketPrice("Arnav", 6666666, 'G', 8, 'B') == 114000


#  For Invalid Classes


#I6
def test3():
    with pytest.raises(InvalidNameError):
        CalcTicketPrice("5Meghna", 2222222, 'p', 6, 'E')


#I7
def test4():
    with pytest.raises(OutOfRangeError):
        CalcTicketPrice("Meghna", 5, 'P', 7, 'B')


#I8
def test5():
    with pytest.raises(OutOfRangeError):
        CalcTicketPrice("Meghna", 10000000, 'S', 6, 'E')


#I9
def test6():
    with pytest.raises(OutOfRangeError):
        CalcTicketPrice("Meghna", 2222222, 'P', 0, 'B')


#I10
def test7():
    with pytest.raises(OutOfRangeError):
        CalcTicketPrice("Meghna", 2222222, 'G', 80, 'E')


#I11
def test8():
    with pytest.raises(InvalidTypeError):
        CalcTicketPrice("Meghna", 2222222, 'M', 6, 'E')


#I12
def test9():
    with pytest.raises(InvalidTypeError):
        CalcTicketPrice("Meghna", 2222222, 'P', 6, 'R')
