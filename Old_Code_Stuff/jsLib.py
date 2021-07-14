import random


def constrain(n, low, high):
    if type(n) == int:
        return min(high, max(low, n))
    elif type(n) == iter:
        nl = []
        for x in n:
            x = min(high, max(low, x))
            nl.append(x)
        return nl
    elif type(n) == Vector:
        n.x = min(float(high), max(float(low), n.x))
        n.y = min(float(high), max(float(low), n.y))
        return Vector(n.x, n.y)


def standardD(lst):
    m = mean(lst)
    distance = [abs(x - m) ** 2 for x in lst]
    return (sum(distance) / len(lst)) ** 0.5


def sumL(lst):
    num = 0
    for n in lst:
        num += n
    return num


def mean(lst):
    m = 0
    for x in lst:
        m += x
    return m / len(lst)


def setColor(x1=0, x2=0, x3=0):
    return x1, x2, x3


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Returns Vector to string type:
    def __repr__(self):
        return str([self.x, self.y, self.z])

    # Set new Vector values:
    def set(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def copy(self):
        return Vector(self.x, self.y, self.z)

    def __add__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        if type_1 is type_2:
            x += other.x
            y += other.y
            z += other.z
        elif type_2 is int or type_2 is float or type_2 is complex:
            x += other
            y += other
            z += other
        else:
            err = "Cannot add types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)

        return Vector(x, y, z)

    def __radd__(__add__, other):
        return __add__

    def __mod__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        if type_1 is type_2:
            x = x % other.x
            y = y % other.y
            z = z % other.z
        elif type_2 is type(int) or type_2 is type(float) or type_2 is type(complex):
            x += other
            y += other
            z += other
        else:
            err = "Cannot use modulo on types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)

        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        if type_1 is type_2:
            x -= other.x
            y -= other.y
            z -= other.z
        elif type_2 is int or type_2 is float or type_2 is complex:
            x -= other
            y -= other
            z -= other
        else:
            err = "Cannot subtract types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)

        return Vector(x, y, z)

    def __mul__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        if type_1 is type_2:
            x *= other.x
            y *= other.y
            z *= other.z
        elif type_2 is int or type_2 is float or type_2 is complex:
            x *= other
            y *= other
            z *= other
        else:
            err = "Cannot multiply types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)

        return Vector(x, y, z)

    def __rmul__(__mul__, other):
        return __mul__

    def __truediv__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        try:
            if type_1 is type_2:
                x /= other.x
                y /= other.y
                z /= other.z
            elif type_2 is int or type_2 is float or type_2 is complex:
                x /= other
                y /= other
                z /= other
            else:
                err = "Cannot divide types " + str(type_1) + " and " + str(type(type_2)) + " together."
                raise TypeError(err)
        except ZeroDivisionError:
            return Vector(x, y, z)
        return Vector(x, y, z)

    def __pow__(self, power):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(power)

        if type_1 is type_2:
            x = x ** power.x
            y = y ** power.y
            z = z ** power.z
        elif type_2 is int or type_2 is float or type_2 is complex:
            x = x ** power
            y = y ** power
            z = z ** power
        else:
            err = "Cannot use exponent on types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)

        return Vector(x, y, z)

    def __lt__(self, other):
        x = self.x
        y = self.y
        z = self.z
        type_1 = type(self)
        type_2 = type(other)

        if type_1 is type_2:
            if x < other.x and y < other.y and z < other.z:
                return True
            else:
                return False
        elif type_2 is int or type_2 is float or type_2 is complex:
            if x < other and y < other and z < other:
                return True
            else:
                return False
        else:
            err = "Cannot use exponent on types " + str(type_1) + " and " + str(type(type_2)) + " together."
            raise TypeError(err)


    def mag(self):
        vm = (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
        return vm

    def magSq(self):
        pass

    def dot(self):
        pass

    def cross(self):
        pass

    def dist(self):
        pass

    def normalize(self):
        mag = Vector.mag(self)
        self /= mag
        return self

    def limit(self, maximum=0):
        result = constrain(self, maximum*-1, maximum)
        return result

    def setMag(self, mag=1):
        result = self.normalize().mult(mag)
        return result

    def heading(self):
        pass

    def setHeading(self):
        pass

    def rotate(self):
        pass

    def angleBetween(self):
        pass

    def lerp(self):
        pass

    def reflect(self):
        pass

    def array(self):
        pass

    def equals(self):
        pass

    def fromAngle(self):
        pass

    def fromAngles(self):
        pass

    @staticmethod
    def random2D():
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        result = Vector(x, y).normalize()
        return result

    def random3D(self):
        pass
