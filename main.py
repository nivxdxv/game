import qiskit
import random
circuit = qiskit.QuantumCircuit(2, 2)
num_guesses = 0
target = random.randint(0, 3)
circuit.h(0)
circuit.cx(0, 1)
while True:
    print("Guess a number between 0 and 3:")
    guess = int(input())
    if guess == target:
        print("Congratulations! You guessed the number in", num_guesses, "guesses.")
        break
    num_guesses += 1
    if guess == 0:
        pass
    elif guess == 1:
        circuit.x(0)
    elif guess == 2:
        circuit.x(1)
    elif guess == 3:
        circuit.x(0)
        circuit.x(1)
    circuit.measure([0, 1], [0, 1])
    backend = qiskit.Aer.get_backend('qasm_simulator')
    job = qiskit.execute(circuit, backend=backend, shots=1)
    result = job.result().get_counts()
    new_guess = int(list(result.keys())[0], 2)
    print("Your guess of", guess, "was incorrect.")
    print("The quantum circuit returned", new_guess)
    circuit = qiskit.QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
