from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes

def BFS(G,u):
        L = []
        discovered = dict()
        discovered[u] = True
        nodos = list(G.nodes.keys())
        for n in nodos:
                if u != n:
                        discovered[n] = False
        
        g = Graph()
        g.addNode(u)
        L0 = [u]
        g.addNode(u)
        L.append(L0)
        Li = L0*1
        while len(Li) != 0:
                Lii = []
                for u in Li:
                        D = G.getNode(u).neighboors 
                        for v in D:
                                if discovered[v] == False:
                                        discovered[v] = True
                                        g.addNode(v)
                                        g.addEdge(u + '->' + v,u,v)
                                        Lii.append(v)
                L.append(Lii)
                Li = Lii*1

        return g

#g1 = randomErdosRenyi(500,700)
#g1.show(nombre='erdosRenyi500_700')

#g1 = randomGilbert(500,0.2)
#g1.show(nombre='gilbert500_02')

#g1 = randomGeographic(500,0.5)
#g1.show(nombre='geographic_500_0_5')

#g1 = randomBarabasiAlbert(500,3)
#g1.show(nombre='barabasiAlbert_500_3')

g1 = grid(20,5)
g1.show(nombre='grid20_25')

#g1 = dorogovtsevMendes(500)
#g1.show(nombre='dorogovtsevMendes500')

g2 = BFS(g1,'1')
g2.show(nombre='BFS_grid20_25')
