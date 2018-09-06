# A number is chosen randomly with the randint function. The user tries to guess it.
import random
# A number is generated in the range of 1 to 100
number = random.randint(1, 100)
attempts = 1
hunch = int(raw_input("What's the number? "))

while hunch != number:
	attempts += 1

	if hunch > number:
		print "The number is less than this"
	elif hunch < number:
		print "The number is larger than this"

	hunch = int(raw_input("What's the number? "))

print "Right! You needed %d attempts." % attempts
