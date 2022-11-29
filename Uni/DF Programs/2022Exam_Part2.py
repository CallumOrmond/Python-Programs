from cv2 import normalize
import numpy as np
import math

from pandas import array

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
B = np.array([1,2,3,4])


array = np.zeros((60, 100, 35, 2))
len(array)
last fram = (100, 35, 2)

def expected_locations(guess_array, img):

    last_frame = guess_array[len(guess_array) - 1]

    avg = lik_cell(np.mean(last_frame, axis=0), img)
    avg = np.exp(last_fram - avg) 

    expected = np.sum(normalized_values, axis=1)/ 35 #(100, 35,2) --> (100, 2)

    return expected

    


