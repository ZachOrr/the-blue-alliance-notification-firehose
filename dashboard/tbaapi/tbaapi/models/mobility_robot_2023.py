from enum import Enum


class MobilityRobot2023(str, Enum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
