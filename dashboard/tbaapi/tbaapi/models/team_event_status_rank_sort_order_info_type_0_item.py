from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamEventStatusRankSortOrderInfoType0Item")


@_attrs_define
class TeamEventStatusRankSortOrderInfoType0Item:
    """
    Attributes:
        precision (int | Unset): The number of digits of precision used for this value, eg `2` would correspond to a
            value of `101.11` while `0` would correspond to `101`.
        name (str | Unset): The descriptive name of the value used to sort the ranking.
    """

    precision: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        precision = self.precision

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if precision is not UNSET:
            field_dict["precision"] = precision
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        precision = d.pop("precision", UNSET)

        name = d.pop("name", UNSET)

        team_event_status_rank_sort_order_info_type_0_item = cls(
            precision=precision,
            name=name,
        )

        team_event_status_rank_sort_order_info_type_0_item.additional_properties = d
        return team_event_status_rank_sort_order_info_type_0_item

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
