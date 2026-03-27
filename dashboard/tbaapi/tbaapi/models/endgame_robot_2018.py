from enum import Enum


class EndgameRobot2018(str, Enum):
    CLIMBING = "Climbing"
    LEVITATE = "Levitate"
    NONE = "None"
    PARKING = "Parking"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
