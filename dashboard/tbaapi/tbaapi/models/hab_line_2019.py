from enum import Enum


class HabLine2019(str, Enum):
    CROSSEDHABLINEINSANDSTORM = "CrossedHabLineInSandstorm"
    CROSSEDHABLINEINTELEOP = "CrossedHabLineInTeleop"
    NONE = "None"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
