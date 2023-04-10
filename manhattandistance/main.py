# This is a sample Python script.
from manhattandistance.Point import Point


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate_manhattan_distance():
    point_x = Point(1, 1)
    point_y = Point(5, 5)
    print("Manhattan distance is: {}".format(point_x.manhattan_distance(point_y)))


if __name__ == '__main__':
    calculate_manhattan_distance()
