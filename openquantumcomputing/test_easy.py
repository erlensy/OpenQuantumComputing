import networkx as nx
from matplotlib import pyplot as plt
from qiskit.visualization import *
from easy import *

# find H_c
def tp(A, B, C):
    return np.kron(np.kron(A, B), C)

X = np.matrix([[0, 1], [1, 0]])
Y = np.matrix([[0, -1j], [1j, 0]])
Z = np.matrix([[1, 0], [0, -1]])
I = np.matrix([[1, 0], [0, 1]])

H_c = 0.5*np.kron(I - Z, I + Z) + 1/4*np.kron(I + Z, I - Z) - 5/4 * np.kron(I - Z, I - Z) - 5/4 * np.kron(I + Z, I + Z)

# create graph
G = nx.Graph()
G.add_nodes_from([0, 1])
G.add_edges_from([(0, 1)])
nx.draw(G)
plt.show()

# set parameters
params = {'G' : G, "usebarrier" : True}
qaoa = QAOAtest()

angles = np.array((np.pi, np.pi)) 
a = qaoa.createCircuit(angles, 1, params = params)
a.draw(output = "mpl")
plt.show()

#transpile(a, basis_gates = ["rz", "h", "s", "sdg", "cx"]).draw(output = "mpl")
#plt.show()

qasmSim = Aer.get_backend("qasm_simulator")

for i in range(3):
    qaoa.increase_depth(qasmSim, 1024, params = params)

hist = qaoa.hist(qaoa.angles_hist['d3_final'], qasmSim, 1024, params = params)

plot_histogram(hist)
plt.show()

plt.plot(qaoa.costval.values())
plt.show()
