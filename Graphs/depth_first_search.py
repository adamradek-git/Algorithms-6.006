
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

def get_neighbours(location, graph):
	neighbours = []
	for node in graph[location]:
		neighbours.append(node)
	return neighbours

# this graph searches from the location that is specified 
def BFS(location, graph): 
	visited = []
	pointer = 0
	visited.append(location)
	while pointer < len(visited): 
		for node in graph[visited[pointer]]:
			if node not in visited: 
				visited.append(node)
		pointer += 1
	return visited

# must also implement a depth first search algorithm

node_visited = []

def DFS(location, graph, visited = None): 
	if visited == None: 
		visited = [False for i in range(len(graph))]
	if visited[location] == True:
		return
		
	visited[location] = True
	node_visited.append(location)

	for node in graph[location]:
		DFS(node, graph, visited)
	return visited


DFS(0,graph)
print(node_visited)









