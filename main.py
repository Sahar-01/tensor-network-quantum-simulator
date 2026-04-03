from full_state import create_zero_state, apply_single_qubit_gate
from gates import hadamard

state = create_zero_state(1)
new_state = apply_single_qubit_gate(state, hadamard(), 0, 1)

print(new_state)