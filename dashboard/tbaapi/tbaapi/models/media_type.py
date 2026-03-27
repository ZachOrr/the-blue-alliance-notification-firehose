from enum import Enum


class MediaType(str, Enum):
    AVATAR = "avatar"
    CDPHOTOTHREAD = "cdphotothread"
    CD_THREAD = "cd-thread"
    EXTERNAL_LINK = "external-link"
    FACEBOOK_PROFILE = "facebook-profile"
    GITHUB_PROFILE = "github-profile"
    GITLAB_PROFILE = "gitlab-profile"
    GRABCAD = "grabcad"
    IMGUR = "imgur"
    INSTAGRAM_IMAGE = "instagram-image"
    INSTAGRAM_PROFILE = "instagram-profile"
    ONSHAPE = "onshape"
    PERISCOPE_PROFILE = "periscope-profile"
    TWITTER_PROFILE = "twitter-profile"
    YOUTUBE = "youtube"
    YOUTUBE_CHANNEL = "youtube-channel"

    def __str__(self) -> str:
        return str(self.value)
