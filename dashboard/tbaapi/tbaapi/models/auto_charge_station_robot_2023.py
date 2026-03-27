from enum import Enum


class AutoChargeStationRobot2023(str, Enum):
    DOCKED = "Docked"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
