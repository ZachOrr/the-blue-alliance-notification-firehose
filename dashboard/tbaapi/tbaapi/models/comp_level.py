from enum import Enum


class CompLevel(str, Enum):
    EF = "ef"
    F = "f"
    QF = "qf"
    QM = "qm"
    SF = "sf"

    def __str__(self) -> str:
        return str(self.value)
