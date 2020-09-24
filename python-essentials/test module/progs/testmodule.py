from sys import path
# path.append('..\\modules') not working (?)
path.append('C:\\Data\\python\\test module\\modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))
