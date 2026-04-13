""" This scales the Matrix by 1/sqrt(2) in order to
create superposition
Hadamard Matrix : H = 1/sqrt(2)[[1,1], [1,-1]]
"""
import numpy as np

def hadamard():
    return (1/np.sqrt(2)) * np.array([
        [1, 1],
        [1, -1]
    ])

def pauli_x():
    return np.array([
        [0, 1],
        [1, 0]
    ])

def cnot():
    return np.array([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0]
    ])