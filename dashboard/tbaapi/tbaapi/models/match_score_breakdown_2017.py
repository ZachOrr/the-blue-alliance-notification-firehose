from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.match_score_breakdown_2017_alliance import MatchScoreBreakdown2017Alliance


T = TypeVar("T", bound="MatchScoreBreakdown2017")


@_attrs_define
class MatchScoreBreakdown2017:
    """See the 2017 FMS API documentation for a description of each value.

    Attributes:
        blue (MatchScoreBreakdown2017Alliance):
        red (MatchScoreBreakdown2017Alliance):
    """

    blue: MatchScoreBreakdown2017Alliance
    red: MatchScoreBreakdown2017Alliance
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blue = self.blue.to_dict()

        red = self.red.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blue": blue,
                "red": red,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_score_breakdown_2017_alliance import MatchScoreBreakdown2017Alliance

        d = dict(src_dict)
        blue = MatchScoreBreakdown2017Alliance.from_dict(d.pop("blue"))

        red = MatchScoreBreakdown2017Alliance.from_dict(d.pop("red"))

        match_score_breakdown_2017 = cls(
            blue=blue,
            red=red,
        )

        match_score_breakdown_2017.additional_properties = d
        return match_score_breakdown_2017

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
