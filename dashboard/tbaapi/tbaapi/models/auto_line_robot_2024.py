from enum import Enum


class AutoLineRobot2024(str, Enum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
