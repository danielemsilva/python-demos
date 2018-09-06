# Calculation of the hypotenuse of a right triangle
import math

leg1 = float(raw_input("Measurement of the first leg of the triangle:"))
leg2 = float(raw_input("measurement of the second leg of the triangle:"))

hypotenuse = leg1 ** 2 + leg2 ** 2
hypotenuse = math.sqrt(hypotenuse)

print "Measure of the Hypotenuse: %.2f" % hypotenuse
