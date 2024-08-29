
# Стеки это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out, LIFO)
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())

# Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()
print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())

# class Node(): - деревья. Корневой узел называется root node, его потомки — дети, и они также могут быть родителями для других узлов.
# Бинарное дерево — это вид дерева, в котором каждый узел имеет не более двух потомков.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Функция для добавления нового узла
    def insert(self, key):
        if self.val < key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)
        else:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)
        return self

    # Функция для вывода дерева с отступами
    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level + 1)
        print(' ' * 4 * level + '->', self.val)
        if self.left:
            self.left.print_tree(level + 1)

# Создаем корневой узел и добавляем узлы
root = Node(70)
root.insert(30)
root.insert(56)
root.insert(89)
root.insert(45)
root.insert(60)
root.insert(73)
root.insert(98)
root.insert(84)

# Выводим структуру дерева
root.print_tree()

# Graph  Граф — это структура данных, состоящая из множества узлов, то есть вершин, и множества рёбер, которые соединяют пары узлов.

class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()