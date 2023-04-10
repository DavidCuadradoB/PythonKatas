class Point:
    def __init__(self, coordinate_x, coordinate_y):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y

    def manhattan_distance(self, to):
        distance_x = abs(self.coordinate_x - to.coordinate_x)
        distance_y = abs(self.coordinate_y - to.coordinate_y)
        return distance_x+distance_y

