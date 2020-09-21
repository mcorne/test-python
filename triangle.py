def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
    
def is_right_triangle(a, b, c):
    if not is_triangle(a, b, c):
        is_right_triangle = False
    elif a > b and a > c:
        is_right_triangle = a**2 == b**2 + c**2
    elif b > a and b > c:
        is_right_triangle = b**2 == a**2 + c**2
    else:
        is_right_triangle = c**2 == a**2 + b**2
    return is_right_triangle    
    
def heron(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
def triangle_field(a, b, c):
    if not is_triangle(a, b, c):
        return None
    return heron(a, b, c)    
        

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
print("is triangle: ", is_triangle(a, b, c))
print("is right triangle: ", is_right_triangle(a, b, c))
print("triangle field: ", triangle_field(a, b, c))
