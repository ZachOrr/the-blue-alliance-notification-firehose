from enum import Enum


class InitLineRobot2020(str, Enum):
    EXITED = "Exited"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
