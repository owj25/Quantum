from qiskit import QuantumCircuit
from qiskit import transpile
from qiskit.visualization import plot_histogram
from qiskit_ibm_runtime.fake_provider import FakeOsaka
import matplotlib.pyplot as plt

r = len(str(bin(int(input("Max for number (7, 15, 31, 63, 127, 255)"))))) - 2

# Get a fake backend from the fake provider
backend = FakeOsaka()

circuit = QuantumCircuit(r, r)

circuit.h([i for i in range(r)])

circuit.measure([j for j in range(r)], [h for h in range(r)])


transpiled_circuit = transpile(circuit, backend)
# transpiled_circuit.draw('mpl', style="iqp")

# Run the transpiled circuit using the simulated fake backend

job = backend.run(transpiled_circuit, shots=1)
result = int(max(job.result().get_counts()), 2)

print(f"Random Number: {result}")

x = job.result().get_counts().keys()
