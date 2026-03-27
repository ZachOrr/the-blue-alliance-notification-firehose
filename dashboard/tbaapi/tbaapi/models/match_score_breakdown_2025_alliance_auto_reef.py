from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reef_row_2025 import ReefRow2025


T = TypeVar("T", bound="MatchScoreBreakdown2025AllianceAutoReef")


@_attrs_define
class MatchScoreBreakdown2025AllianceAutoReef:
    """
    Attributes:
        top_row (ReefRow2025):
        mid_row (ReefRow2025):
        bot_row (ReefRow2025):
        trough (int):
        tba_bot_row_count (int | Unset): Unofficial TBA-computed value that sums the total number of game pieces scored
            in the botRow object.
        tba_mid_row_count (int | Unset): Unofficial TBA-computed value that sums the total number of game pieces scored
            in the midRow object.
        tba_top_row_count (int | Unset): Unofficial TBA-computed value that sums the total number of game pieces scored
            in the topRow object.
    """

    top_row: ReefRow2025
    mid_row: ReefRow2025
    bot_row: ReefRow2025
    trough: int
    tba_bot_row_count: int | Unset = UNSET
    tba_mid_row_count: int | Unset = UNSET
    tba_top_row_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_row = self.top_row.to_dict()

        mid_row = self.mid_row.to_dict()

        bot_row = self.bot_row.to_dict()

        trough = self.trough

        tba_bot_row_count = self.tba_bot_row_count

        tba_mid_row_count = self.tba_mid_row_count

        tba_top_row_count = self.tba_top_row_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topRow": top_row,
                "midRow": mid_row,
                "botRow": bot_row,
                "trough": trough,
            }
        )
        if tba_bot_row_count is not UNSET:
            field_dict["tba_botRowCount"] = tba_bot_row_count
        if tba_mid_row_count is not UNSET:
            field_dict["tba_midRowCount"] = tba_mid_row_count
        if tba_top_row_count is not UNSET:
            field_dict["tba_topRowCount"] = tba_top_row_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reef_row_2025 import ReefRow2025

        d = dict(src_dict)
        top_row = ReefRow2025.from_dict(d.pop("topRow"))

        mid_row = ReefRow2025.from_dict(d.pop("midRow"))

        bot_row = ReefRow2025.from_dict(d.pop("botRow"))

        trough = d.pop("trough")

        tba_bot_row_count = d.pop("tba_botRowCount", UNSET)

        tba_mid_row_count = d.pop("tba_midRowCount", UNSET)

        tba_top_row_count = d.pop("tba_topRowCount", UNSET)

        match_score_breakdown_2025_alliance_auto_reef = cls(
            top_row=top_row,
            mid_row=mid_row,
            bot_row=bot_row,
            trough=trough,
            tba_bot_row_count=tba_bot_row_count,
            tba_mid_row_count=tba_mid_row_count,
            tba_top_row_count=tba_top_row_count,
        )

        match_score_breakdown_2025_alliance_auto_reef.additional_properties = d
        return match_score_breakdown_2025_alliance_auto_reef

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
