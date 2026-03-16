class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
    def __repr__(self):
        return f"Node(Durum: {self.state})"

class StackFrontier:
    def __init__(self):
        self.frontier = []
    def add(self, node):
        self.frontier.append(node)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise Exception("Hata: Frontier boş.")
        node = self.frontier.pop()
        return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Hata: Frontier boş.")
        node = self.frontier.pop(0)
        return node

def main():

    node1 = Node("Başlangıç (A)", None, None)
    node2 = Node("Orta Nokta (B)", node1, "Sağa git")
    node3 = Node("Hedef (C)", node2, "Sola git")
    print("StackFrontier (LIFO - Son giren ilk çıkar)")
    stack = StackFrontier()
    stack.add(node1)
    stack.add(node2)
    stack.add(node3)
    print("1. Çıkarılan:", stack.remove())
    print("2. Çıkarılan:", stack.remove())

    print("QueueFrontier (FIFO - İlk giren ilk çıkar)")
    queue = QueueFrontier()
    queue.add(node1)
    queue.add(node2)
    queue.add(node3)
    print("1. Çıkarılan:", queue.remove())
    print("2. Çıkarılan:", queue.remove())

if __name__ == "__main__":
    main()