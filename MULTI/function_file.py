class Error(BaseException):
    pass


class OutOfRangeError(Error):
    def __init__(self, message):
        self.message = message


def checkRange(a, b):
    if a < 1 or a > 10 or b < 1:
        raise OutOfRangeError('num is out of the given range')


def multi(a, b):
    checkRange(a, b)
    return a * b
