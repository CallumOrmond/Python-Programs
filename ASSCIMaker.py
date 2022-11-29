import numpy as np
from PIL import Image
import os

img = Image.open('C:/Users/callu/PythonPrograms/Genral/media/pepe.jpg').convert('L')
arr = np.array(img)

assci = [".", ",", "¬", "~", "=", "+", "/", "#", "%", "@" ]
assci.reverse()
# record the original shape
shape = arr.shape


arr = arr[::6, ::2]

print(arr.shape)

f = open("art.txt", "w")
for i in arr:
    f.write("\n")
    for j in i:

        index = round(j / 25) - 1
        #print(index, "index")
        f.write(assci[index])

f.close()


# make a PIL image
# img2 = Image.fromarray(arr2, 'L')
# img2.show()