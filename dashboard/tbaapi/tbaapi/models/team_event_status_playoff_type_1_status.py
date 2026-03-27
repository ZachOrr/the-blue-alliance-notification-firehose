from enum import Enum


class TeamEventStatusPlayoffType1Status(str, Enum):
    ELIMINATED = "eliminated"
    PLAYING = "playing"
    WON = "won"

    def __str__(self) -> str:
        return str(self.value)
