from sympy import Matrix
from sympy.abc import x

def is_orthogonal():
  return null

def is_linearly_independent(matrix):
  """ checks a matrix for linear independence and returns a boolean"""
  rref_results = matrix.rref()
  if len(rref_results[1]) == matrix.cols:
    return True
  else:
    return False

def orthogonalize(set_of_vectors):
  """ takes an array of vectors (Sympy Matrix objects) and uses Gram-Schmidt to orthogonalize them"""
  return GramSchmidt(set_of_vectors)

def orthonormalize(set_of_vectors):
  """ takes an array of vectors (Sympy Matrix objects) and uses Gram-Schmidt to orthogonalize them"""
  return GramSchmidt(set_of_vectors, True)

M = Matrix([[1, 2], [x, 1 - 1/x]])
print(is_linearly_independent(M))