from IPython.display import display, Latex, Math, Markdown
import numpy as np
import sympy as sym
sym.init_printing()

def printltx(s):
  try:
  	display(Latex(s))
  except:
    print(s)

def ltxmtx(A, axis = 1):
  try:
    if isinstance(A, np.ndarray):
      A = A.round(4)
    M = sym.Matrix(A)
    sh = np.array(M.shape)
    sz = np.prod(sh)
    if sz == np.max(sh):
      if axis == 0:
        M = M.reshape(sz, 1)
      else:
        M = M.reshape(1, sz)
    return " $" + sym.latex(M) + "$ "
  except:
    return A

array_f = get_ipython().display_formatter.formatters['text/latex']
array_f.for_type('numpy.ndarray', ltxmtx)
array_f.for_type('sympy.matrices.dense.MutableDenseMatrix', ltxmtx)