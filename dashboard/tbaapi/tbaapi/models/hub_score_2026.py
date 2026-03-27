from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HubScore2026")


@_attrs_define
class HubScore2026:
    """
    Attributes:
        auto_count (int):
        auto_points (int):
        endgame_count (int):
        endgame_points (int):
        shift_1_count (int):
        shift_1_points (int):
        shift_2_count (int):
        shift_2_points (int):
        shift_3_count (int):
        shift_3_points (int):
        shift_4_count (int):
        shift_4_points (int):
        teleop_count (int):
        teleop_points (int):
        total_count (int):
        total_points (int):
        transition_count (int):
        transition_points (int):
    """

    auto_count: int
    auto_points: int
    endgame_count: int
    endgame_points: int
    shift_1_count: int
    shift_1_points: int
    shift_2_count: int
    shift_2_points: int
    shift_3_count: int
    shift_3_points: int
    shift_4_count: int
    shift_4_points: int
    teleop_count: int
    teleop_points: int
    total_count: int
    total_points: int
    transition_count: int
    transition_points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_count = self.auto_count

        auto_points = self.auto_points

        endgame_count = self.endgame_count

        endgame_points = self.endgame_points

        shift_1_count = self.shift_1_count

        shift_1_points = self.shift_1_points

        shift_2_count = self.shift_2_count

        shift_2_points = self.shift_2_points

        shift_3_count = self.shift_3_count

        shift_3_points = self.shift_3_points

        shift_4_count = self.shift_4_count

        shift_4_points = self.shift_4_points

        teleop_count = self.teleop_count

        teleop_points = self.teleop_points

        total_count = self.total_count

        total_points = self.total_points

        transition_count = self.transition_count

        transition_points = self.transition_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoCount": auto_count,
                "autoPoints": auto_points,
                "endgameCount": endgame_count,
                "endgamePoints": endgame_points,
                "shift1Count": shift_1_count,
                "shift1Points": shift_1_points,
                "shift2Count": shift_2_count,
                "shift2Points": shift_2_points,
                "shift3Count": shift_3_count,
                "shift3Points": shift_3_points,
                "shift4Count": shift_4_count,
                "shift4Points": shift_4_points,
                "teleopCount": teleop_count,
                "teleopPoints": teleop_points,
                "totalCount": total_count,
                "totalPoints": total_points,
                "transitionCount": transition_count,
                "transitionPoints": transition_points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_count = d.pop("autoCount")

        auto_points = d.pop("autoPoints")

        endgame_count = d.pop("endgameCount")

        endgame_points = d.pop("endgamePoints")

        shift_1_count = d.pop("shift1Count")

        shift_1_points = d.pop("shift1Points")

        shift_2_count = d.pop("shift2Count")

        shift_2_points = d.pop("shift2Points")

        shift_3_count = d.pop("shift3Count")

        shift_3_points = d.pop("shift3Points")

        shift_4_count = d.pop("shift4Count")

        shift_4_points = d.pop("shift4Points")

        teleop_count = d.pop("teleopCount")

        teleop_points = d.pop("teleopPoints")

        total_count = d.pop("totalCount")

        total_points = d.pop("totalPoints")

        transition_count = d.pop("transitionCount")

        transition_points = d.pop("transitionPoints")

        hub_score_2026 = cls(
            auto_count=auto_count,
            auto_points=auto_points,
            endgame_count=endgame_count,
            endgame_points=endgame_points,
            shift_1_count=shift_1_count,
            shift_1_points=shift_1_points,
            shift_2_count=shift_2_count,
            shift_2_points=shift_2_points,
            shift_3_count=shift_3_count,
            shift_3_points=shift_3_points,
            shift_4_count=shift_4_count,
            shift_4_points=shift_4_points,
            teleop_count=teleop_count,
            teleop_points=teleop_points,
            total_count=total_count,
            total_points=total_points,
            transition_count=transition_count,
            transition_points=transition_points,
        )

        hub_score_2026.additional_properties = d
        return hub_score_2026

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
