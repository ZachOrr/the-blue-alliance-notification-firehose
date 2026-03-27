from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDistrictPointsTiebreakersAdditionalProperty")


@_attrs_define
class EventDistrictPointsTiebreakersAdditionalProperty:
    """
    Attributes:
        highest_qual_scores (list[int] | Unset):
        qual_wins (int | Unset):
    """

    highest_qual_scores: list[int] | Unset = UNSET
    qual_wins: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        highest_qual_scores: list[int] | Unset = UNSET
        if not isinstance(self.highest_qual_scores, Unset):
            highest_qual_scores = self.highest_qual_scores

        qual_wins = self.qual_wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if highest_qual_scores is not UNSET:
            field_dict["highest_qual_scores"] = highest_qual_scores
        if qual_wins is not UNSET:
            field_dict["qual_wins"] = qual_wins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        highest_qual_scores = cast(list[int], d.pop("highest_qual_scores", UNSET))

        qual_wins = d.pop("qual_wins", UNSET)

        event_district_points_tiebreakers_additional_property = cls(
            highest_qual_scores=highest_qual_scores,
            qual_wins=qual_wins,
        )

        event_district_points_tiebreakers_additional_property.additional_properties = d
        return event_district_points_tiebreakers_additional_property

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
