import networkx as nx
from matplotlib import pyplot as plt
from qiskit.visualization import *
from task1 import *
from utilities import *
from mixer_utilities import *

# create graph
G = nx.Graph()
G.add_nodes_from([0, 1])
G.add_edges_from([(0, 1)])
nx.draw(G)
plt.show()

# set parameters
params = {'G' : G, "usebarrier" : True}

def test1():
    """
    initial: hadamard
    mixer: X mixer
    results: "00" and "11" is the most probable states as expected. ok
    """
    qaoa = QAOAtest1()
    qaoa.createCircuit(np.array((np.pi, np.pi)), 1, params = params).draw(output = "mpl")
    plt.show()

    qasmSim = Aer.get_backend("qasm_simulator")
    for i in range(2):
        qaoa.increase_depth(qasmSim, 1024, params = params)

    hist = qaoa.hist(qaoa.angles_hist['d2_final'], qasmSim, 1024, params = params)
    plot_histogram(hist)
    plt.show()
    plt.plot(qaoa.costval.values())
    plt.show()

def test2():
    """
    initial: superpos of one hot (Wn)
    mixer: 0.5(XX + YY) 
    results: only mixing of "01" and "10" -> "01" becomes the most probable and has lowest cost. ok
    """
    qaoa = QAOAtest2()
    qaoa.createCircuit(np.array((np.pi, np.pi)), 1, params = params).draw(output = "mpl")
    plt.show()

    qasmSim = Aer.get_backend("qasm_simulator")
    for i in range(2):
        qaoa.increase_depth(qasmSim, 1024, params = params)

    hist = qaoa.hist(qaoa.angles_hist['d2_final'], qasmSim, 1024, params = params)
    plot_histogram(hist)
    plt.show()
    plt.plot(qaoa.costval.values())
    plt.show()

def test3():
    """
    initial: hadamard
    mixer: X
    penalty term: from get_g(), makes "11" preferred over "00"
    results: change alpha inside QAOAtest3 class
             alpha = 10 -> almost 50% "11" and 50% "00", to low alpha
             alpha = 100 -> almost 100% "11", almost correct alpha
             alpha = 1000 -> almost 50% "11" and 50% "00", to high alpha 
    """
    g = get_g(["01", "10", "11"])

    qaoa = QAOAtest3()
    qaoa.createCircuit(np.array((np.pi, np.pi)), 1, params = params).draw(output = "mpl")
    plt.show()

    qasmSim = Aer.get_backend("qasm_simulator")
    for i in range(1):
        qaoa.increase_depth(qasmSim, 1024, params = params)

    hist = qaoa.hist(qaoa.angles_hist['d1_final'], qasmSim, 1024, params = params)
    plot_histogram(hist)
    plt.show()

def test4():
    """
    initial: hadamard
    mixer: X mixer
    penalty term: H_pen matrix which affects "11" (H_problem = H_c + alpha*H_pen)
    results: alpha = 10 -> "00" becomes almost 100% probable. good
             alpha = 1 -> almost equal probability between "00" and "11" 
             alpha = 100 -> almost equal probability between "00" and "11" 
    """
    H_c = np.diag([-5., 1., 2., -5.])
    alpha = 100.0
    H_pen = np.diag([0., 0., 0., alpha])
    qaoa = QAOAtest4()
    print(decompose2_IZ(H_c + H_pen))

    qaoa.createCircuit(np.array((np.pi, np.pi)), 1, params = params).draw(output = "mpl")
    plt.show()

    qasmSim = Aer.get_backend("qasm_simulator")
    for i in range(1):
        qaoa.increase_depth(qasmSim, 1024, params = params)

    hist = qaoa.hist(qaoa.angles_hist['d1_final'], qasmSim, 1024, params = params)
    plot_histogram(hist)
    plt.show()
