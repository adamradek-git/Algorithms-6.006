import math 

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

# Attempt 1
def BFS_shortest_path(start, final, graph):
	dist = [math.inf for i in range(len(graph))]
	current_nodes = []
	pointer = 0
	counter = 0
	current_nodes.append(start)
	dist[start] = 0
	while pointer < len(graph): 
		counter += 1 # this mechanism not working
		for node in graph[current_nodes[pointer]]:
			current_nodes.append(node)
			if counter < dist[node]:
				dist[node] = counter
		print(current_nodes)
		pointer += 1
	return dist[final]

# Attempt 2 (shortest path algorithm using BFS)
def BFS_path(start, final, graph):
	dist = [math.inf for i in range(len(graph))]
	parent_nodes = [None for i in range(len(graph))]
	parent_nodes[start] = 0
	current_nodes = []
	pointer = 0
	dist[start] = 0
	current_nodes.append(start)
	while pointer < len(graph):
		for node in graph[current_nodes[pointer]]:
			current_nodes.append(node)
			parent_nodes[node] = current_nodes[pointer]
			if dist[node] > dist[parent_nodes[node]] + 1:
				dist[node] = dist[parent_nodes[node]] + 1
		pointer += 1
	print(parent_nodes)
	return dist


print(BFS_path(0, 12, graph))
