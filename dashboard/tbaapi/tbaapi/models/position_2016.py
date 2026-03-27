from enum import Enum


class Position2016(str, Enum):
    A_CHEVALDEFRISE = "A_ChevalDeFrise"
    A_PORTCULLIS = "A_Portcullis"
    B_MOAT = "B_Moat"
    B_RAMPARTS = "B_Ramparts"
    C_DRAWBRIDGE = "C_Drawbridge"
    C_SALLYPORT = "C_SallyPort"
    D_ROCKWALL = "D_RockWall"
    D_ROUGHTERRAIN = "D_RoughTerrain"
    NOTSPECIFIED = "NotSpecified"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
