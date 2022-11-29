import numpy as np
import math

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b = np.array([[1,2],[2,4],[5,4]])
c = np.array([[5,4],[1,2],[2,4]])



def distances(input_tensor, output_tensor):
    distance = input_tensor - output_tensor
    distance = np.linalg.norm(distance, axis=1, ord=1)
    return distance ** 2

