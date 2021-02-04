
vertices = [1,2,3,4,5,6]
aristas  = [[1,2],[1,3],[3,4],[2,4],[4,6],[4,5],[5,6]]

def grafo_euleriano(vertices, aristas, vertice_actual=1):
	ramas = list()

	if len(aristas) == 1 and vertice_actual in aristas[0]:
		return aristas[0]

	for arista in aristas:
		if vertice_actual in arista:
			ramas.append(arista)

	if len(ramas) == 0:
		return False 

	for rama in ramas:
		#Hallar el vertice
		bifurcacion = rama.copy()
		bifurcacion.remove(vertice_actual)
		vertice_siguiente = bifurcacion[0]

		#lista de aristas sin la arista utilizada
		aristas_siguientes = aristas.copy()
		aristas_siguientes.remove(rama)

		grafo = grafo_euleriano(vertices, aristas_siguientes, vertice_siguiente)

		if grafo != False:
			return rama + grafo

	return False

print(grafo_euleriano(vertices, aristas))









