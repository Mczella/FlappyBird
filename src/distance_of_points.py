from math import sqrt


def distance(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]

    return sqrt(dx ** 2 + dy ** 2)
