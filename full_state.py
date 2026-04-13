import numpy as np


# ----------------------------
# APPLY GATE TO FULL STATE
# ----------------------------
def apply_full_gate(psi, G, N, k, two_qubit=False):
    """
    Apply a gate to a full quantum state.

    Parameters:
    - psi: state vector (size 2^N)
    - G: gate (2x2 for single, 4x4 for two-qubit)
    - N: number of qubits
    - k: target qubit index
    - two_qubit: whether gate is 2-qubit

    Returns:
    - new state vector
    """

    # reshape into tensor form
    psi = psi.reshape([2] * N)

    if not two_qubit:
        # ----------------------------
        # SINGLE-QUBIT GATE
        # ----------------------------
        # Contract gate with qubit k
        psi = np.tensordot(G, psi, axes=[1, k])

        # Move new axis into position k
        psi = np.moveaxis(psi, 0, k)

    else:
        # ----------------------------
        # TWO-QUBIT GATE
        # ----------------------------
        # reshape (4,4) → (2,2,2,2)
        G = G.reshape(2, 2, 2, 2)

        # Contract input indices with qubits k and k+1
        psi = np.tensordot(G, psi, axes=[[2, 3], [k, k+1]])

        # Move output indices back to positions k and k+1
        psi = np.moveaxis(psi, [0, 1], [k, k+1])

    return psi.reshape(-1)


# ----------------------------
# OPTIONAL: DEBUG VERSION
# ----------------------------
def apply_full_gate_debug(psi, G, N, k, two_qubit=False):
    psi = psi.reshape([2] * N)

    print("\n--- DEBUG ---")
    print("Initial psi shape:", psi.shape)

    if not two_qubit:
        print("Single-qubit gate")
        print("G shape:", G.shape)

        psi = np.tensordot(G, psi, axes=[1, k])
        print("After tensordot:", psi.shape)

        psi = np.moveaxis(psi, 0, k)
        print("After moveaxis:", psi.shape)

    else:
        print("Two-qubit gate")
        print("Original G shape:", G.shape)

        G = G.reshape(2, 2, 2, 2)
        print("Reshaped G:", G.shape)

        psi = np.tensordot(G, psi, axes=[[2, 3], [k, k+1]])
        print("After tensordot:", psi.shape)

        psi = np.moveaxis(psi, [0, 1], [k, k+1])
        print("After moveaxis:", psi.shape)

    return psi.reshape(-1)