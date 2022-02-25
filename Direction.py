from enum import Enum, auto


class Direction(Enum):
    RIGHT = "Derecha"
    LEFT = "Izquierda"

    def __str__(self) -> str:
        return self._value_
