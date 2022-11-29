import numpy as np


#get 
scan_llik = llik(scan_data) #P(phi | signal) P(A|B)
P_signal = prior([0,111]) #P(phi) A
P_phi = 1/112 #P(B)

P = scan_link * P_signal.T / (1 / 112)

P = np.array([[4,2,3], [1,0,3]])
P = np.amax(P, axis=1)

