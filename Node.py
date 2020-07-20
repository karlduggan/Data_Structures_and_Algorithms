class Node(object):
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node


t1 = Node(100)
t2 = Node(300)
t3 = Node(400)
t1.set_next_node(t2)
t2.set_next_node(t3)

print(t1.get_next_node().get_next_node().get_value())