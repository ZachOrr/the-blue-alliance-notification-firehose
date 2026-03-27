from enum import Enum


class Touchpad2017(str, Enum):
    NONE = "None"
    READYFORTAKEOFF = "ReadyForTakeoff"

    def __str__(self) -> str:
        return str(self.value)
