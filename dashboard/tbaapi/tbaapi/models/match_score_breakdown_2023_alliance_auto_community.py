from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.match_score_breakdown_2023_alliance_auto_community_b_item import (
    MatchScoreBreakdown2023AllianceAutoCommunityBItem,
)
from ..models.match_score_breakdown_2023_alliance_auto_community_m_item import (
    MatchScoreBreakdown2023AllianceAutoCommunityMItem,
)
from ..models.match_score_breakdown_2023_alliance_auto_community_t_item import (
    MatchScoreBreakdown2023AllianceAutoCommunityTItem,
)

T = TypeVar("T", bound="MatchScoreBreakdown2023AllianceAutoCommunity")


@_attrs_define
class MatchScoreBreakdown2023AllianceAutoCommunity:
    """
    Attributes:
        b (list[MatchScoreBreakdown2023AllianceAutoCommunityBItem]):
        m (list[MatchScoreBreakdown2023AllianceAutoCommunityMItem]):
        t (list[MatchScoreBreakdown2023AllianceAutoCommunityTItem]):
    """

    b: list[MatchScoreBreakdown2023AllianceAutoCommunityBItem]
    m: list[MatchScoreBreakdown2023AllianceAutoCommunityMItem]
    t: list[MatchScoreBreakdown2023AllianceAutoCommunityTItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        b = []
        for b_item_data in self.b:
            b_item = b_item_data.value
            b.append(b_item)

        m = []
        for m_item_data in self.m:
            m_item = m_item_data.value
            m.append(m_item)

        t = []
        for t_item_data in self.t:
            t_item = t_item_data.value
            t.append(t_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "B": b,
                "M": m,
                "T": t,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        b = []
        _b = d.pop("B")
        for b_item_data in _b:
            b_item = MatchScoreBreakdown2023AllianceAutoCommunityBItem(b_item_data)

            b.append(b_item)

        m = []
        _m = d.pop("M")
        for m_item_data in _m:
            m_item = MatchScoreBreakdown2023AllianceAutoCommunityMItem(m_item_data)

            m.append(m_item)

        t = []
        _t = d.pop("T")
        for t_item_data in _t:
            t_item = MatchScoreBreakdown2023AllianceAutoCommunityTItem(t_item_data)

            t.append(t_item)

        match_score_breakdown_2023_alliance_auto_community = cls(
            b=b,
            m=m,
            t=t,
        )

        match_score_breakdown_2023_alliance_auto_community.additional_properties = d
        return match_score_breakdown_2023_alliance_auto_community

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
