import math 

graph = {
	'a':{'b':3,'c':4, 'd':7},
	'b':{'c':1,'f':5},
	'c':{'f':6,'d':2},
	'd':{'e':3, 'g':6},
	'e':{'g':3, 'h':4},
	'f':{'e':1, 'h':8},
	'g':{'h':2},
	'h':{'g':2}
}

def dijkstra(start, end, graph): 
	shortest_distance = {}
	track_predecessor = {} 
	unseenNodes = graph 
	infinity = math.inf 
	track_path = []

	for node in unseenNodes:
		shortest_distance[node] = infinity
	shortest_distance[start] = 0

# we are deriving our next target "shortest distance"
	while unseenNodes:
		min_distance_node = None
		for node in unseenNodes: 
			if min_distance_node is None: # during the first iteration
				min_distance_node = node
			elif shortest_distance[node] < shortest_distance[min_distance_node]:
				min_distance_node = node

		path_options = graph[min_distance_node].items()

		# relaxing the children node 
		for child_node, weight in path_options: 
			if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]: 
				shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
				track_predecessor[child_node] = min_distance_node

		unseenNodes.pop(min_distance_node)

	return shortest_distance


print(dijkstra('a','h', graph))
