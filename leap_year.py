# Check if the given year is leap year
year = int(raw_input("Enter a year: "))
leap_year = False

if year % 400 == 0:
  leap_year = True
elif year % 4 == 0 and year % 100 != 0:
	leap_year = True

if leap_year == True:
	print "%d is leap year" % year
else:
	print "%d is not leap year" % year
