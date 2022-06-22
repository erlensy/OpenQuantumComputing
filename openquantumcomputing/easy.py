from utilities import *
from qiskit import *
import numpy as np
from openquantumcomputing.QAOABase import QAOABase
from QAOABase import *

class QAOAtest(QAOABase):

    def cost(self, string, params):
        C = 5
        if string == "01":
            C = -1
        elif string == "10":
            C = -2
        return C

    def createCircuit(self, angles, depth, params={}):
        G = params.get('G', None)
        usebarrier = params.get('usebarrier', False)
        name= params.get('name', "")

        num_V = G.number_of_nodes()

        q = QuantumRegister(num_V)
        c = ClassicalRegister(num_V)
        circ = QuantumCircuit(q, c, name=name)

        # initial state
        # one-hot
        Wn(circ, [0, 1])

        # binary
        #circ.h([q[0], q[1]])

        if usebarrier: 
            circ.barrier()

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
            # xx + yy mixer
            #circ.h([q[0], q[1]])
            #circ.cx(q[0], q[1])
            #circ.rz(-beta, q[1])
            #circ.cx(q[0], q[1])
            #circ.h([q[0], q[1]])
            #circ.s([q[0], q[1]])
            #circ.h([q[0], q[1]])
            #circ.cx(q[0], q[1])
            ##circ.rz(-beta, q[1])
            #circ.cx(q[0], q[1])
            #circ.h([q[0], q[1]])
            #circ.sdg([q[0], q[1]])
            
            #circ.rxx(-beta, q[0], q[1])
            #circ.ryy(-beta, q[0], q[1])
               
            # x mixer
            circ.rx(-2.*beta, [q[0], q[1]])

        circ.measure(q, c)
        return circ
