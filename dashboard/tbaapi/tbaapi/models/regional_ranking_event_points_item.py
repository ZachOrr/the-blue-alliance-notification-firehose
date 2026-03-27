from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RegionalRankingEventPointsItem")


@_attrs_define
class RegionalRankingEventPointsItem:
    """
    Attributes:
        total (int): Total points awarded at this event.
        alliance_points (int): Points awarded for alliance selection.
        elim_points (int): Points awarded for elimination match performance.
        award_points (int): Points awarded for event awards.
        event_key (str): TBA Event key for this event.
        qual_points (int): Points awarded for qualification match performance.
    """

    total: int
    alliance_points: int
    elim_points: int
    award_points: int
    event_key: str
    qual_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        alliance_points = self.alliance_points

        elim_points = self.elim_points

        award_points = self.award_points

        event_key = self.event_key

        qual_points = self.qual_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "alliance_points": alliance_points,
                "elim_points": elim_points,
                "award_points": award_points,
                "event_key": event_key,
                "qual_points": qual_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        alliance_points = d.pop("alliance_points")

        elim_points = d.pop("elim_points")

        award_points = d.pop("award_points")

        event_key = d.pop("event_key")

        qual_points = d.pop("qual_points")

        regional_ranking_event_points_item = cls(
            total=total,
            alliance_points=alliance_points,
            elim_points=elim_points,
            award_points=award_points,
            event_key=event_key,
            qual_points=qual_points,
        )

        regional_ranking_event_points_item.additional_properties = d
        return regional_ranking_event_points_item

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
