from enum import Enum


class EndgameRungIsLevel2020(str, Enum):
    ISLEVEL = "IsLevel"
    NOTLEVEL = "NotLevel"

    def __str__(self) -> str:
        return str(self.value)
