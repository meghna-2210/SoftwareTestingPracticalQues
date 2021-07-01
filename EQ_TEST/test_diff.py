from diff_sq import *
import pytest


# For Valid Classes I1,I2
def test_nominal():
    assert absVal(5, 5) == 0


# For Invalid Classes
#I3
def test_minm_a():
    with pytest.raises(OutOfRangeError):
        absVal(0, 5)


    #I4
def test_maxp_a():
    with pytest.raises(OutOfRangeError):
        absVal(11, 6)


    #I5
def test_minm_b():
    with pytest.raises(OutOfRangeError):
        absVal(4, 0)


    #I6
def test_maxp_b():
    with pytest.raises(OutOfRangeError):
        absVal(7, 11)
