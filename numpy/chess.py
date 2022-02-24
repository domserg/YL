import numpy as np


def make_field(size):
    arr = np.zeros((size, size), dtype=np.int8)
    arr[::2, ::2] = 1
    arr[1::2, 1::2] = 1
    return arr


print(make_field(5))
