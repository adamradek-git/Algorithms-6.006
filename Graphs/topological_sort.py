graph1 = {
	2: {11},
	9: {11, 8, 10},
	10: {11, 3},
	11: {7, 5},
	8: {7, 3},
}

from toposort import toposort, toposort_flatten

#print(list(toposort_flatten(graph)))

# my attempt, this is a DAG

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



def topological_sort(location, graph, visited = None):
	node_visited = []
	node_completed = [False for i in range(len(graph))]
	order = []

	def neighbour_check(node_completed, node, graph): 
		count = 0
		for neighbours in graph[node]: 
			if node_completed[neighbours] == True:
				count += 1
		if count == len(graph[node]):
			return True
		return False

	def DFS(location, graph, visited = None):
		if visited == None: 
			visited = [False for i in range(len(graph))]
		if visited[location] == True:
			return
			
		visited[location] = True
		node_visited.append(location)

		print(location)
		print(node_completed)

		if graph[location] == []:
			order.append(node)
			node_completed[location] == True
		else:
			for node in graph[location]:
				if neighbour_check(node_completed, node, graph) == True:
					order.append(node)
					node_completed[location] == True
				else:
					DFS(node, graph, visited)

		return "complete"

	DFS(location, graph)

	return order


print(topological_sort(0, graph))











