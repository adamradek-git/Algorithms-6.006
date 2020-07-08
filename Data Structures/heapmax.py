class heapmax:
	def __init__(self, heap):
		self.heap = heap

	def get_left_child(self, p_index):
		return 2*(p_index+1)-1

	def get_right_child(self, p_index):
		return 2*(p_index+1)

	def get_parent(self, c_index): 
		return (c_index +1)//2 -1

	def get_max(self):
		return self.heap[0]

	def add(self, value):
		self.heap.append(value)

	def heapify_up(self):
		start = len(self.heap)-1
		while self.get_parent(start) >= 0:
			added = self.heap[start]
			parent = self.heap[self.get_parent(start)]
			if added > parent: 
				pp = self.heap[self.get_parent(start)]
				self.heap[self.get_parent(start)] = added
				self.heap[start] = pp
			start = self.get_parent(start)

# Technical Testing 

heap = heapmax([8,6,5,3,2,1,1,1,1,9])
heap.heapify_up()
print(heap.get_max())


