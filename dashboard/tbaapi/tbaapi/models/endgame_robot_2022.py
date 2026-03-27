from enum import Enum


class EndgameRobot2022(str, Enum):
    HIGH = "High"
    LOW = "Low"
    MID = "Mid"
    NONE = "None"
    TRAVERSAL = "Traversal"

    def __str__(self) -> str:
        return str(self.value)
