from Direction import Direction
from TypesNode import TypesNode


class Node:
    def __init__(self, value: str, cost: int) -> None:
        self.__value = value
        self.__cost = cost
        self.__childrens: dict[Direction, Node] = {}
        self.__parent: Node = None
        self.__type_node: TypesNode = TypesNode.LEAF

    def contains(self, node) -> bool:
        return self.__childrens.__contains__(node)

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
            if self.__childrens.__len__() == 2:
                self.__type_node = TypesNode.PARENT_WITH_TWO_CHILDS
            else:
                self.__type_node = TypesNode.PARENT_WITH_ONE_CHILD

        else:
            current_children.add(children)

    def get(self, direction: Direction):
        return self.__childrens.get(direction)

    def __get_last_in(self, direction: Direction):
        if not self.__type_node.is_leaf():
            iterator = self.get(direction)
            while iterator:
                iterator = iterator.get(direction)
            return iterator

        return self

    def delete(self, delete_node) -> None:
        print("eliminar ", delete_node)
        if delete_node.__type_node.is_parent_with_two_childs():
            print(self.__get_last_in(Direction.LEFT))
            # change_node = delete_node.get(Direction.RIGHT).__get_last_in(Direction.LEFT)
            # change_node = delete_node
            # delete_parent_node = delete_node.__parent
            # for direction, node in delete_parent_node.__childrens.items():
            #     if node == delete_node:
            #         delete_parent_node.__childrens[direction] = change_node

        elif delete_node.__type_node.is_parent_with_one_child():
            pass
            # right, left = delete_node.get(Direction.RIGHT), delete_node.get(
            #     Direction.LEFT
            # )
            # if right:
            #     right.changes_position(delete_node)
            # elif left:
            #     left.changes_position(delete_node)
        else:
            pass
            # delete_node.__parent = None

    def changes_position(self, parent) -> None:
        self.__parent = parent.__parent
        parent.__parent = None

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

    def get_childrens(self) -> list:
        return self.__childrens

    def have_parent(self) -> bool:
        return self.__parent

    def get_parent(self):
        return self.__parent

    def get_value(self) -> str:
        return self.__value

    def get_cost(self) -> str:
        return self.__costs

    def set_name(self, name: str) -> None:
        self.__value = name

    def set_cost(self, cost: int) -> None:
        self.__cost = cost

    def __str__(self) -> str:
        return f"{self.__value}: {self.__cost} {self.__type_node}"

    def __gt__(self, __o: object) -> bool:
        return self.__cost > __o.__cost
