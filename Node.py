from Direction import Direction
from TypesNode import TypesNode


class Node:
    def __init__(self, value: str, cost: int) -> None:
        self.__value = value
        self.__cost = cost
        self.__childrens: dict[Direction, Node] = {}
        self.__parent: Node = None
        self.__type_node: TypesNode = TypesNode.LEAF

    def add(self, children) -> None:
        if children > self:
            self.__add_to(Direction.RIGHT, children)
        elif children < self:
            self.__add_to(Direction.LEFT, children)

    def __add_to(self, direction: Direction, children) -> None:
        current_children = self.get(direction)
        if not current_children:
            self.__childrens[direction] = children
            children.__parent = self
            self.__update_type_node()
        else:
            current_children.add(children)

    def get(self, direction: Direction):
        return self.__childrens.get(direction)

    def __get_last_in(self, direction: Direction):
        if not self.__type_node.is_leaf():
            iterator = self.get(direction)
            while iterator is not None and iterator.get(direction):
                iterator = iterator.get(direction)
            if iterator:
                return iterator

        return self

    def delete(self, delete_node) -> None:
        if delete_node.__type_node.is_parent_with_two_childs():
            change_node = delete_node.get(Direction.RIGHT).__get_last_in(Direction.LEFT)
            delete_node.__value = change_node.__value
            delete_node.__cost = change_node.__cost
            self.delete(change_node)

        elif delete_node.__type_node.is_parent_with_one_child():
            change_node = list(delete_node.__childrens.values())[0]
            delete_node.__value = change_node.__value
            delete_node.__cost = change_node.__cost
            delete_node.__type_node = change_node.__type_node
            delete_node.__childrens = change_node.__childrens
            delete_node.__update_type_node()

        else:
            direction = delete_node.__parent.get_direction(delete_node)
            del delete_node.__parent.__childrens[direction]
            delete_node.__parent.__update_type_node()

    def get_direction(self, node):
        for direction, _node in self.__childrens.items():
            if _node == node:
                return direction
        return None

    def __update_type_node(self):
        self.__type_node = TypesNode.get(self.__childrens.__len__())

    def find(self, node) -> bool:
        find = self == node
        if not find:
            if node > self:
                check = self.get(Direction.RIGHT)
            else:
                check = self.get(Direction.LEFT)
            if check:
                return check.find(node)
        return find

    def have_parent(self) -> bool:
        return self.__parent

    def have_childrens(self) -> bool:
        return self.__childrens

    def get_value(self) -> str:
        return self.__value

    def get_cost(self) -> str:
        return self.__cost

    def set_name(self, name: str) -> None:
        self.__value = name

    def __str__(self) -> str:
        result = f"{self.__value}: {self.__cost} {self.__type_node} "
        direction = None
        if self.__parent:
            direction = self.__parent.get_direction(self)
        if direction:
            return result.__add__(f"{direction}")
        return result

    def __gt__(self, __o: object) -> bool:
        return self.__cost > __o.__cost
