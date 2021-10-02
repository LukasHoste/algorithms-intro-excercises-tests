class Line:
  def __init__(self):
    self.__x1 = 0
    self.__y1 = 0
    self.__x2 = 0
    self.__y2 = 0
  def __init__(self, x1, y1, x2, y2):
    self.__x1 = x1
    self.__y1 = y1
    self.__x2 = x2
    self.__y2 = y2
  
  def lineLength(self):
    return ((self.__x2 - self.__x1)**2 + (self.__y2 - self.__y1)**2)**0.5

line = Line(7,32,9,-22)
print(line.lineLength())