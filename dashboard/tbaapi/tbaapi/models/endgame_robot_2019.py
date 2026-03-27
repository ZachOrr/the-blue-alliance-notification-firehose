from enum import Enum


class EndgameRobot2019(str, Enum):
    HABLEVEL1 = "HabLevel1"
    HABLEVEL2 = "HabLevel2"
    HABLEVEL3 = "HabLevel3"
    NONE = "None"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
