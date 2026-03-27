from enum import Enum


class Bay2019(str, Enum):
    NONE = "None"
    PANEL = "Panel"
    PANELANDCARGO = "PanelAndCargo"

    def __str__(self) -> str:
        return str(self.value)
