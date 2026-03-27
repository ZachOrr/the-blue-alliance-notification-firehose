from enum import Enum


class LeaderboardInsightDataKeyType(str, Enum):
    EVENT = "event"
    MATCH = "match"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
