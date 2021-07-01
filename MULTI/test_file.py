from function_file import *
import pytest
"""
calculating MULTIPLICATION(a,b) 
Range of a: [1,10]
Range of b: [1,5]
Use of ROBUST TESTING :6*n + 1 test cases 
            i.e 6(2)+1=13 test cases
            
"""


#1
def test_robust_minimum_minus_A():
    with pytest.raises(OutOfRangeError):
        multi(0, 3)


#2
def test_robust_minimum_A():
    assert multi(1, 3) == 3


#3
def test_robust_minimum_positive_A():
    assert multi(2, 3) == 6


#4
def test_robust_maximum_minus_A():
    assert multi(9, 3) == 27


#5
def test_robust_maximum_A():
    assert multi(10, 3) == 30


#6
def test_robust_maximum_positive_A():
    with pytest.raises(OutOfRangeError):
        multi(11, 3)


#7
def test_robust_minimum_minus_B():
    with pytest.raises(OutOfRangeError):
        multi(5, 0)


#8
def test_robust_minimum_B():
    assert multi(5, 1) == 5


#9
def test_robust_minimum_positive_B():
    assert multi(5, 2) == 10


#10
def test_robust_maximum_minus_B():
    assert multi(5, 4) == 20


#11
def test_robust_maximum_B():
    assert multi(5, 5) == 25


#12
def test_robust_maximum_positive_B():
    with pytest.raises(OutOfRangeError):
        multi(5, 6)


#13
def test_robust_nominal():
    assert multi(5, 3) == 15
