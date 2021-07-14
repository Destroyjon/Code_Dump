import random

class smallest_equation():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("A = {}\nB = {}".format(self.a, self.b))
        self.state = True
        self.equation = ""
    def __repr__(self):
        return self.equation
    # (A + B)
    def c1(self, operator=None):
        total = (self.a + self.b)
        if self.state and operator is None:
            self.equation += "({} + {})".format(self.a, self.b)
        elif self.state:
            self.equation += "({} + {}) {} ".format(self.a, self.b, operator)
        elif operator is None:
            self.equation += "(a:{} + b:{} = {})".format(self.a, self.b, total)
        else:
            self.equation += "(a:{} + b:{} = {}) {} ".format(self.a, self.b, total, operator)
        return total
    # (A - B)
    def c2(self, operator=None):
        total = (self.a - self.b)
        if self.state and operator is None:
            self.equation += "({} - {})".format(self.a, self.b)
        elif self.state:
            self.equation += "({} - {}) {} ".format(self.a, self.b, operator)
        elif operator is None:
            self.equation += "(a:{} - b:{} = {})".format(self.a, self.b, total)
        else:
            self.equation += "(a:{} - b:{} = {}) {} ".format(self.a, self.b, total, operator)
        return total
    # (B + A)
    def d1(self, operator=None):
        total = (self.b + self.a)
        if self.state and operator is None:
            self.equation += "({} + {})".format(self.b, self.a)
        elif self.state:
            self.equation += "({} + {}) {} ".format(self.b, self.a, operator)
        elif operator is None:
            self.equation += "(b:{} + a:{} = {})".format(self.b, self.a, total)
        else:
            self.equation += "(b:{} + a:{} = {}) {} ".format(self.b, self.a, total, operator)
        return total
    # (B - A)
    def d2(self, operator=None):
        total = (self.b - self.a)
        if self.state and operator is None:
            self.equation += "({} - {})".format(self.b, self.a)
        elif self.state:
            self.equation += "({} - {}) {} ".format(self.b, self.a, operator)
        elif operator is None:
            self.equation += "(b:{} - a:{} = {})".format(self.b, self.a, total)
        else:
            self.equation += "(b:{} - a:{} = {}) {} ".format(self.b, self.a, total, operator)
        return total

    def equation_1(self):
        c1 = self.c1
        c2 = self.c2
        d1 = self.d1
        d2 = self.d2
        self.state = True
        total = (c2("+") + c1("+")) + (d2("+") + c1())
        self.equation += "\nTotal = {}".format(total)
        return total

    def user_input(self):
        program_on = True
        while program_on:
            get_input = input("'c1'-(a+b), 'c2'-(a-b), 'd1'-(b+a), 'd2'-(b-a): ")
            if get_input is "c1":
                pass
            elif get_input is "c2":
                pass
            elif get_input is "d1":
                pass
            elif get_input is "d2":
                pass
            else:
                print("Wrong Input")
            get_input = input("Type an operator character: ")

less = smallest_equation(random.randint(0, 100), random.randint(0, 100))
less.equation_1()
print(less)

def get_gradient_at_b(x, y, m, b):
  diff = 0
  for i in range(0, len(x)):
    y_val = y[i]
    x_val = y[i]
    diff += (y_val - ((m*x_val)+b))
  return diff