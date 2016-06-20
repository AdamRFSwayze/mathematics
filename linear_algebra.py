import numpy as np
from sympy import Matrix, GramSchmidt
from sympy.abc import x

def is_square(matrix):
  if matrix.shape[0] == matrix.shape[1]:
    return True
  else:
    return False

def is_linearly_independent(matrix):
  """ checks a numpy array of vectors for linear independence and returns a boolean """
  matrix = Matrix(matrix)
  rref_results = matrix.rref()
  if len(rref_results[1]) == matrix.cols:
    return True
  else:
    return False

def is_orthogonal(matrix):
  """ check if a numpy array of vectors is orthogonal and returns a boolean """
  if matrix.T.dot(matrix) == matrix.dot(matrix.T):
    return True
  else:
    return False

def orthogonalize(matrix):
  """ takes a numpy array of vectors and uses Gram-Schmidt to orthogonalize them """
  matrix = [Matrix(vector) for vector in matrix]
  orthogonalized_vectors = GramSchmidt(matrix)
  numpy_orthogonalized_vectors = np.array([list(vector) for vector in orthogonalized_vectors])
  return numpy_orthogonalized_vectors

def orthonormalize(matrix):
  """ takes a numpy array of vectors and uses Gram-Schmidt to orthonormalize them """
  matrix = [Matrix(vector) for vector in matrix]
  orthonormalized_vectors = GramSchmidt(matrix, True)
  numpy_orthonormalized_vectors = np.array([list(vector) for vector in orthonormalized_vectors])
  return numpy_orthonormalized_vectors

def get_geometric_multiplicity(matrix, eigenvalue):
  """ still needs work """
  if is_square(matrix):
    matrix = Matrix(matrix)
    eigenvectors = matrix.eigenvects()
    print(eigenvectors)
    return null
  else:
    raise Exception('not a square matrix')

def get_algebraic_multiplicity(matrix, eigenvalue):
  if is_square(matrix):
    matrix = Matrix(matrix)
    eigenvalues = matrix.eigenvals()
    algebraic_multiplicity = eigenvalues[eigenvalue]
    return algebraic_multiplicity
  else:
    raise Exception('not a square matrix')

def is_diagonalizable(matrix):
  """ still needs work """
  if get_algebraic_multiplicity(matrix) == get_geometric_multiplicity(matrix):
    return True
  else:
    return False

# create numpy matrix
matrix = np.array([[3, -2,  4, -2], [5,  3, -3, -2], [5, -2,  2, -2], [5, -2, -3,  3]])
print(get_geometric_multiplicity(matrix, 3))
# print(orthonormalize(matrix))
# print(is_diagonalizabe(matrix))