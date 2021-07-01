# importing the modules
import pytest
from Vehicle import Car, Truck, Motorcycle
from datetime import date


class Test_CAR:
    def test_details(self):
        h = Car('Verna', 4)
        print("testing details : Car")
        assert ('Verna', 4, 15) == (h.name, h.tyres_count, h.years_allowed)

    def test_EndDate(self):
        h = Car('AUDI', 4)
        print("testing Ending Date : Car")
        EndDate = h.getEndingDate(date(2020, 1, 23))
        assert EndDate == date(2035, 1, 23)


class Test_TRUCK:
    def test_details(self):
        t = Truck('Mahindra Truxo', 18)
        print("testing details : Truck")
        assert ('Mahindra Truxo', 18, 20) == (t.name, t.tyres_count,
                                              t.years_allowed)

    def test_EndDate(self):
        t = Truck('Tiger', 20)
        print("testing Ending Date : Truck")
        EndDate = t.getEndingDate(date(2020, 2, 20))
        assert EndDate == date(2040, 2, 20)


class Test_MOTORCYCLE:
    def test_details(self):
        m = Motorcycle('Royal Enfield Bullet 350', 2)
        print("testing details : Motorcycle")
        assert ('Royal Enfield Bullet 350', 2, 15) == (m.name, m.tyres_count,
                                                       m.years_allowed)

    def test_EndDate(self):
        m = Motorcycle('Royal Enfield Bullet 350', 2)
        print("testing Ending Date : Motorcycle")
        EndDate = m.getEndingDate(date(2018, 12, 17))
        assert EndDate == date(2033, 12, 17)
