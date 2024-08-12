import numpy as np

coeficientes= np.array([[2,1],[1,-1]])
ladoDireito=np.array([5,1])
solucao = np.linalg.solve(coeficientes,ladoDireito)
print(solucao)