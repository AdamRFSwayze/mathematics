GOLDEN_RATIO = 1.61803398875

def fibonacci_sequence(firstInteger, secondInteger, limit):
  firstInteger = float(firstInteger)
  secondInteger = float(secondInteger)
  sigma = 0
  fib_sequence = []
  ratios = []
  fib_sequence.append(firstInteger)
  fib_sequence.append(secondInteger)

  while(sigma < limit):
    sigma = firstInteger + secondInteger
    firstInteger = secondInteger
    secondInteger = sigma
    fib_sequence.append(sigma)
    ratios.append(secondInteger/firstInteger)

  return fib_sequence, ratios

fib_sequence, ratios = fibonacci_sequence(8, 17, 9000000)
fib_sequence = [int(i) for i in fib_sequence]

print('Fibonacci Sequence:\n' + str(fib_sequence) + '\n')
print('Ratio between any two consecutive #s:\n' + str(ratios) + '\n')
print('Ratio converges to:' + str(ratios[-1]))
print('Golden Ratio Margin of Error:' + str(GOLDEN_RATIO - ratios[-1]))