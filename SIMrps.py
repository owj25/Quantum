from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime.fake_provider import FakeManilaV2
import matplotlib.pyplot as plt

p1 = input("Player 1:")
p2 = input("Player 2:")

# Get a fake backend from the fake provider
backend = FakeManilaV2()

# Create a simple circuit
circuit = QuantumCircuit(2)
circuit.h([0, 1])
circuit.cx(1, 0)
circuit.cx(0, 1)
circuit.measure_all()


# Transpile the ideal circuit to a circuit that can be directly executed by the backend
transpiled_circuit = transpile(circuit, backend)
transpiled_circuit.draw('mpl', style="iqp")

# Run the transpiled circuit using the simulated fake backend
job = backend.run(transpiled_circuit, shots=1)
counts = job.result().get_counts()
#print(counts)

#print(max(counts))

plot_histogram(counts)
plt.show()

if max(counts) == '10':
    print(f"Congratulations {p1}, you win! The result was {max(counts)}.")
elif max(counts) == '01':
    print(f"Congratulations {p2}, you win! The result was {max(counts)}.")
else:
    print(f"You tied, play again. The result was {max(counts)}.")

