# Quantum Dice Roll API
# Austin Alberd 
# 06/25/2025



# Library Imports
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

from flask import Flask, request, render_template
from flask_cors import CORS


# Quantum Stuff
#Custom Functions
def rollDice(transpiled_circuit):
    roll = 25
    while roll > 20 or roll == 0:
        result = aer_simulator.run(transpiled_circuit,shots = 1).result().get_counts()
        roll=int(list(result.keys())[0],2)
    return roll
    
#Generate the quantum circuit
qc = QuantumCircuit(5)
qc.h(range(5))
qc.measure_all()

# Transpile and such
aer_simulator = Aer.get_backend("aer_simulator")
transpiled_circuit = transpile(qc,aer_simulator)

print(rollDice(transpiled_circuit=transpiled_circuit))

#API Stuff
app = Flask(__name__)
CORS(app,origins=["*"])


@app.route('/api/rollDie', methods = ["GET"])
def rollDieEndpoint():
    if request.method == "GET":
        return f"<h2>Your Result Is: {str(rollDice(transpiled_circuit=transpiled_circuit))}<h2>"
    
@app.route('/', methods = ["GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=80)