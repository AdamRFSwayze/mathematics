from sympy import Matrix
from sympy.abc import x
import numpy as np
from numba import vectorize

def is_square(matrix):
  if matrix.shape[0] == matrix.shape[1]:
    return True
  else:
    return False

def is_orthogonal(matrix):
  """ check if matrix is orthogonal """
  if matrix.T.dot(matrix) == matrix.dot(matrix.T):
    return True
  else:
    return False

def is_linearly_independent(matrix):
  """ checks a matrix for linear independence and returns a boolean"""
  matrix = Matrix(matrix)
  rref_results = matrix.rref()
  if len(rref_results[1]) == matrix.cols:
    return True
  else:
    return False

def orthogonalize(set_of_vectors):
  """ takes an array of vectors and uses Gram-Schmidt to orthogonalize them"""
  set_of_vectors = [Matrix(vector) for vector in set_of_vectors]
  return GramSchmidt(set_of_vectors)

def orthonormalize(set_of_vectors):
  """ takes an array of vectors and uses Gram-Schmidt to orthonormalize them"""
  set_of_vectors = [Matrix(vector) for vector in set_of_vectors]
  return GramSchmidt(set_of_vectors, True)

# create numpy matrix
matrix = np.array([[3, 1, 9], [1, 2, 8]])