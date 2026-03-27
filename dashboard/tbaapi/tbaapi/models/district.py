from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.district_official_advancement_counts import DistrictOfficialAdvancementCounts


T = TypeVar("T", bound="District")


@_attrs_define
class District:
    """
    Attributes:
        abbreviation (str): The short identifier for the district.
        display_name (str): The long name for the district.
        key (str): Key for this district, e.g. `2016ne`.
        year (int): Year this district participated.
        official_advancement_counts (DistrictOfficialAdvancementCounts): The number of teams advancing to DCMP and CMP
            from this district, as specified in the FIRST manual.
    """

    abbreviation: str
    display_name: str
    key: str
    year: int
    official_advancement_counts: DistrictOfficialAdvancementCounts
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        abbreviation = self.abbreviation

        display_name = self.display_name

        key = self.key

        year = self.year

        official_advancement_counts = self.official_advancement_counts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "abbreviation": abbreviation,
                "display_name": display_name,
                "key": key,
                "year": year,
                "official_advancement_counts": official_advancement_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_official_advancement_counts import DistrictOfficialAdvancementCounts

        d = dict(src_dict)
        abbreviation = d.pop("abbreviation")

        display_name = d.pop("display_name")

        key = d.pop("key")

        year = d.pop("year")

        official_advancement_counts = DistrictOfficialAdvancementCounts.from_dict(d.pop("official_advancement_counts"))

        district = cls(
            abbreviation=abbreviation,
            display_name=display_name,
            key=key,
            year=year,
            official_advancement_counts=official_advancement_counts,
        )

        district.additional_properties = d
        return district

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
