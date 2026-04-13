import numpy as np

def random_state(N):
    psi = np.random.rand(2**N)
    return psi / np.linalg.norm(psi)


def print_mps_shapes(mps):
    for i, A in enumerate(mps):
        print(f"A[{i}] shape: {A.shape}")