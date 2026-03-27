from enum import Enum


class TaxiRobot2022(str, Enum):
    NO = "No"
    YES = "Yes"

    def __str__(self) -> str:
        return str(self.value)
