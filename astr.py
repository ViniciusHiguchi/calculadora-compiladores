
class VariableNotDefinedException(Exception):
    pass

class Number():
    def __init__(self, value, sign):
        self.value = value
        self.sign = sign

    def eval(self):
        temp = float(self.value)
        if self.sign == '-':
            temp = temp*(-1)
        return temp                      


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Mod(BinaryOp):
    def eval(self):
        return int(self.left.eval() % self.right.eval())


class LessThan(BinaryOp):
    def eval(self):
        return (self.left.eval() < self.right.eval())

class LessThanEqual(BinaryOp):
    def eval(self):
        return (self.left.eval() <= self.right.eval())

class MoreThan(BinaryOp):
    def eval(self):
        return (self.left.eval() > self.right.eval())

class MoreThanEqual(BinaryOp):
    def eval(self):
        return (self.left.eval() >= self.right.eval())

class IsEqual(BinaryOp):
    def eval(self):
        return (self.left.eval() == self.right.eval())

class IsNotEqual(BinaryOp):
    def eval(self):
        return (self.left.eval() != self.right.eval())


class Ambient():
    def __init__(self, key, value, ambient):
        self.key = key
        self.value = value
        self.ambient = ambient

    def eval(self):
        self.ambient.update({self.key : self.value.eval()})
        return True

class AmbientGet():
    def __init__(self, key, ambient):
        self.key = key
        self.ambient = ambient
        self.value = self.eval()

    def eval(self):
        if self.key not in self.ambient.keys():
            raise VariableNotDefinedException(f"Identificador '{self.key}' não definido.")
        return self.ambient[self.key]

class AritPriority():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return(self.value.eval())


class Scan():
    def eval(self):
        return(float(input()))


class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(f"{self.value.eval()}\n")