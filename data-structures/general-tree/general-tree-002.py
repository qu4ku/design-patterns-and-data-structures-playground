# http://www.quesucede.com/page/show/id/python-3-tree-implementation
# refactored / minimalized for a better understanding

class Node:
	def __init__(self, identifier):
		self.identifier = identifier
		self.children = []

	def add_child(self, identifier):
		self.children.append(identifier)


(_ROOT, _DEPTH, _BREADTH) = range(3)


class Tree:
	def __init__(self):
		self.nodes = {}

	def add_node(self, identifier, parent=None):
		node = Node(identifier)
		self.nodes[identifier] = node

		if parent is not None:
			self.nodes[parent].add_child(identifier)

		return node

	def display(self, identifier, depth=_ROOT):
		children = self.nodes[identifier].children
		if depth == _ROOT:
			print(f'{identifier}')
		else:
			print('\t'*depth, '{}'.format(identifier))

		depth += 1
		for child in children:
			self.display(child, depth)

	def traverse(self, identifier, mode='depth'):
		yield identifier
		queue = self.nodes[identifier].children
		while queue:
			yield queue[0]
			expansion = self.nodes[queue[0]].children
			if mode == 'depth':
				queue = expansion + queue[1:]  # depth-first
			elif mode == 'breadth':
				queue = queue[1:] + expansion  # width-first


tree = Tree()

tree.add_node("Harry")  # root node
tree.add_node("Jane", "Harry")
tree.add_node("Bill", "Harry")
tree.add_node("Kamil", "Harry")
tree.add_node("Joe", "Jane")
tree.add_node("Diane", "Jane")
tree.add_node("George", "Diane")
tree.add_node("Mary", "Diane")
tree.add_node("Jill", "George")
tree.add_node("Carol", "Jill")
tree.add_node("Grace", "Bill")
tree.add_node("Mark", "Jane")

tree.display('Harry')
print('*** depth-first iteration ***')
for node in tree.traverse('Harry'):
	print(node)

print('*** depth-first iteration ***')
for node in tree.traverse('Harry', mode='breadth'):
	print(node)
















