__a = 7
__b = 2
__c = 8


def triangle_perimeter(a: int = __a, b: int = __b, c: int = __c):
    return a + b + c


def triangle_area(a: int = __a, b: int = __b, c: int = __c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
