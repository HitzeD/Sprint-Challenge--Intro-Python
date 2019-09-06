# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Super class
class Vehicle():
	pass

# inherits from vehicle
class FlightVehicle(Vehicle):
	pass

# Inherits from FlightVehicle
class StarShip(FlightVehicle):
	pass

# Inherits from FlightVehicle
class Airplane(FlightVehicle):
	pass

# inherits from Vehicle
class GroundVehicle(Vehicle):
	pass

# inherits from GroundVehicle
class Car(GroundVehicle):
	pass

# inherits from GroundVehicle
class MotorCycle(GroundVehicle):
	pass