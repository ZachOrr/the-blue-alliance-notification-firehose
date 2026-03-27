from enum import Enum


class RobotAuto2017(str, Enum):
    MOBILITY = "Mobility"
    NONE = "None"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
