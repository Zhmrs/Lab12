from model.model import Model
from database.dao import DAO

model=Model()
dao=DAO()
result=dao.readConnessioniAnno(2000)
print(result[0])

# a=dao.readRifugi()
# print(a)

c=model.build_weighted_graph(2000)
archi=len(model.G.edges())
nodi=len(model.G.nodes())
print('NODI',nodi)
print('ARCHI',archi)
print('peso',model.G[1][2]['peso'])

pesi_min,pesi_max=model.get_edges_weight_min_max()
print('PESI', pesi_min, pesi_max)


minori,maggiori=model.count_edges_by_threshold(4)
print('MINOR',minori)
print('MAGGIORI',maggiori)

# grafo=model.G
# print('GRAFO',len(list(grafo))) # mi conta il numero di nodi presenti nel grafo

g=model.cammino_minimo_nx(4)
print('grafo', g)
