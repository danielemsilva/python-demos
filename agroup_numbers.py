# coding: utf-8
# Grouping of odd and even numbers

gEven = "even"
gOdd = "odd"

def agroup_pairs_odd(numbers):
	groups = {gEven: [], gOdd: []}
	
	for i in range(len(numbers)):
		if numbers[i] % 2 == 0:
			groups[gEven].append(numbers[i])
		else:
			groups[gOdd].append(numbers[i])
	
	return groups

print "Enter the numbers: "
seq = raw_input().split(' ')
# Convert to int
for i in range(len(seq)):
  seq[i] = int(seq[i])

group = agroup_pairs_odd(seq)
print "Even numbers:", group[gEven]
print "Odd numbers:", group[gOdd]