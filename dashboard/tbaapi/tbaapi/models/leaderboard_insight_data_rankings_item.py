from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LeaderboardInsightDataRankingsItem")


@_attrs_define
class LeaderboardInsightDataRankingsItem:
    """
    Attributes:
        value (float): Value of the insight that the corresponding team/event/matches have, e.g. number of blue banners,
            or number of matches played.
        keys (list[str]): Team/Event/Match keys that have the corresponding value.
    """

    value: float
    keys: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        keys = self.keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "keys": keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        keys = cast(list[str], d.pop("keys"))

        leaderboard_insight_data_rankings_item = cls(
            value=value,
            keys=keys,
        )

        leaderboard_insight_data_rankings_item.additional_properties = d
        return leaderboard_insight_data_rankings_item

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
