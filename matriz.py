import numpy as np

matriz1 = np.array([[1,2,3],[4,5,6]])
matriz2 = np.array([[7,8,9],[10,11,12]])

soma=np.add(matriz1,matriz2)
print(f'a soma entre matrizes é: {soma}')
transporta = matriz1.transpose() 
print(f'a troca de valores ficou assim: {transporta}')
determinante= np.linalg.det(matriz1)
print(f'para verificar o determinante: {determinante}')


