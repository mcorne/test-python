s = 'hello world'
print(str(s))
print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + str(x) + ', and y is ' + str(y) + '...'
print(s)
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello world\n'
hello2 = repr(hello)
print(hello2)