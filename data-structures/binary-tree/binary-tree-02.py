# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/
from queue import Queue


class BinaryTree:
	
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

	def insert_left(self, value):
		if self.left_child == None:
			self.left_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.left_child = self.left_child
			self.left_child = new_node

	def insert_right(self, value):
		if self.right_child == None:
			self.right_child = BinaryTree(value)
		else:
			new_node = BinaryTree(value)
			new_node.right_child = self.right_child
			self.right_node = new_node

	# depth-first search
	def pre_order(self):
		print(self.value)

		if self.left_child:
			self.left_child.pre_order()

		if self.right_child:
			self.right_child.pre_order()

	# depth-first search
	def in_order(self):
		if self.left_child:
			self.left_child.in_order()

		print(self.value)

		if self.right_child:
			self.right_child.in_order()

	# depth-first search
	def post_order(self):
		if self.left_child:
			self.left_child.post_order()

		if self.right_child:
			self.right_child.post_order()

		print(self.value)

	# breadth-first search
	def bfs(self):
		queue = Queue()
		queue.put(self)

		while not queue.empty():
			current_node = queue.get()
			print(current_node.value)

			if current_node.left_child:
				queue.put(current_node.left_child)

			if current_node.right_child:
				queue.put(current_node.right_child)



# Test 01
tree = BinaryTree('a')
print(tree.value)
print(tree.left_child)
print(tree.right_child)

# Test 02
a_node = BinaryTree('a')
a_node.insert_left('b')
a_node.insert_right('c')

b_node = a_node.left_child
b_node.insert_right('d')

c_node = a_node.right_child
c_node.insert_left('e')
c_node.insert_right('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

for ch in 'abcdef':
	exec(f'print({ch}_node.value)')

a_node.pre_order()
a_node.bfs()
