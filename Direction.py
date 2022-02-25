from enum import Enum, auto


class Direction(Enum):
    RIGHT = "Derecho"
    LEFT = "Izquierdo"

    def __str__(self) -> str:
        return self._value_
