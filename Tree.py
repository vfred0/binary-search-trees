from Direction import Direction
from Node import Node
from Draw import Draw


class Tree:
    def __init__(self) -> None:
        self.__root: Node = None
        self.__nodes: list[Node] = []

    def show(self) -> None:
        if not self.is_empty():
            print("#############")
            print("Arbol")
            self.__print(self.__root, 0)
            print("#############")
        else:
            print("El aŕbol está sin nodos!!!")

    def is_empty(self) -> bool:
        return self.__root is None

    def __print(self, node: Node, level: int) -> None:
        if node:
            for i in range(level):
                if i < (level - 1):
                    print(" |  ", end="")
                else:
                    print(" +- ", end="")

            print(node)
            level += 1
            self.__print(node.get(Direction.LEFT), level)
            self.__print(node.get(Direction.RIGHT), level)

    def add(self, node: Node) -> None:
        if not self.is_empty():
            self.__root.add(node)
        else:
            self.__root = node

    def delete(self, node: Node) -> None:
        if node.have_childrens() or node.have_parent():
            if self.contains(node):
                self.__root.delete(node)
            else:
                print("No existe!!!", node)
        else:
            self.__root = None

    def update(self, node_search: Node, value: str) -> None:
        if self.contains(node_search):
            node_search.set_name(value)
        else:
            print("No existe!!!", node_search)

    def contains(self, node: Node) -> bool:
        if not self.is_empty():
            return self.__root.find(node)
        return False

    def get_nodes(self) -> list[Node]:
        self.__nodes = []
        self.__set_nodes(self.__root)
        return self.__nodes

    def get_node(self, position: int) -> Node:
        return self.get_nodes()[position]

    def __set_nodes(self, node: Node) -> None:
        if node:
            self.__nodes.append(node)
            self.__set_nodes(node.get(Direction.RIGHT))
            self.__set_nodes(node.get(Direction.LEFT))


ss = Tree()
x = Node("1", 23)
ss.add(Node("2", 233))
ss.add(Node("2", 233))
ss.add(Node("2", 23))
ss.add(x)

ss.show()
print(ss.contains(x))
