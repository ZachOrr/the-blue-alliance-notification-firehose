from enum import Enum


class Stage3TargetColor2020(str, Enum):
    BLUE = "Blue"
    GREEN = "Green"
    RED = "Red"
    UNKNOWN = "Unknown"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
