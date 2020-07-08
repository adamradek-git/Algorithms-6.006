# Khan's Algorithm - not working

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

new_graph = graph

def delete(graph, value):
	for node in graph:
		for key in graph[node]:
			if key == value:
				graph[node].remove(key)

def khans(graph, start):
	g = len(graph) 
	result = []

	current_layer = []
	visited = [None for i in range(len(graph))]

	def find_end(graph, node):
		visited[node] = True
		if graph[node] == []:
			current_layer.append(node) 
			return node
		for neighbour in graph[node]:
			if visited[neighbour] == None:
				find_end(graph, neighbour)

	while len(result) <= g-1: 
		find_end(graph, start)
		for element in current_layer:
			result.append(element)
			delete(graph, element)
		current_layer = []

	return result
		


print(khans(new_graph, 0))








