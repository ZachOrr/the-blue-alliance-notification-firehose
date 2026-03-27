from enum import Enum


class BridgeState2023(str, Enum):
    LEVEL = "Level"
    NOTLEVEL = "NotLevel"

    def __str__(self) -> str:
        return str(self.value)
