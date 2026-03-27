from enum import Enum


class DoubleElimRound(str, Enum):
    FINALS = "Finals"
    ROUND_1 = "Round 1"
    ROUND_2 = "Round 2"
    ROUND_3 = "Round 3"
    ROUND_4 = "Round 4"
    ROUND_5 = "Round 5"

    def __str__(self) -> str:
        return str(self.value)
