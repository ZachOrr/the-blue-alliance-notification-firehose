from enum import Enum


class TowerFace2016(str, Enum):
    BOTH = "Both"
    CHALLENGED = "Challenged"
    NONE = "None"
    SCALED = "Scaled"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
