def SumOfNumbersDivisibleBy7Or9(start, end):
  sum = 0
  for i in range(start, end+1):
    if ((i % 7 == 0) or (i % 9 == 0)):
      sum += i
  return sum
  
print(SumOfNumbersDivisibleBy7Or9(0,9))
