from enum import Enum


class PreMatchBay2019(str, Enum):
    CARGO = "Cargo"
    PANEL = "Panel"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
