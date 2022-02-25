from Tree import Tree
from Menu import Menu
from Console import Console
from Node import Node


class TreeManagement:
    def __init__(self) -> None:
        self.__tree: Tree = Tree()
        self.__menu: Menu = Menu(
            "Gestión de árboles",
            [
                "Ingreso de nodos",
                "Actualización de nodos",
                "Eliminación de nodos",
                "Buscar nodo",
                "Mostrar",
                "Salir",
            ],
        )

    def interact(self):
        self.__menu.interact()
        while not self.__menu.is_option_exit():
            if self.__menu.is_option(1):
                self.__set_nodes()
            if self.__menu.is_option(2):
                self.__update_nodes()
            if self.__menu.is_option(3):
                self.__delete_nodes()
            if self.__menu.is_option(4):
                self.__search()
            if self.__menu.is_option(5):
                self.__show_tree()

            self.__menu.interact()

    def __set_nodes(self) -> None:
        is_exit = False
        while not is_exit:
            node = Node(Console.read_str(f"Nombre: "), Console.read_int(f"Costo: "))
            if not self.__exists(node):
                self.__tree.add(node)
            self.__tree.show()
            is_exit = not Console.is_yes("¿Deseas añadir mas nodos?(Y/n): ")

    def __update_nodes(self) -> None:
        menu = Menu("Actualización de nodos", self.__options())
        menu.interact()
        while not menu.is_option_exit():
            node = self.__get_node(menu.get_option())
            print(f"Actualizar datos del nodo '{node}'")
            new_node = Node(Console.read_str(f"Nombre: "), node.get_cost())
            if not self.__exists(new_node):
                node.set_name(new_node.get_value())
            self.__show_tree()
            menu.interact()

    def __delete_nodes(self) -> None:
        menu = Menu("Eliminacion de nodos", self.__options())
        menu.interact()
        while not menu.is_option_exit():
            node = self.__get_node(menu.get_option())
            self.__tree.show()
            if Console.is_yes(f"¿Estás seguro de eliminar el nodo '{node}'? (Y/n): "):
                self.__tree.delete(node)
                menu = Menu("Eliminacion de nodos", self.__options())
                self.__show_tree()
            menu.interact()

    def __search(self) -> None:
        if self.__tree.contains(Node(Console.read_str("Nombre: "), 0)):
            input("Se ha encontrado el nodo!!!!")
        else:
            input("No se ha encontrado el nodo!!!!")

    def __options(self) -> list[str]:
        result = []
        for i in self.__tree.get_nodes():
            if i != "Volver":
                result.append(i)
        result.append("Volver")
        return result

    def __show_tree(self) -> None:
        self.__tree.show()
        input()

    def __exists(self, node: Node) -> bool:
        return self.__tree.contains(node)

    def __get_node(self, position: int) -> Node:
        return self.__tree.get_node(position - 1)


TreeManagement().interact()
