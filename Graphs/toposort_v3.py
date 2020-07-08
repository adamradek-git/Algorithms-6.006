graph = {
	0:[9,7,11],
	1:[8],
	2:[12],
	3:[2,4],
	4:[],
	5:[],
	6:[5],
	7:[3,6],
	8:[12],
	9:[8,10],
	10:[1],
	11:[7],
	12:[]
}

def toposort(graph):
	# the index represents whether the number node has been visited
    visited = [False for i in range(len(graph))]
    #this stores the order
    result = []

    def DFS(node):
    	if visited[node]:
    		return
    	visited[node] = True
    	# once this is not activated it does to result.append
    	for adj in graph[node]:
    		DFS(adj)
    	result.append(node)
    """
    this makes sure no sub tree is left out.
    Most times it will terminate bc visited = True
    """
    for i in range(len(graph)):
    	DFS(i)

    return result

print(toposort(graph))
	