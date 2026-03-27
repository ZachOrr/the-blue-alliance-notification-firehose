from enum import Enum


class RobotAuto2016WithUnknown(str, Enum):
    CROSSED = "Crossed"
    NONE = "None"
    REACHED = "Reached"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
