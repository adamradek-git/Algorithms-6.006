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

# new implementation is done via https://www.youtube.com/watch?v=TvTNFOn4KcE
# working better but not working .....


def topological_sort(graph): 
	visited_stack = []
	sorted_stack = []

	available_nodes = []
	for nodes in graph:
		available_nodes.append(nodes)

	# we want this function to return true
	def availability(graph, node):
		count = 0
		for neighbour in graph[node]:
			if neighbour in available_nodes:
				count += 1
		if count != 0:
			return False
		return True

	def path_traverse(graph, visited_stack):
		for element in visited_stack:
			thing = visited_stack.pop(-1)
			if availability(graph, thing) == True:
				sorted_stack.append(thing)
				del available_nodes[thing]

		# no idea why I have to right this...
		try:
			sorted_stack.append(visited_stack[0])
			visited_stack.remove(visited_stack[0])
		except: IndexError

	def DFS(start, graph):
		print(start)
		visited_stack.append(start)
		if start in sorted_stack:
			return
		elif availability(graph, start) == True: 
			sorted_stack.append(start)
			visited_stack.pop(-1)
			del available_nodes[start]
			
			# add analysis of visited stack from the back
			path_traverse(graph, visited_stack)

			print(sorted_stack)
			print(visited_stack)

		else:
			for neighbours in graph[start]:
				DFS(neighbours, graph)

	DFS(11,graph)





print(topological_sort(graph))

