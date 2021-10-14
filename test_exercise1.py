from excercise1 import sumOfNumbersDivisibleBy7Or9

def test_sumOfNumbers():
  assert(sumOfNumbersDivisibleBy7Or9(0,9) == 16)
  assert(sumOfNumbersDivisibleBy7Or9(0,20) == 48)
  assert(sumOfNumbersDivisibleBy7Or9(9,20) == 41)