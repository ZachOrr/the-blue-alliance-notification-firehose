from enum import Enum


class MatchScoreBreakdown2018AllianceTbaGameData(str, Enum):
    LLL = "LLL"
    LRL = "LRL"
    RLR = "RLR"
    RRR = "RRR"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
