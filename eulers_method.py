import numpy as np
import pandas as pd
import math

def eulers_method(initial_values, euler_config, differential_equations):
  """
  This function uses Euler's Method to approximate a solution.
  """
  table = []
  limit = euler_config['limit']
  step_size = euler_config['step_size']

  for step in np.arange(initial_values[0], limit+step_size, step_size):
    # keep up with our location on x axis
    initial_values[0] = step
    # calculate derivatives for each differential equation we have
    derivatives = [equation(initial_values) for equation in differential_equations]
    table.append(initial_values + derivatives)
    # calculate new function value
    initial_values = [initial_values[0]] + [function_value + derivatives[index] * step_size for index, function_value in enumerate(initial_values[1:])]
  return table

#----- INITIAL CONDITIONS -----#
# [t, function1(t), function2(t), etc...]
initial_values = [0, 0.5, 0.5, 0, 0] # t, g1, g3, g2, g4
euler_config = {'step_size': .001, 'limit': 5}

#----- DIFFERENTIAL EQUATIONS -----#
g_sub_one_prime = lambda initial_values: initial_values[3]
g_sub_two_prime = lambda initial_values: (initial_values[1] + 1)*(1 - math.sqrt((initial_values[1] + 1)**2 + initial_values[2]**2))/math.sqrt((initial_values[1] + 1)**2 + initial_values[2]**2) + initial_values[1]*(1 - math.sqrt(initial_values[1]**2 + (1- initial_values[2])**2))/math.sqrt(initial_values[1]**2 + (1- initial_values[2])**2) + (1 - initial_values[1])*(1 - math.sqrt((1- initial_values[1])**2 + initial_values[2]**2))/math.sqrt((1- initial_values[1])**2 + initial_values[2]**2) + initial_values[1]*(1 - math.sqrt(initial_values[1] + (initial_values[2] + 1)**2))/math.sqrt(initial_values[1] + (initial_values[2] + 1)**2)
g_sub_three_prime = lambda initial_values: initial_values[4]
g_sub_four_prime = lambda initial_values: (initial_values[2]*(1 - math.sqrt((initial_values[1] + 1)**2 + initial_values[2]**2))/math.sqrt((initial_values[1] + 1)**2 + initial_values[2]**2)) + ((1 - initial_values[2])*(1 - math.sqrt(initial_values[1]**2 - (1 - initial_values[2])**2))/math.sqrt(initial_values[1]**2 - (1 - initial_values[2])**2)) + (initial_values[2]*(1 - math.sqrt((1 - initial_values[1])**2 + initial_values[2]**2))/math.sqrt((1 - initial_values[1])**2 + initial_values[2]**2)) + (initial_values[2] + 1)*(1 - math.sqrt(initial_values[1]**2 + ((initial_values[2] + 1)**2))/math.sqrt(initial_values[1]**2 + (initial_values[2] + 1)**2))
# add more equations here...

differential_equations = [g_sub_one_prime, g_sub_two_prime, g_sub_three_prime, g_sub_four_prime]

#----- RUN EULER'S METHOD -----#
euler_table = eulers_method(initial_values, euler_config, differential_equations)

#----- DISPLAY REUSLTS -----#
euler_table_row_names = ["t"] + ["g_" + str(i) for i in range(1, len(differential_equations)+1)] + ["g'_" + str(i) for i in range(1, len(differential_equations)+1)]
euler_table = np.asarray(euler_table)
euler_dataframe = pd.DataFrame(data = euler_table, columns = euler_table_row_names)
print(euler_dataframe)
