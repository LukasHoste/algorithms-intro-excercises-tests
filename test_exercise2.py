from excercise2 import luc,sumOfLucas

def test_generateLucas():
  assert(3 == luc(2))
  assert(4 == luc(3))

def test_sumOfLucas():
  assert(sumOfLucas(4)==6)
  assert(sumOfLucas(7) ==24)