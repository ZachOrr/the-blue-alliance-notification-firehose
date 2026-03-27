from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_score_breakdown_2015_coopertition import MatchScoreBreakdown2015Coopertition

if TYPE_CHECKING:
    from ..models.match_score_breakdown_2015_alliance import MatchScoreBreakdown2015Alliance


T = TypeVar("T", bound="MatchScoreBreakdown2015")


@_attrs_define
class MatchScoreBreakdown2015:
    """See the 2015 FMS API documentation for a description of each value

    Attributes:
        blue (MatchScoreBreakdown2015Alliance):
        red (MatchScoreBreakdown2015Alliance):
        coopertition (MatchScoreBreakdown2015Coopertition):
        coopertition_points (int):
    """

    blue: MatchScoreBreakdown2015Alliance
    red: MatchScoreBreakdown2015Alliance
    coopertition: MatchScoreBreakdown2015Coopertition
    coopertition_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blue = self.blue.to_dict()

        red = self.red.to_dict()

        coopertition = self.coopertition.value

        coopertition_points = self.coopertition_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blue": blue,
                "red": red,
                "coopertition": coopertition,
                "coopertition_points": coopertition_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_score_breakdown_2015_alliance import MatchScoreBreakdown2015Alliance

        d = dict(src_dict)
        blue = MatchScoreBreakdown2015Alliance.from_dict(d.pop("blue"))

        red = MatchScoreBreakdown2015Alliance.from_dict(d.pop("red"))

        coopertition = MatchScoreBreakdown2015Coopertition(d.pop("coopertition"))

        coopertition_points = d.pop("coopertition_points")

        match_score_breakdown_2015 = cls(
            blue=blue,
            red=red,
            coopertition=coopertition,
            coopertition_points=coopertition_points,
        )

        match_score_breakdown_2015.additional_properties = d
        return match_score_breakdown_2015

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
