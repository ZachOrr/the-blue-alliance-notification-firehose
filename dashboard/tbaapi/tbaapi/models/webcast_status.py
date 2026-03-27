from enum import Enum


class WebcastStatus(str, Enum):
    OFFLINE = "offline"
    ONLINE = "online"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
