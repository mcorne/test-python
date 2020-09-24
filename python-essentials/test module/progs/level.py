class Level0:
    Var0 = 100
    def __init__(self):
        self.var0 = 101
    def fun0(self):
        return 102

class Level1(Level0):
    Var1 = 200
    def __init__(self):
        super().__init__()
        self.var1 = 201
    def fun1(self):
        return 202

class Level2(Level1):
    Var2 = 300
    def __init__(self):
        super().__init__()
        self.var2 = 301
    def fun2(self):
        return 302

object = Level2()
print(object.Var0, object.var0, object.fun0())
print(object.Var1, object.var1, object.fun1())
print(object.Var2, object.var2, object.fun2())