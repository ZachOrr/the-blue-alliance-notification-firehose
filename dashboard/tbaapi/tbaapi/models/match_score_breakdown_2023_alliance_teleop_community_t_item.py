from enum import Enum


class MatchScoreBreakdown2023AllianceTeleopCommunityTItem(str, Enum):
    CONE = "Cone"
    CUBE = "Cube"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
