from asyncio.windows_events import INFINITE
import numpy as np

x = [[1,2],[3,4], [5,6]]
y = [[1,4], [2,3]]
x = np.array(x)
y = np.array(y)
y_mean = y.mean(axis=0)


minNorm = INFINITE
for i in x:
    v = i - y
    new = np.linalg.norm(v)
    if new < minNorm:
        minNorm = new
        bestX = i 

print(bestX, y_mean)