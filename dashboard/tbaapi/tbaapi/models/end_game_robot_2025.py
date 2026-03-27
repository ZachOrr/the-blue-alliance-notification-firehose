from enum import Enum


class EndGameRobot2025(str, Enum):
    DEEPCAGE = "DeepCage"
    NONE = "None"
    PARKED = "Parked"
    SHALLOWCAGE = "ShallowCage"

    def __str__(self) -> str:
        return str(self.value)
