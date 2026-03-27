from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_score_breakdown_2023_alliance_links_type_0_item_nodes_item import (
    MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem,
)
from ..models.match_score_breakdown_2023_alliance_links_type_0_item_row import (
    MatchScoreBreakdown2023AllianceLinksType0ItemRow,
)

T = TypeVar("T", bound="MatchScoreBreakdown2023AllianceLinksType0Item")


@_attrs_define
class MatchScoreBreakdown2023AllianceLinksType0Item:
    """
    Attributes:
        nodes (list[MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem]):
        row (MatchScoreBreakdown2023AllianceLinksType0ItemRow):
    """

    nodes: list[MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem]
    row: MatchScoreBreakdown2023AllianceLinksType0ItemRow
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.value
            nodes.append(nodes_item)

        row = self.row.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
                "row": row,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem(nodes_item_data)

            nodes.append(nodes_item)

        row = MatchScoreBreakdown2023AllianceLinksType0ItemRow(d.pop("row"))

        match_score_breakdown_2023_alliance_links_type_0_item = cls(
            nodes=nodes,
            row=row,
        )

        match_score_breakdown_2023_alliance_links_type_0_item.additional_properties = d
        return match_score_breakdown_2023_alliance_links_type_0_item

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
