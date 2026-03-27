from enum import Enum


class WebcastType(str, Enum):
    DACAST = "dacast"
    DIRECT_LINK = "direct_link"
    HTML5 = "html5"
    IFRAME = "iframe"
    JUSTIN = "justin"
    LIVESTREAM = "livestream"
    MMS = "mms"
    RTMP = "rtmp"
    STEMTV = "stemtv"
    TWITCH = "twitch"
    USTREAM = "ustream"
    YOUTUBE = "youtube"

    def __str__(self) -> str:
        return str(self.value)
