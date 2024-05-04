pi = 3.141592653589793
__default_radius = 5


def circle_perimeter(radius: int = __default_radius):
    return 2 * pi * radius


def circle_area(radius: int = __default_radius):
    return pi * radius ** 2
