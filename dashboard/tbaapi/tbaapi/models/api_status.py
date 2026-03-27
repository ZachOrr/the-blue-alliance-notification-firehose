from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_status_app_version import APIStatusAppVersion


T = TypeVar("T", bound="APIStatus")


@_attrs_define
class APIStatus:
    """
    Attributes:
        current_season (int): Year of the current FRC season.
        max_season (int): Maximum FRC season year for valid queries.
        is_datafeed_down (bool): True if the entire FMS API provided by FIRST is down.
        down_events (list[str]): An array of strings containing event keys of any active events that are no longer
            updating.
        ios (APIStatusAppVersion):
        android (APIStatusAppVersion):
        max_team_page (int): Maximum team page number for valid queries.
    """

    current_season: int
    max_season: int
    is_datafeed_down: bool
    down_events: list[str]
    ios: APIStatusAppVersion
    android: APIStatusAppVersion
    max_team_page: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_season = self.current_season

        max_season = self.max_season

        is_datafeed_down = self.is_datafeed_down

        down_events = self.down_events

        ios = self.ios.to_dict()

        android = self.android.to_dict()

        max_team_page = self.max_team_page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_season": current_season,
                "max_season": max_season,
                "is_datafeed_down": is_datafeed_down,
                "down_events": down_events,
                "ios": ios,
                "android": android,
                "max_team_page": max_team_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_status_app_version import APIStatusAppVersion

        d = dict(src_dict)
        current_season = d.pop("current_season")

        max_season = d.pop("max_season")

        is_datafeed_down = d.pop("is_datafeed_down")

        down_events = cast(list[str], d.pop("down_events"))

        ios = APIStatusAppVersion.from_dict(d.pop("ios"))

        android = APIStatusAppVersion.from_dict(d.pop("android"))

        max_team_page = d.pop("max_team_page")

        api_status = cls(
            current_season=current_season,
            max_season=max_season,
            is_datafeed_down=is_datafeed_down,
            down_events=down_events,
            ios=ios,
            android=android,
            max_team_page=max_team_page,
        )

        api_status.additional_properties = d
        return api_status

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
