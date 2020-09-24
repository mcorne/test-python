class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')


class C(A,B):
    def c(self):
        self.a()

o = C()
o.c()