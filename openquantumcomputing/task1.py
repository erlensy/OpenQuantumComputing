from utilities import *
from qiskit import *
import numpy as np
from openquantumcomputing.QAOABase import QAOABase
from QAOABase import *

class QAOAtest1(QAOABase):

    def cost(self, string, params):
        C = -5
        if string == "01":
            C = 1
        elif string == "10":
            C = 2
        return -C

    def createCircuit(self, angles, depth, params={}):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        name= params.get('name', "")
        circ = QuantumCircuit(q, c, name=name)
        # initial state
        circ.h([q[0], q[1]])

        for d in range(depth):
            gamma = angles[2 * d]
            beta = angles[2 * d + 1]

            # cost hamiltonian
            circ.rz(2*gamma*(1./4.), q[0])

            circ.rz(2*gamma*(-1./4.), q[1])

            circ.cx(q[0], q[1])
            circ.rz(2*gamma*(13/4.), q[1])
            circ.cx(q[0], q[1])

            # mixer hamiltonian
            circ.rx(-2 * beta, q[0])
            circ.rx(-2 * beta, q[1])
            
        circ.measure(q, c)
        return circ

class QAOAtest2(QAOABase):

    def cost(self, string, params):
        C = -5
        if string == "01":
            C = 1
        elif string == "10":
            C = 2
        return -C

    def createCircuit(self, angles, depth, params={}):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        name= params.get('name', "")
        circ = QuantumCircuit(q, c, name=name)
        # initial state
        Wn(circ, [0, 1])

        for d in range(depth):
            gamma = angles[2 * d]
            beta = angles[2 * d + 1]

            # cost hamiltonian
            circ.rz(2*gamma*(-1./4.), q[0])

            circ.rz(2*gamma*(1./4.), q[1])

            circ.cx(q[0], q[1])
            circ.rz(2*gamma*(13/4.), q[1])
            circ.cx(q[0], q[1])

            # mixer hamiltonian
            circ.h([q[0], q[1]])
            circ.cx(q[0], q[1])
            circ.rz(-beta, q[1])
            circ.cx(q[0], q[1])
            circ.h([q[0], q[1]])
            circ.s([q[0], q[1]])
            circ.h([q[0], q[1]])
            circ.cx(q[0], q[1])
            circ.rz(-beta, q[1])
            circ.cx(q[0], q[1])
            circ.h([q[0], q[1]])
            circ.sdg([q[0], q[1]])
            
        circ.measure(q, c)
        return circ

class QAOAtest3(QAOABase):

    def cost(self, string, params):
        C = -5
        if string == "01":
            C = 1
        elif string == "10":
            C = 2
        return -C

    def createCircuit(self, angles, depth, params={}):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        name= params.get('name', "")
        circ = QuantumCircuit(q, c, name=name)
        # initial state
        #Wn(circ, [0, 1])
        circ.h([q[0], q[1]])

        alpha = 100.0

        for d in range(depth):
            gamma = angles[2 * d]
            beta = angles[2 * d + 1]

            # cost hamiltonian
            circ.rz(2*gamma*(-1./4.), q[0])

            circ.rz(2*gamma*(1./4.), q[1])

            circ.cx(q[0], q[1])
            circ.rz(2*gamma*(13/4.), q[1])
            circ.cx(q[0], q[1])

            # penalty hamiltonian
            circ.rz(-alpha * gamma, q[0])

            circ.rz(-alpha * gamma, q[1])

            circ.cx(q[0], q[1])
            circ.rz(-alpha * gamma, q[1])
            circ.cx(q[0], q[1])

            # mixer hamiltonian
            circ.rx(-2. * beta, q[0])
            circ.rx(-2. * beta, q[1])
            
        circ.measure(q, c)
        return circ

class QAOAtest4(QAOABase):

    def cost(self, string, params):
        C = -5
        if string == "01":
            C = 1
        elif string == "10":
            C = 2
        return -C

    def createCircuit(self, angles, depth, params={}):
        q = QuantumRegister(2)
        c = ClassicalRegister(2)
        name= params.get('name', "")
        circ = QuantumCircuit(q, c, name=name)
        # initial state
        #Wn(circ, [0, 1])
        circ.h([q[0], q[1]])

        for d in range(depth):
            gamma = angles[2 * d]
            beta = angles[2 * d + 1]

            # cost hamiltonian
            circ.rz(2*gamma*(101./4.), q[0])

            circ.rz(2*gamma*(99./4.), q[1])

            circ.cx(q[0], q[1])
            circ.rz(2*gamma*(-87./4.), q[1])
            circ.cx(q[0], q[1])

            # mixer hamiltonian
            circ.rx(-2 * beta, q[0])
            circ.rx(-2 * beta, q[1])
            
        circ.measure(q, c)
        return circ
