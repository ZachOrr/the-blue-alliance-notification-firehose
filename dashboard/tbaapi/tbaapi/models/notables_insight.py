from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.notables_insight_data import NotablesInsightData


T = TypeVar("T", bound="NotablesInsight")


@_attrs_define
class NotablesInsight:
    """
    Attributes:
        data (NotablesInsightData):
        name (str):
        year (int):
    """

    data: NotablesInsightData
    name: str
    year: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        name = self.name

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "name": name,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notables_insight_data import NotablesInsightData

        d = dict(src_dict)
        data = NotablesInsightData.from_dict(d.pop("data"))

        name = d.pop("name")

        year = d.pop("year")

        notables_insight = cls(
            data=data,
            name=name,
            year=year,
        )

        notables_insight.additional_properties = d
        return notables_insight

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
