import numpy as np


def power_iterate(A, x, n):
    for i in range(n):
        x = A @ x # matrix multiplication
        x = x / np.linalg.norm(x, np.inf) #
        #normalize x using the L-infinity norm during power
        #iteration
    return x / np.linalg.norm(x, 2) # finally,
#divide by the L2 norm so x can be compared with
#result of np.linalg.eig


# create a random 3 x 3 matrix
A = np.random.normal(0, 1, (3, 3))
# make it symmetric to ensure all eigenvalues are real (not complex)
A = A + A.T
print( A)


# create a random 3-element column vector
random_vec = np.random.normal(0, 1, (3, 1))
print(random_vec)

power = power_iterate(A, random_vec, n=500)
print(power)
