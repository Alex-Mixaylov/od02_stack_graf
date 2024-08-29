# Применение деревьев:
#
# Поисковые системы (например, двоичные деревья поиска).
# Управление структурой папок в файловых системах.
# Парсинг выражений (например, синтаксические деревья).
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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

    def print_tree(self, level=0):
        if self.right:
            self.right.print_tree(level + 1)
        print(' ' * 4 * level + '->', self.val)
        if self.left:
            self.left.print_tree(level + 1)

# Пример использования дерева
root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)

root.print_tree()
# Результат:
#     -> 14
# -> 10
#     -> 6
#         -> 3
