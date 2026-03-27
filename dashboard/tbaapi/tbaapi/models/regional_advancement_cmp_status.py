from enum import Enum


class RegionalAdvancementCmpStatus(str, Enum):
    DECLINED = "Declined"
    EVENTQUALIFIED = "EventQualified"
    NOTINVITED = "NotInvited"
    POOLQUALIFIED = "PoolQualified"
    PREQUALIFIED = "PreQualified"

    def __str__(self) -> str:
        return str(self.value)
