from enum import Enum


class MatchSimpleWinningAlliance(str, Enum):
    BLUE = "blue"
    RED = "red"
    VALUE_2 = ""

    def __str__(self) -> str:
        return str(self.value)
