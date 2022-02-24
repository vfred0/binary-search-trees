from Direction import Direction
from Node import Node
from Draw import Draw


class Tree:
    def __init__(self) -> None:
        self.__root: Node = None

    def show(self) -> None:
        self.__recursive_print(self.__root, 0)

    def __recursive_print(self, node: Node, level: int) -> None:
        if node:
            for i in range(level):
                if i < (level - 1):
                    print(" |  ", end="")
                else:
                    print(" +- ", end="")

            print(node)
            level += 1
            self.__recursive_print(node.get(Direction.LEFT), level)
            self.__recursive_print(node.get(Direction.RIGHT), level)

    def add(self, node: Node) -> None:
        if self.__root:
            self.__root.add(node)
        else:
            self.__root = node

    def delete(self, node: Node) -> None:
        if self.contains(node):
            self.__root.delete(node)

    # def update(self, node_search: Node, node_update: Node) -> None:
    #     self.__root.update(node_search, node_update)

    def contains(self, node: Node) -> bool:
        return self.__root.exists(node)

    # def get_root(self) -> Node:
    #     return self.__root


tree = Tree()
tree.add(Node("A", 16))
tree.add(Node("B", 8))
tree.add(Node("C", 24))
x = Node("G", 3)
tree.add(x)
tree.add(Node("D3", 19))
tree.add(Node("D2", 13))
tree.add(Node("E", 7))
tree.add(Node("F", 21))
# tree.add(Node("H", 1))
# tree.add(Node("I", 11))
# tree.add(x)
# tree.delete(x)
tree.delete(x)
tree.show()
# print(tree.contains(Node("x", 23)))
# print(tree.contains(x))
# print(tree.contains(Node("C", 24)))
# tree.delete(Node("A", 2))


# print(x.get_parent().get_parent())
# tree.delete(Node("12"))
# tree.update(a, Node("A", 12))
# tree.get_all_nodes()
# tree.exists(Node("A"))
