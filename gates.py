import numpy as np

""" This scales the Matrix by 1/sqrt(2) in order to
create superposition
Hadamard Matrix : H = 1/sqrt(2)[[1,1], [1,-1]]
"""
def hadamard():
    return (1/np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ], dtype=complex)
