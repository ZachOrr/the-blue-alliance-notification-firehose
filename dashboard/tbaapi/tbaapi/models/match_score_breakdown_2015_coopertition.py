from enum import Enum


class MatchScoreBreakdown2015Coopertition(str, Enum):
    NONE = "None"
    STACK = "Stack"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
