import math
class Vector():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "{:.2f}, {:.2f}".format(self.x, self.y)

    def __repr__(self):
        return repr((self.x, self.y))  # ask more

    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)

    def __eq__(self, vec):
        rd = self.x == vec.x and self.y == vec.y
        return rd

    def magnitude(self):
        result_mag = math.sqrt((self.x) ** 2 + (self.y) ** 2)
        return "{:.2f}".format(result_mag)

    def unit(self):
        mag = (self.magnitude())
        if (mag) == 0:
            raise ValueError("Cannot convert zero vector to a unit vector")
        elif float(mag) > 0 or float(mag) < 0:
            return Vector((self).x / float(mag), (self).y / float(mag))

        # try:
        #     print("magnitude for unit vector: ",mag)
        # except:
        #     raise ValueError("Cannot convert zero vector to a unit vector")
        # finally:
        #     return Vector((self).x / mag, (self).y / mag)

    def __mul__(self, vec):
        dot = self.x * vec.x + self.y * vec.y
        return dot

    def __rmul__(self, vec):
        return self.__mul__(vec)


if __name__ == '__main__':
    v1 = Vector(4, 6.4)
    v2 = Vector(1.1, 10 / 3)
    fl = 4
    num = (4 ,4)
    print("v1: ", v1.__str__())
    print("v2: ", v2.__repr__())
    print("Sum: ", v1.__add__(v2))
    st =  v1.__sub__(v2)
    print("Subtract: ", v1.__sub__(v2))
    rs = v1.__eq__(v2)
    print("Equal?: ", rs)
    print("magnitude v1: ", v1.magnitude())
    print("magnitude v2: ", v2.magnitude())
    print("Unit v1: ", v1.unit())
    print("Unit v2: ", v2.unit())
    print("Dot product (dot product yields a scalar): ", v1.__mul__(v2))
    print(v1.__rmul__(v2))

