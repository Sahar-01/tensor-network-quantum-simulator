# tensor-network-quantum-simulator

## Overview

This project explores the simulation of small quantum systems using both full-state representations and tensor network methods.

The goal is to understand how quantum states scale with system size, and how alternative representations such as Matrix Product States (MPS) can be used to reduce computational complexity.

## Motivation

Simulating quantum systems quickly becomes intractable as the number of qubits increases, due to the exponential growth in the size of the state space. This project investigates this challenge by implementing a basic quantum simulator and comparing it with a tensor network approach.

The work is inspired by methods used in quantum computing and many-body physics, where structured representations of states can provide significant efficiency gains.

## Features

* Representation of quantum states for small numbers of qubits
* Implementation of basic quantum gates (Hadamard, CNOT)
* Tensor product construction of multi-qubit systems
* Initial implementation of Matrix Product State (MPS) decomposition
* Experimental comparison between full-state and tensor-based approaches

## Structure

* `full_state.py` — basic quantum state representation and gate application
* `mps.py` — initial tensor network (MPS) implementation
* `gates.py` — definitions of quantum gates
* `experiments.py` — simple runtime and scaling experiments

## Current Status

Work in progress. Initial focus is on building a working full-state simulator before extending to tensor network methods.

## Future Work

* Extend MPS implementation to larger systems
* Investigate the effect of entanglement on compression
* Compare runtime scaling between methods
* Explore additional quantum circuits

## Notes

This project is intended as a learning exercise in quantum computing and numerical methods, with a focus on building intuition for tensor-based representations of quantum systems.
