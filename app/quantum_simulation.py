from qiskit import QuantumCircuit, Aer, execute

def simulate_qkd():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts()

    return counts
