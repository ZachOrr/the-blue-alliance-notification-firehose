from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.zebra_team import ZebraTeam


T = TypeVar("T", bound="ZebraAlliances")


@_attrs_define
class ZebraAlliances:
    """
    Attributes:
        red (list[ZebraTeam] | Unset): Zebra MotionWorks data for teams on the red alliance
        blue (list[ZebraTeam] | Unset): Zebra data for teams on the blue alliance
    """

    red: list[ZebraTeam] | Unset = UNSET
    blue: list[ZebraTeam] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        red: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.red, Unset):
            red = []
            for red_item_data in self.red:
                red_item = red_item_data.to_dict()
                red.append(red_item)

        blue: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blue, Unset):
            blue = []
            for blue_item_data in self.blue:
                blue_item = blue_item_data.to_dict()
                blue.append(blue_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if red is not UNSET:
            field_dict["red"] = red
        if blue is not UNSET:
            field_dict["blue"] = blue

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zebra_team import ZebraTeam

        d = dict(src_dict)
        _red = d.pop("red", UNSET)
        red: list[ZebraTeam] | Unset = UNSET
        if _red is not UNSET:
            red = []
            for red_item_data in _red:
                red_item = ZebraTeam.from_dict(red_item_data)

                red.append(red_item)

        _blue = d.pop("blue", UNSET)
        blue: list[ZebraTeam] | Unset = UNSET
        if _blue is not UNSET:
            blue = []
            for blue_item_data in _blue:
                blue_item = ZebraTeam.from_dict(blue_item_data)

                blue.append(blue_item)

        zebra_alliances = cls(
            red=red,
            blue=blue,
        )

        zebra_alliances.additional_properties = d
        return zebra_alliances

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
