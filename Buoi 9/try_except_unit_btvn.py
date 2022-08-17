import math
class Vector():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def magnitude(self):
        result_mag = math.sqrt((self.x) ** 2 + (self.y) ** 2)
        return "{:.2f}".format(result_mag)
    def unit(self):
        mag = (self.magnitude())
        if mag == 0:
            print("Cannot convert zero vector to a unit vector")
        elif float(mag) > 0 or float(mag) < 0:
            return Vector(self.x / float(mag), self.y / float(mag))

if __name__ == '__main__':
    v1 = Vector(0, 0)
    v2 = Vector(1.1, 10 / 3)
    v1.magnitude()
    a = v1.unit()
    print(a)
    #try except at main