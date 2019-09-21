# http://www.quesucede.com/page/show/id/python-3-tree-implementation


class Node:
	def __init__(self, identifier):
		self._identifier = identifier
		self._children = []

	@property
	def identifier(self):
		return self._identifier

	@property
	def children(self):
		return self._children

	def add_child(self, identifier):
		self._children.append(identifier)


(_ROOT, _DEPTH, _BREADTH) = range(3)


class Tree:
	def __init__(self):
		self._nodes = {}

	@property
	def nodes(self):
		return self._nodes

	def add_node(self, identifier, parent=None):
		node = Node(identifier)
		self[identifier] = node

		if parent is not None:
			self[parent].add_child(identifier)

		return node

	def display(self, identifier, depth=_ROOT):
		children = self[identifier].children
		if depth == _ROOT:
			print(f'{identifier}')
		else:
			print('\t'*depth, '{}'.format(identifier))

		depth += 1
		for child in children:
			self.display(child, depth)

	def traverse(self, identifier, mode=_DEPTH):
		yield identifier
		queue = self[identifier].children
		while queue:
			yield queue[0]
			expansion = self[queue[0]].children
			if mode == _DEPTH:
				queue = expansion + queue[1:]  # depth-first
			elif mode == _BREADTH:
				queue = queue[1:] + expansion  # width-first

	def __getitem__(self, key):
		return self._nodes[key]

	def __setitem__(self, key, item):
		self._nodes[key] = item


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
for node in tree.traverse('Harry', mode=_BREADTH):
	print(node)
















