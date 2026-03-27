from enum import Enum


class AutoRobot2018(str, Enum):
    AUTORUN = "AutoRun"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
