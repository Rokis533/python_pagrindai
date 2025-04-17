from .helper import get_pi_number as pi
from ..test_module import *

def suma(x, y):
    return x + y

def division(x,y):
    if y == 0:
        print("Dalyba is nulio negalima")
        return None
    return x / y

def circle_area(radius):
    return (2 * pi() * radius) ** 2


