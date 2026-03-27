from enum import Enum


class RobotAuto2016WithoutUnknown(str, Enum):
    CROSSED = "Crossed"
    NONE = "None"
    REACHED = "Reached"

    def __str__(self) -> str:
        return str(self.value)
