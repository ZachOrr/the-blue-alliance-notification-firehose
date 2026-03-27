from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.leaderboard_insight_data_key_type import LeaderboardInsightDataKeyType

if TYPE_CHECKING:
    from ..models.leaderboard_insight_data_rankings_item import LeaderboardInsightDataRankingsItem


T = TypeVar("T", bound="LeaderboardInsightData")


@_attrs_define
class LeaderboardInsightData:
    """
    Attributes:
        rankings (list[LeaderboardInsightDataRankingsItem]):
        key_type (LeaderboardInsightDataKeyType): What type of key is used in the rankings; either 'team', 'event', or
            'match'.
    """

    rankings: list[LeaderboardInsightDataRankingsItem]
    key_type: LeaderboardInsightDataKeyType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rankings = []
        for rankings_item_data in self.rankings:
            rankings_item = rankings_item_data.to_dict()
            rankings.append(rankings_item)

        key_type = self.key_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rankings": rankings,
                "key_type": key_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_insight_data_rankings_item import LeaderboardInsightDataRankingsItem

        d = dict(src_dict)
        rankings = []
        _rankings = d.pop("rankings")
        for rankings_item_data in _rankings:
            rankings_item = LeaderboardInsightDataRankingsItem.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        key_type = LeaderboardInsightDataKeyType(d.pop("key_type"))

        leaderboard_insight_data = cls(
            rankings=rankings,
            key_type=key_type,
        )

        leaderboard_insight_data.additional_properties = d
        return leaderboard_insight_data

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
