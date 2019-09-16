# https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/
"""
A Binary Search Tree is sometimes called ordered or sorted binary trees, and it keeps its values in sorted order, so that lookup and other operations can use the principle of binary search
"""


class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.right_child = None

	def insert_node(self, value):
		if value <= self.value and self.left_child:
			self.left_child.insert_node(value)
		elif value <= self.value:
			self.left_child = BinarySearchTree(value)
		elif value > self.value and self.right_child:
			self.right_child.insert_node(value)
		else:
			self.right_child = BinarySearchTree(value)

	def find_node(self, value):
		if value < self.value and self.left_child:
			return self.left_child.find_node(value)
		if value > self.value and self.right_child:
			return self.right_child.find_node(value)

		return value == self.value

	def remove_node(self, value, parent):
		if value < self.value and self.left_child:
			return self.left_child.remove_node(value, self)
		elif value < self.value:
			return False
		elif value > self.value and self.right_child:
			return self.right_child.remove_node(value, self)
		elif value > self.value:
			return False
		else:
			if self.left_child is None and self.right_child is None and self == parent.left_child:
				parent.left_child = None
				self.clear_node()
			elif self.left_child is None and self.right_child is None and self == parent.right_child:
				parent.right_child = None
				self.clear_node()
			elif self.left_child and self.right_child is None and self == parent.left_child:
				parent.left_child = self.left_child
				self.clear_node()
			elif self.left_child and self.right_child is None and self = parent.right_child:
				parent.right_child = self.left_child
				self.clear_node()
			elif self.rigth_child and self.left_child is None and self == parent.left_child:
				parent.left_child = self.right_child
				self.clear_node()
			elif self.right_child and self.left_child is None and self == parent.right_child:
				parent.right_child = self.right_child
				self.clear_node()
			else:
				self.value = self.right_child.find_minimum_value()
				self.right_child.remove_node(self.value, self)

			return True

	def clear_node(self):
		self.value = None
		self.left_child = None
		self.rigth_child = None

	def find_minimum_value(self):
		if self.left_child:
			return self.left_child.find_minimum_value()
		else:
			return self.value








bst = BinarySearchTree(15)

bst.insert_node(10)
bst.insert_node(8)
bst.insert_node(12)
bst.insert_node(20)
bst.insert_node(17)
bst.insert_node(25)
bst.insert_node(19)

print(bst.find_node(0))
