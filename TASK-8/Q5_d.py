import numpy as np
arr = np.array([1.5,3.6,5.4,6.2,9.8])
print(f'array type before changing {arr.dtype}')
print(arr) # it is before changing array
arr = arr.astype(np.int32)
print(f'array type after changing {arr.dtype}')
print(arr) # it is after changing the array
