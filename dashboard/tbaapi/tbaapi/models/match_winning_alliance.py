from enum import Enum


class MatchWinningAlliance(str, Enum):
    BLUE = "blue"
    RED = "red"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
