import numpy as np
from numba import jit
import matplotlib.pyplot as plt

@jit
def branching_process(samples, probs, colony_size_limit):

    prob_0_kids = probs[0]
    prob_1_kid  = probs[1]
    prob_2_kids = probs[2]

    print('P(0 kids) = {}'.format(prob_0_kids))
    print('P(1 kids) = {}'.format(prob_1_kid))
    print('P(2 kids) = {}\n'.format(prob_2_kids))

    samples_survived = 0
    samples_died = 0

    for sample in range(samples):
        # start colony with 1 individual
        X = 1
        # set limit on how big a colony can grow
        while X < colony_size_limit:
            for i in range(X):
                r = np.random.rand()
                if 0 <= r < prob_0_kids:
                    X -= 1
                if prob_0_kids < r < 1 - prob_1_kid:
                    X += 0
                if 1 - prob_1_kid < r < 1:
                    X += 1

            # if at any time X = 0, the population will never recover
            if X <= 0:
                samples_died += 1
                break

        if X > 0:
            samples_survived += 1

    print('{} percent of colonies survived'.format((samples_survived/samples)*100))
    print('{} percent of colonies died'.format((samples_died/samples)*100))

    return None

q = 5
samples = 1000
probs = [1-q, q/2, q/2]
colony_size_limit = 1000

branching_process(samples, probs, colony_size_limit)
