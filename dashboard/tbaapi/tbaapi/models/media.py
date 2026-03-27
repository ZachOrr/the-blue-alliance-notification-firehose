from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.media_type import MediaType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_details_type_0 import MediaDetailsType0
    from ..models.media_details_type_1 import MediaDetailsType1
    from ..models.media_details_type_2 import MediaDetailsType2
    from ..models.media_details_type_3 import MediaDetailsType3
    from ..models.media_details_type_4 import MediaDetailsType4
    from ..models.media_details_type_5 import MediaDetailsType5


T = TypeVar("T", bound="Media")


@_attrs_define
class Media:
    """The `Media` object contains a reference for most any media associated with a team or event on TBA.

    Attributes:
        type_ (MediaType): String type of the media element.
        foreign_key (str): The key used to identify this media on the media site.
        team_keys (list[str]): List of teams that this media belongs to. Most likely length 1.
        details (MediaDetailsType0 | MediaDetailsType1 | MediaDetailsType2 | MediaDetailsType3 | MediaDetailsType4 |
            MediaDetailsType5 | Unset): If required, a JSON dict of additional media information.
        preferred (bool | Unset): True if the media is of high quality.
        direct_url (str | Unset): Direct URL to the media.
        view_url (str | Unset): The URL that leads to the full web page for the media, if one exists.
    """

    type_: MediaType
    foreign_key: str
    team_keys: list[str]
    details: (
        MediaDetailsType0
        | MediaDetailsType1
        | MediaDetailsType2
        | MediaDetailsType3
        | MediaDetailsType4
        | MediaDetailsType5
        | Unset
    ) = UNSET
    preferred: bool | Unset = UNSET
    direct_url: str | Unset = UNSET
    view_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.media_details_type_0 import MediaDetailsType0
        from ..models.media_details_type_1 import MediaDetailsType1
        from ..models.media_details_type_2 import MediaDetailsType2
        from ..models.media_details_type_3 import MediaDetailsType3
        from ..models.media_details_type_4 import MediaDetailsType4

        type_ = self.type_.value

        foreign_key = self.foreign_key

        team_keys = self.team_keys

        details: dict[str, Any] | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, MediaDetailsType0):
            details = self.details.to_dict()
        elif isinstance(self.details, MediaDetailsType1):
            details = self.details.to_dict()
        elif isinstance(self.details, MediaDetailsType2):
            details = self.details.to_dict()
        elif isinstance(self.details, MediaDetailsType3):
            details = self.details.to_dict()
        elif isinstance(self.details, MediaDetailsType4):
            details = self.details.to_dict()
        else:
            details = self.details.to_dict()

        preferred = self.preferred

        direct_url = self.direct_url

        view_url = self.view_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "foreign_key": foreign_key,
                "team_keys": team_keys,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details
        if preferred is not UNSET:
            field_dict["preferred"] = preferred
        if direct_url is not UNSET:
            field_dict["direct_url"] = direct_url
        if view_url is not UNSET:
            field_dict["view_url"] = view_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_details_type_0 import MediaDetailsType0
        from ..models.media_details_type_1 import MediaDetailsType1
        from ..models.media_details_type_2 import MediaDetailsType2
        from ..models.media_details_type_3 import MediaDetailsType3
        from ..models.media_details_type_4 import MediaDetailsType4
        from ..models.media_details_type_5 import MediaDetailsType5

        d = dict(src_dict)
        type_ = MediaType(d.pop("type"))

        foreign_key = d.pop("foreign_key")

        team_keys = cast(list[str], d.pop("team_keys"))

        def _parse_details(
            data: object,
        ) -> (
            MediaDetailsType0
            | MediaDetailsType1
            | MediaDetailsType2
            | MediaDetailsType3
            | MediaDetailsType4
            | MediaDetailsType5
            | Unset
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = MediaDetailsType0.from_dict(data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = MediaDetailsType1.from_dict(data)

                return details_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_2 = MediaDetailsType2.from_dict(data)

                return details_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_3 = MediaDetailsType3.from_dict(data)

                return details_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_4 = MediaDetailsType4.from_dict(data)

                return details_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            details_type_5 = MediaDetailsType5.from_dict(data)

            return details_type_5

        details = _parse_details(d.pop("details", UNSET))

        preferred = d.pop("preferred", UNSET)

        direct_url = d.pop("direct_url", UNSET)

        view_url = d.pop("view_url", UNSET)

        media = cls(
            type_=type_,
            foreign_key=foreign_key,
            team_keys=team_keys,
            details=details,
            preferred=preferred,
            direct_url=direct_url,
            view_url=view_url,
        )

        media.additional_properties = d
        return media

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
