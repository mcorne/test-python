def bmi(weight, height):
    if  height < 1.0 and height > 2.5 or \
        weight < 20 and weight > 200:
        return
    return weight / height**2
    
def lbtokg(lb):
    return lb * 0.45359237
    
def ftintom(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
    
height = ftintom(5, 7)
weight = lbtokg(176)
print(weight, height, bmi(weight, height))