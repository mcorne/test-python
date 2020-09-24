def l100kmtompg(litres):
    miles   = 100000 / 1609.344
    gallons = litres / 3.785411784
    return miles / gallons

def mpgtol100km(miles):
    meters = miles * 1609.344
    litres = 3.785411784
    return litres / meters * 100000

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))