from enum import Enum


class EndgameRobot2020(str, Enum):
    HANG = "Hang"
    NONE = "None"
    PARK = "Park"

    def __str__(self) -> str:
        return str(self.value)
