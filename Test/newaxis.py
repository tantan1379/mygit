import numpy as np

a = np.random.rand(2,3,3)
print(a.shape)
aa = a[:,:,np.newaxis]
print(aa.shape)