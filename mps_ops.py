import numpy as np

def apply_single_qubit_gate(mps, G, k):
    A = mps[k]
    A_new = np.tensordot(G, A, axes=[1, 1])
    A_new = np.transpose(A_new, (1, 0, 2))
    mps[k] = A_new


def apply_two_qubit_gate(mps, G, k, cutoff=1e-10):
    A = mps[k]
    B = mps[k+1]

    left_dim = A.shape[0]
    right_dim = B.shape[2]

    theta = np.tensordot(A, B, axes=[2, 0])  # (l,2,2,r)

    theta = theta.reshape(left_dim, 4, right_dim)
    theta = np.tensordot(G, theta, axes=[1, 1])
    theta = np.transpose(theta, (1, 0, 2))

    theta = theta.reshape(left_dim * 2, 2 * right_dim)

    U, S, Vh = np.linalg.svd(theta, full_matrices=False)

    max_bond = 4
    keep = np.arange(len(S)) < max_bond
    if np.sum(keep) == 0:  # safety
        keep[0] = True

    U = U[:, keep]
    S = S[keep]
    Vh = Vh[keep, :]

    r = S.shape[0]

    mps[k] = U.reshape(left_dim, 2, r)
    mps[k+1] = (np.diag(S) @ Vh).reshape(r, 2, right_dim)