import random

number_of_trials =1000000
event_A = 'H'
sample_space = ['H', 'T']

heads = 0.0
tails = 0.0
for i in range(0, number_of_trials):
  outcome = random.choice(sample_space)
  if outcome == 'H':
    heads+=1
  else:
    tails+=1

true_probability = 0.5
print('True probability is: 0.5')
relative_frequency = heads/float(number_of_trials)
print('Relative frequency is:' + str(relative_frequency))
margin_of_error = true_probability - relative_frequency
print('Margin of error is:' + str(margin_of_error))
