from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.match_alliance import MatchAlliance


T = TypeVar("T", bound="MatchAlliances")


@_attrs_define
class MatchAlliances:
    """A list of alliances, the teams on the alliances, and their score.

    Attributes:
        red (MatchAlliance):
        blue (MatchAlliance):
    """

    red: MatchAlliance
    blue: MatchAlliance
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        red = self.red.to_dict()

        blue = self.blue.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "red": red,
                "blue": blue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_alliance import MatchAlliance

        d = dict(src_dict)
        red = MatchAlliance.from_dict(d.pop("red"))

        blue = MatchAlliance.from_dict(d.pop("blue"))

        match_alliances = cls(
            red=red,
            blue=blue,
        )

        match_alliances.additional_properties = d
        return match_alliances

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
