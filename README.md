# Matrix Product State Quantum Simulator


---

## Overview

This project explores the simulation of small quantum systems using two different approaches:

1. **Full-State Representation**  
2. **Matrix Product State (MPS) Representation**

The aim is to understand:

- how quantum states scale as the number of qubits increases,
- why brute-force simulation becomes difficult,
- how tensor network methods reduce complexity,
- and how quantum gates can be applied in both frameworks.

This project was built as a practical introduction to:

- quantum computing,
- linear algebra,
- tensor methods,
- singular value decomposition (SVD).

---

## Why MPS?

A system of \(N\) qubits has a state vector of size:

$$
2^N
$$

This means:

| Qubits | State Size |
|------|------------|
| 5 | 32 |
| 10 | 1,024 |
| 20 | 1,048,576 |
| 30 | 1,073,741,824 |

Even moderate systems become computationally expensive.

Matrix Product States solve this by decomposing the full wavefunction into a chain of smaller tensors.

Instead of storing exponential data, many useful states can be represented approximately using:

$$
O(ND^2)
$$

where \(D\) is the bond dimension.

---

## Full State vs MPS

| Feature | Full State | MPS |
|--------|------------|-----|
| Storage Growth | \(2^N\) | \(ND^2\) |
| Exactness | Exact | Exact / Approximate |
| Good for Large Systems | No | Yes |
| Handles Entanglement | Yes | Limited by bond dimension |
| Easy to Understand | Yes | More advanced |

---

### Visual Comparison


---

## Project Structure

```text
project/
│── main.py
│── full_state.py
│── mps_svd.py
│── mps_ops.py
│── gates.py
│── utils.py
│── images/
```

### File Descriptions

- **main.py**  
  Runs the complete simulation and compares methods.

- **full_state.py**  
  Applies gates directly to the full \(2^N\)-dimensional quantum state.

- **mps_svd.py**  
  Converts a full quantum state into MPS form using SVD and reconstructs it.

- **mps_ops.py**  
  Applies single-qubit and two-qubit gates directly to MPS tensors.

- **gates.py**  
  Defines quantum gates such as Hadamard and CNOT.

- **utils.py**  
  Helper functions such as random state generation and tensor shape printing.

---

## Mathematics

---

## 1. Quantum State Representation

An \(N\)-qubit quantum state is:

$$
|\psi\rangle = \sum_i c_i |i\rangle
$$

For 3 qubits:

$$
|\psi\rangle =
\begin{bmatrix}
c_{000}\\
c_{001}\\
c_{010}\\
c_{011}\\
c_{100}\\
c_{101}\\
c_{110}\\
c_{111}
\end{bmatrix}
$$

This requires \(2^N\) coefficients.

---

## 2. Matrix Product State Decomposition

Instead of one large tensor, rewrite:

$$
\psi_{i_1 i_2 i_3 ... i_N}
$$

as:

$$
A^{[1]}A^{[2]}A^{[3]}...A^{[N]}
$$

Each site stores a smaller tensor.

For example:

```text
A[0] -- A[1] -- A[2]
```

with shapes:

```text
(1,2,D), (D,2,D), (D,2,1)
```

---

## 3. Singular Value Decomposition (SVD)

To split tensors efficiently:

$$
M = U \Sigma V^\dagger
$$

This is used repeatedly to convert the full state into MPS form.

---

## 4. Quantum Gates

### Hadamard Gate

Creates superposition:

$$
H =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1\\
1 & -1
\end{bmatrix}
$$

### CNOT Gate

Entangles two qubits.


---

## Example Run

```python
N = 3
psi = random_state(N)
mps = mps_decompose(psi, N)

print_mps_shapes(mps)

psi_rec = mps_reconstruct(mps)

apply_single_qubit_gate(mps, H, 0)
apply_two_qubit_gate(mps, CNOT, 0)
```

### Example Output

```text
Initial state:
[0.31 0.18 0.44 0.21 0.52 ...]

MPS shapes:
A[0] shape: (1,2,2)
A[1] shape: (2,2,2)
A[2] shape: (2,2,1)

Reconstruction error:
2.1e-15

Final error:
8.7e-15
```

---

## Interpretation of Results

The final error is extremely small:

$$
\sim 10^{-15}
$$

This means:

- the MPS implementation is numerically accurate,
- gates were applied correctly,
- reconstruction is working properly.

---

## Visual Explanation

### Full State Method

Stores entire vector:

```text
[c000 c001 c010 c011 c100 c101 c110 c111]
```

### MPS Method

Stores linked tensors:

```text
[A1]--[A2]--[A3]
```

This is often dramatically smaller.

---

## Future Improvements

- Extend MPS implementation to larger systems
- Introduce truncation using bond dimension limits
- Study entanglement entropy
- Compare runtime scaling vs full-state simulation
- Simulate deeper quantum circuits
- Add visualization tools
- Implement variational algorithms

---

## Notes

This project was developed as a learning exercise in:

- quantum computing,
- tensor networks,
- numerical linear algebra,
- scalable simulation methods.

It focuses on building intuition for how modern quantum simulators represent states efficiently.


---
