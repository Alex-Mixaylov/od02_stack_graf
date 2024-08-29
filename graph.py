
# Применение графов:
#
# Социальные сети, где узлы представляют пользователей, а рёбра – их связи.
# Маршрутизация в сети (например, алгоритмы поиска кратчайшего пути).
# Представление дорог и транспортных систем.

#коде для реализации графа и обхода его в ширину (BFS — Breadth-First Search).
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Метод bfs выполняет обход графа в ширину (Breadth-First Search), начиная с вершины start.
    #
    # Инициализация:
    # visited — множество, которое хранит уже посещенные вершины, чтобы избежать повторного посещения.
    # queue — очередь, в которую добавляются вершины, которые нужно посетить.
    # В начале обхода стартовая вершина start добавляется в очередь и отмечается как посещенная.
    #
    # Основной цикл:
    # Пока очередь не пуста, извлекается вершина vertex из начала очереди и выводится на экран.
    # Затем программа проверяет всех соседей текущей вершины (neighbor).
    # Если сосед еще не посещен, он добавляется в очередь и помечается как посещенный.

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Пример использования графа
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)  # Результат: 2 0 3 1
