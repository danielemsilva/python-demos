# Sorting a list using the 'bubblesort' technique
def bubblesort(seq):
  exchanges = True
  decrease = len(seq) - 1
  while decrease > 0 and exchanges:
    exchanges = False
    for i in range(decrease):
      if seq[i] > seq[i + 1]:
        exchanges = True
        temp = seq[i]
        seq[i] = seq[i + 1]
        seq[i + 1] = temp
    decrease = decrease - 1

numbers = raw_input("Enter the sequence of numbers (separated by space):").split(' ')
numbers = map(int, numbers)
bubblesort(numbers)

strlist = ""
for n in numbers:
  strlist += str(n) + ' '
print "Ordered list:", strlist
