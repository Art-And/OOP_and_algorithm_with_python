
class Coordinates:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance(self, other_cordinate):
        x_diff = (self.x - other_cordinate.x)**2
        y_diff = (self.y - other_cordinate.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_one = Coordinates(50, 3)
    coord_two = Coordinates(20, 52)

    print(coord_one.distance(coord_two))
    print(isinstance(coord_two, Coordinates))