from enum import Enum


class TowerRobot2026(str, Enum):
    LEVEL1 = "Level1"
    LEVEL2 = "Level2"
    LEVEL3 = "Level3"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
