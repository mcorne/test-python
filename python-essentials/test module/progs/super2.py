class Super:
    def __init__(self):
        self.var1 = 11

class Sub(Super):
    def __init__(self):
        super().__init__()

object = Sub()
print(object.var1)
