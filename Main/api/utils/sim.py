import time
import os
import numpy as np
import itertools
from qiskit import Aer # for local classical simulator
from qiskit import QuantumCircuit # to creat quantum circuits
from qiskit.algorithms import NumPyMinimumEigensolver # classical solver to compare
from qiskit.utils import QuantumInstance # to modify transpiler options for simulator
from qiskit.algorithms import QAOA # VQE algorithm
from qiskit_optimization.algorithms import MinimumEigenOptimizer # find Minimum
from qiskit.algorithms.optimizers import COBYLA, POWELL # the optimizer
import qiskit_optimization as qo # for making quadratic programs
import qiskit_optimization.converters as qubo_convert
# from braket.circuits import Circuit
# from braket.devices import LocalSimulator

def getskilldata(pep,skill):
    ret = np.zeros(len(pep))
    for ii,idx in enumerate(pep):
        for idx2 in pep[idx]:
            if idx2 == skill:
                ret[ii] = pep[idx][idx2]
    return ret

def qubo_form(data):
    qp = qo.QuadraticProgram()
    volunters, aid_providers = data
    peo_len, pro_len = len(volunters), len(aid_providers)
    qp.binary_var_dict([f'{j}{i}' for j in range(0,pro_len) for i in range(0,peo_len)])
    for idx in range(peo_len):
        constraint_vars = np.insert(np.zeros((pro_len,peo_len-1)), idx, np.ones(pro_len), axis=1)
        qp.linear_constraint(constraint_vars.flatten(),'=',rhs=1,name=f'nd{idx}')
    tot_sum = np.array([])
    for work in aid_providers:
        linear = -2*len(aid_providers[work][1])*np.ones(len(volunters))
        for skill in aid_providers[work][1]:
            linear += (aid_providers[work][1][skill] - getskilldata(volunters,skill))
        tot_sum = np.append(tot_sum, linear*aid_providers[work][0])
    qp.maximize(constant = 0, linear = tot_sum)
    QUBO = qubo_convert.QuadraticProgramToQubo()
    qp2 = QUBO.convert(qp)
    return qp2

def qaoa_solve(qubo_program,shots=1000):
    num_qubits = qubo_program.get_num_binary_vars()
    qc = QuantumCircuit(num_qubits)
    qc.h(range(num_qubits))
    # running on local simulator
    backend = Aer.get_backend('qasm_simulator')
    seed = 123
    cobyla = COBYLA(maxiter=500)
    quantum_instance = QuantumInstance(backend=backend, shots=shots, seed_simulator=seed, seed_transpiler=seed)
    qaoa_mes = QAOA(optimizer=cobyla, reps=3, quantum_instance=quantum_instance, initial_state = qc)
    qaoa = MinimumEigenOptimizer(qaoa_mes)
    result = qaoa.solve(qubo_program)
    return result

def bin2dict(data,result):
    volunters, aid_providers = data
    assignments = {}
    for idx, projects in enumerate(aid_providers):
        idxes = np.nonzero(result[idx])[0]
        assignments[projects] = [list(volunters.keys())[idx] for idx in idxes]
    return assignments

def main(volunters, aid_providers, run_quantum = False):
    qp = qubo_form((volunters, aid_providers))
    if run_quantum:
        result = qaoa_solve(qp)
    else:
        exact_mes = NumPyMinimumEigensolver()
        exact_eigensolver = MinimumEigenOptimizer(exact_mes)
        result = exact_eigensolver.solve(qp)
    num_volunters = len(volunters)
    num_providers = len(aid_providers)
    assign_bin_mat = result.x.reshape(num_providers,num_volunters)
    
    return bin2dict((volunters, aid_providers), assign_bin_mat)
    

volunters = {'Anna': {'CLEANING': 2}, 'Bob': {'REPAIRING': 5, 'NURSING': 5}, 'Maria': {'COOKING': 3}, 'Ahmed':{'CLEANING':3}}
aid_providers = {'NGO1': (10, {'CLEANING': 3}),
  'NGO2': (15, {'REPAIRING': 3, 'CLEANING': 2}),
  'NGO3': (20, {'COOKING': 3, 'REPAIRING': 3})}

print(main(volunters, aid_providers, False))

# main(volunters, aid_providers, True)