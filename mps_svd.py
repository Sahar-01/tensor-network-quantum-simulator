import numpy as np

def mps_decompose(psi, N, cutoff=1e-10):
    psi = psi.reshape([2]*N)
    mps = []
    left_dim = 1

    for _ in range(N - 1):
        psi = psi.reshape(left_dim * 2, -1)

        U, S, Vh = np.linalg.svd(psi, full_matrices=False)

        # 🔥 TRUNCATION
        max_bond = 4
        keep = np.arange(len(S)) < max_bond
        if np.sum(keep) == 0:  # safety (avoid empty)
            keep[0] = True

        U = U[:, keep]
        S = S[keep]
        Vh = Vh[keep, :]

        r = S.shape[0]

        A = U.reshape(left_dim, 2, r)
        mps.append(A)

        psi = np.diag(S) @ Vh
        left_dim = r

    A_last = psi.reshape(left_dim, 2, 1)
    mps.append(A_last)

    return mps


def mps_reconstruct(mps):
    res = mps[0]
    for i in range(1, len(mps)):
        res = np.tensordot(res, mps[i], axes=[-1, 0])
    return res.reshape(-1)