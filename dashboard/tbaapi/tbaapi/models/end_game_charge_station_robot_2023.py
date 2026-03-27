from enum import Enum


class EndGameChargeStationRobot2023(str, Enum):
    DOCKED = "Docked"
    NONE = "None"
    PARK = "Park"
    PARKED = "Parked"

    def __str__(self) -> str:
        return str(self.value)
