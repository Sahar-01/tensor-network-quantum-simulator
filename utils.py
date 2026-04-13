import numpy as np

# random normalized qunatum state for a system with N-qubits
def random_state(N):
    # psi = a random vector in 2^3 dimensional space
    psi = np.random.rand(2**N)
    # return the normalized vector
    return psi / np.linalg.norm(psi)

'''Matrix Product State example output:
    (left bond, physical index, right bond)
    A[0] shape: (1, 2, 3)
    A[1] shape: (3, 2, 4)
    A[2] shape: (4, 2, 1)
    
    Physical index = 2, |0> and |1>
'''
def print_mps_shapes(mps):
    for i, A in enumerate(mps):
        print(f"A[{i}] shape: {A.shape}")