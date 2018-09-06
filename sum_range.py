# Sum of elements of a range
def sum(begin, end):
  sum = 0
  while begin <= end:
    sum += begin
    begin += 1
  return sum

begin = int(raw_input("Enter the starting number:"))
end = int(raw_input("Enter the final number:"))
print sum(begin, end)
