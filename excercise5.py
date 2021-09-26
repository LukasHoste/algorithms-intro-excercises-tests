# presume function is x^2  
# a is the start of the interval and b the end, n is the amount of subintervals
def riemannSum(a, b, n):
  A = 0
  deltaX = (b-a)/n
  for i in range(1,n):
    A += ((a+ (i*deltaX))**2)
  A += b**2
  return A*deltaX

print(riemannSum(2,9,8))
