from enum import Enum


class MatchScoreBreakdown2023AllianceLinksType0ItemRow(str, Enum):
    BOTTOM = "Bottom"
    MID = "Mid"
    TOP = "Top"

    def __str__(self) -> str:
        return str(self.value)
