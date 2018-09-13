# coding: utf-8
# Conversion of a character to bases 2, 10 and 16

character = raw_input()

# converting to decimal
decimal = ord(character)
# converting to binary
binary = bin(decimal)
# converting to hexadecimal
hexadecimal = hex(decimal)

print "Your character is:", character
print "In decimal corresponds to:", decimal
print "In binary is:", binary
print "In hexadecimal is:", hexadecimal
