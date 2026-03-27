from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.regional_advancement import RegionalAdvancement


T = TypeVar("T", bound="GetRegionalAdvancementResponse200Type1")


@_attrs_define
class GetRegionalAdvancementResponse200Type1:
    """ """

    additional_properties: dict[str, RegionalAdvancement] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regional_advancement import RegionalAdvancement

        d = dict(src_dict)
        get_regional_advancement_response_200_type_1 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = RegionalAdvancement.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_regional_advancement_response_200_type_1.additional_properties = additional_properties
        return get_regional_advancement_response_200_type_1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> RegionalAdvancement:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: RegionalAdvancement) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
