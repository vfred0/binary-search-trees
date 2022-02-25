from enum import Enum, auto


class TypesNode(Enum):
    LEAF = "Hoja"
    PARENT_WITH_ONE_CHILD = "Padre con un hijo"
    PARENT_WITH_TWO_CHILDS = "Padre con dos hijos"

    def is_leaf(self):
        return self == TypesNode.LEAF

    def is_parent_with_one_child(self):
        return self == TypesNode.PARENT_WITH_ONE_CHILD

    def is_parent_with_two_childs(self):
        return self == TypesNode.PARENT_WITH_TWO_CHILDS

    def __str__(self) -> str:
        return self._value_
