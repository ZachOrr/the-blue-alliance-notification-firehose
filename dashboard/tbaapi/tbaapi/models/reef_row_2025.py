from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReefRow2025")


@_attrs_define
class ReefRow2025:
    """
    Attributes:
        node_a (bool):
        node_b (bool):
        node_c (bool):
        node_d (bool):
        node_e (bool):
        node_f (bool):
        node_g (bool):
        node_h (bool):
        node_i (bool):
        node_j (bool):
        node_k (bool):
        node_l (bool):
    """

    node_a: bool
    node_b: bool
    node_c: bool
    node_d: bool
    node_e: bool
    node_f: bool
    node_g: bool
    node_h: bool
    node_i: bool
    node_j: bool
    node_k: bool
    node_l: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_a = self.node_a

        node_b = self.node_b

        node_c = self.node_c

        node_d = self.node_d

        node_e = self.node_e

        node_f = self.node_f

        node_g = self.node_g

        node_h = self.node_h

        node_i = self.node_i

        node_j = self.node_j

        node_k = self.node_k

        node_l = self.node_l

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodeA": node_a,
                "nodeB": node_b,
                "nodeC": node_c,
                "nodeD": node_d,
                "nodeE": node_e,
                "nodeF": node_f,
                "nodeG": node_g,
                "nodeH": node_h,
                "nodeI": node_i,
                "nodeJ": node_j,
                "nodeK": node_k,
                "nodeL": node_l,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_a = d.pop("nodeA")

        node_b = d.pop("nodeB")

        node_c = d.pop("nodeC")

        node_d = d.pop("nodeD")

        node_e = d.pop("nodeE")

        node_f = d.pop("nodeF")

        node_g = d.pop("nodeG")

        node_h = d.pop("nodeH")

        node_i = d.pop("nodeI")

        node_j = d.pop("nodeJ")

        node_k = d.pop("nodeK")

        node_l = d.pop("nodeL")

        reef_row_2025 = cls(
            node_a=node_a,
            node_b=node_b,
            node_c=node_c,
            node_d=node_d,
            node_e=node_e,
            node_f=node_f,
            node_g=node_g,
            node_h=node_h,
            node_i=node_i,
            node_j=node_j,
            node_k=node_k,
            node_l=node_l,
        )

        reef_row_2025.additional_properties = d
        return reef_row_2025

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
