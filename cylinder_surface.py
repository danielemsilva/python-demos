# Calculate the surface of a cylinder
import math

radius = float(raw_input("Radius: "))
height = float(raw_input("Height: "))
area = 2 * math.pi * radius * (radius + height)

print 'Cylinder surface = %.2f' % area
