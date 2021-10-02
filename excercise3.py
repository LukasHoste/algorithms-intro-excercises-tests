class BinaryCounter:
  def __init__(self):
    self.__ledBinary = '1111'

  def decimal(self):
    # decimal = 0
    # n = 0
    # for i in range(0,4):
    #   n = ((self.__ledBinary & (1 << (3-i))) >> (3-i))  # Select a digit of the binary number
    #   decimal = (2*decimal) + n # use the doubling method to convert to binary
    return int(self.__ledBinary, 2)

  def hexadecimal(self):
    return hex(self.decimal())
    
  def increment(self):
   decimal = self.decimal() + 1
   if(decimal > 15):
     self.__ledBinary = bin(decimal - 16)
   else:
     self.__ledBinary = bin(decimal)
  
  def decrement(self):
    decimal = self.decimal() - 1
    if(decimal < 0):
      self.__ledBinary = bin(decimal + 16)
    else:
      self.__ledBinary = bin(decimal)
  
counter = BinaryCounter()
print(counter.decimal())
print(counter.hexadecimal())
counter.increment()
print(counter.decimal())
print(counter.hexadecimal())

