from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DistrictOfficialAdvancementCounts")


@_attrs_define
class DistrictOfficialAdvancementCounts:
    """The number of teams advancing to DCMP and CMP from this district, as specified in the FIRST manual.

    Attributes:
        dcmp (int): Number of teams advancing to the District Championship.
        cmp (int): Number of teams advancing to the Championship.
    """

    dcmp: int
    cmp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dcmp = self.dcmp

        cmp = self.cmp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dcmp": dcmp,
                "cmp": cmp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dcmp = d.pop("dcmp")

        cmp = d.pop("cmp")

        district_official_advancement_counts = cls(
            dcmp=dcmp,
            cmp=cmp,
        )

        district_official_advancement_counts.additional_properties = d
        return district_official_advancement_counts

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
