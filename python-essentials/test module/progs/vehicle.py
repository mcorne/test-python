class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicule(LandVehicle):
    pass

vehicle = 'aze'
vehicle2 = vehicle
vehicle += 'qsd'

print(vehicle is vehicle2)