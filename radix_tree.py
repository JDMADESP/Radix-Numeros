

class node_pointers:
    def __init__(self):
        self.children = [None] * 10

class node_with_values:
    def __init__(self):
        self.values = {}

class Radix_tree:
    def __init__(self):
        self.root = None
    
    def insert(self, numeracion_node): ##Important NIR, SERIE, Inicial - Numeracion Final
        if self.root == None:
            self.root = node_pointers()
        self._insert(numeracion_node, self.root)

    def _insert(self, numeracion_node, curr_root):
        for num in numeracion_node.NIR:


