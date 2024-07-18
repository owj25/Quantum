from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime.fake_provider import FakeOsaka
import matplotlib.pyplot as plt

r = len(str(bin(int(input("Max for number (7, 15, 31, 63, 127, 255)"))))) - 2

# Get a fake backend from the fake provider
backend = FakeOsaka()

circuit = QuantumCircuit(r, r)

for i in range(r):
    circuit.h(i)
for j in range(r):
    circuit.measure(j, j)


transpiled_circuit = transpile(circuit, backend)
# transpiled_circuit.draw('mpl', style="iqp")

# Run the transpiled circuit using the simulated fake backend

job = backend.run(transpiled_circuit, shots=100)
result = int(max(job.result().get_counts()), 2)

print(f"Random Number: {result}")
