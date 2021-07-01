'''
EQUIVALENCE PARTIONING
A program computes the ABSOLUTE DIFFERENCE between the 
squares where a,b lies in range [1,10] 
Abs Diff= mod (a^2 -b^2) = (max(a,b))^2 - (min(a,b))^2
a :[1,10]   b :[1,10]
VALID EQUIVALENCE CLASSES :
I1-> a :[1,10]
I2-> b :[1,10]

INVALID EQUIVALENCE CLASSES :
I3-> a<1
I4-> a>10
I5-> b<1
I6-> b>10
'''


class Error(BaseException):
    pass


class OutOfRangeError(Error):
    def __init__(self, message):
        self.message = message


class NotEvenError(Error):
    def __init__(self, message):
        self.message = message


def checkRange(a, b):
    if a < 1 or a > 10 or b < 1 or b > 10:
        raise OutOfRangeError('Numbers are out of range')


def absVal(a, b):
    checkRange(a, b)
    if a > b:
        return (a * a) - (b * b)
    else:
        return (b * b) - (a * a)
