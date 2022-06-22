import networkx as nx
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import pyplot as plt
from qiskit.visualization import *
from find_error import *
from scipy.optimize import minimize

# create graph
numV = 14
G = nx.read_gml("../../data/sample_graphs/w_ba_n"+str(numV)+"_k4_0.gml")
nx.draw(G, pos = nx.spring_layout(G))
plt.show()

# set parameters
params = {'G' : G, "usebarrier" : False}
qaoa = QAOAfindError()

#angles = np.array((np.pi, np.pi)) 
#qaoa.createCircuit(angles, 1, params = params).draw(output = "mpl")
#plt.show()

qasmSim = Aer.get_backend("qasm_simulator")


#f = plt.figure(figsize=(6, 6), dpi= 80, facecolor='w', edgecolor='k');
#plt.xlabel(r'$\gamma$')
#plt.ylabel(r'$\beta$')
#ax = plt.gca()
#plt.title('Expectation value')
#im = ax.imshow(qaoa.E,interpolation='bicubic',origin='lower',extent=[0,np.pi/2,0,np.pi])
#divider = make_axes_locatable(ax)
##cax = divider.append_axes("right", size="5%", pad=0.05)
#plt.colorbar(im, cax=cax)
#plt.show()

#for i in range(3):
#    qaoa.increase_depth(qasmSim, 1024*2, params = params)

#hist = qaoa.hist(qaoa.angles_hist['d3_final'], qasmSim, 8192, params = params)
#
#plot_histogram(hist)
#plt.show()
#
#plt.plot(qaoa.costval.values())
#plt.show()

def compute_expectation(counts, G):

    avg = 0
    sum_count = 0
    for bitstring, count in counts.items():

        obj = qaoa.cost(bitstring, params)
        avg += obj * count
        sum_count += count

    return -avg/sum_count

def get_expectation(G, p, shots=1024):

    qasmSim.shots = shots
    
    def execute_circ(angles):
        
        qc = qaoa.createCircuit(angles, p, params)
        counts = qasmSim.run(qc, nshots=1024).result().get_counts()
        
        return compute_expectation(counts, G)
    
    return execute_circ

#qaoa.sample_cost_landscape(qasmSim, 1024, params=params, angles={"gamma": [0,np.pi/2,10], "beta": [0,np.pi,20]})
#ind_Emin = np.unravel_index(np.argmin(qaoa.E, axis=None), qaoa.E.shape)
#angles0=np.array((qaoa.gamma_grid[ind_Emin[1]], qaoa.beta_grid[ind_Emin[0]]))
#res = minimize(get_expectation(G, p = 1), angles0, method = 'COBYLA')
#angles = np.zeros(4)
#angles[::2] = qaoa.interp(res.x[::2])
#angles[1::2] = qaoa.interp(res.x[1::2])
for i in range(100):
    angles = np.random.rand(4)*4*np.pi - 2*np.pi
    res = minimize(get_expectation(G, p = 2), angles, method = 'COBYLA')
    print(f"fun: {res.fun}, x: {res.x}")
