#Hillary Ellis is done with HW2

import numpy as np
# 2. Create matrix A with size (3,5) containing random numbers A = np.random.random(15)
A = np.random.random(15)
A = A.reshape(3,5)
A = np.matrix(A)
# 3. Find the size and length of matrix A
A.size
len(A)
# 4. Resize (crop/slice) matrix A to size (3,4)
A_Resize = A[:, :-1]
# 5. Find the transpose of matrix A and assign it to B
B = A.T
# 6. Find the minimum value in column 1 of matrix B (check the proper4es of a matrix – ‘B.min()’)
B[:, -2].min()
# 7. Find the minimum and maximum values for the en4re matrix A
A.max()
A.min()
# 8. Create vector X (an array) with 4 random numbers
X = np.array(np.random.random(3))
# 9. Create a func4on and pass vector X and matrix A in it
def mult(X, A):
# 10. In the new func4on mul4ply vector X with matrix A and assign the result to D
# (note: you may get an error! ... think why and fix it. Recall matric manipula4on in class!)
    return X*A

D = mult(X, A)
# 11. Create a complex number Z with absolute and real parts != 0
Z = complex(3,4)
# 12. Show its real and imaginary parts as well as it’s absolute value
Z.imag
Z.real
abs(Z)
# 13. Mul4ply result D with the absolute value of Z and record it to C
C = abs(Z) * D
# 14. Convert matrix B from a matrix to a string and overwrite B
B = np.array_str(B)
