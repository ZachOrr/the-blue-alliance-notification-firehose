from enum import Enum


class EndGameRobot2024(str, Enum):
    CENTERSTAGE = "CenterStage"
    NONE = "None"
    PARKED = "Parked"
    STAGELEFT = "StageLeft"
    STAGERIGHT = "StageRight"

    def __str__(self) -> str:
        return str(self.value)
