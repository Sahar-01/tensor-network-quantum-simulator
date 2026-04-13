import numpy as np

from mps_svd import mps_decompose, mps_reconstruct
from mps_ops import apply_single_qubit_gate, apply_two_qubit_gate
from full_state import apply_full_gate
from gates import hadamard, cnot
from utils import random_state, print_mps_shapes


def main():
    N = 3

    # Create state
    psi = random_state(N)

    print("Initial state:\n", psi)

    # MPS
    mps = mps_decompose(psi, N)

    print("\nMPS shapes:")
    print_mps_shapes(mps)

    # Check reconstruction
    psi_rec = mps_reconstruct(mps)
    print("\nReconstruction error:", np.linalg.norm(psi - psi_rec))

    # Gates
    H = hadamard()
    CNOT = cnot()

    # Apply on MPS
    apply_single_qubit_gate(mps, H, 0)
    apply_two_qubit_gate(mps, CNOT, 0)

    psi_mps = mps_reconstruct(mps)

    # Full state
    psi_full = apply_full_gate(psi, H, N, 0)
    psi_full = apply_full_gate(psi_full, CNOT, N, 0, two_qubit=True)

    # Compare
    print("\nFinal error:", np.linalg.norm(psi_full - psi_mps))


if __name__ == "__main__":
    main()