from full_state import create_zero_state, apply_single_qubit_gate, apply_cnot
from gates import hadamard

# start in |00>
state = create_zero_state(2)

# apply H to qubit 0
state = apply_single_qubit_gate(state, hadamard(), 0, 2)

# apply CNOT
state = apply_cnot(state, 0, 1, 2)

print(state)
