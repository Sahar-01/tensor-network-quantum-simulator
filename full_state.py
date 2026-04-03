import numpy as np
from gates import hadamard

# basis states
zero = np.array([1, 0], dtype=complex)
one = np.array([0, 1], dtype=complex)

def create_zero_state(n):
    """Create |00...0> for n qubits"""
    state = zero
    for _ in range(n - 1):
        state = np.kron(state, zero)
    return state


'''I (eye) being the identity matrix: [[1,0][0,1]]'''
def apply_single_qubit_gate(state, gate, qubit, n):
    """Apply gate to a single qubit"""
    I = np.eye(2, dtype=complex)

    op = 1
    for i in range(n):
        if i == qubit:
            op = np.kron(op, gate)
        else:
            op = np.kron(op, I)

    return op @ state