class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'my name is ' + self.name

class Sub(Super):
    def __init__(self, name):
        super().__init__(name)

object = Sub('andy')
print(object)
