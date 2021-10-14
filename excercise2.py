def sumOfLucas(highestNumber):
  current =1
  sum =2
  while(current < highestNumber):
    nextNumber = luc(current)
    if nextNumber %2 ==0:
      sum += nextNumber
    current += 1
  return sum

  # previousNumber = 2
  # currentNumber = 1
  # sum = 1
  # while (currentNumber + previousNumber) < highestNumber:
  #   temp = currentNumber
  #   currentNumber = currentNumber + previousNumber
  #   previousNumber = temp
  #   if currentNumber % 2 != 0:
  #     sum += currentNumber
  # return sum

def luc(n):
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return luc(n-1) + luc(n-2)

print(sumOfLucas(4))
