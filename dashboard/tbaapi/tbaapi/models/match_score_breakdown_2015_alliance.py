from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2015Alliance")


@_attrs_define
class MatchScoreBreakdown2015Alliance:
    """
    Attributes:
        auto (None | str | Unset):
        auto_points (int | None | Unset):
        teleop_points (int | Unset):
        container_points (int | Unset):
        tote_points (int | Unset):
        litter_points (int | Unset):
        foul (None | str | Unset):
        foul_points (int | None | Unset):
        adjust_points (int | Unset):
        total_points (int | Unset):
        foul_count (int | Unset):
        tote_count_far (int | Unset):
        tote_count_near (int | Unset):
        tote_set (bool | Unset):
        tote_stack (bool | Unset):
        container_count_level1 (int | Unset):
        container_count_level2 (int | Unset):
        container_count_level3 (int | Unset):
        container_count_level4 (int | Unset):
        container_count_level5 (int | Unset):
        container_count_level6 (int | Unset):
        container_set (bool | Unset):
        litter_count_container (int | Unset):
        litter_count_landfill (int | Unset):
        litter_count_unprocessed (int | Unset):
        robot_set (bool | Unset):
    """

    auto: None | str | Unset = UNSET
    auto_points: int | None | Unset = UNSET
    teleop_points: int | Unset = UNSET
    container_points: int | Unset = UNSET
    tote_points: int | Unset = UNSET
    litter_points: int | Unset = UNSET
    foul: None | str | Unset = UNSET
    foul_points: int | None | Unset = UNSET
    adjust_points: int | Unset = UNSET
    total_points: int | Unset = UNSET
    foul_count: int | Unset = UNSET
    tote_count_far: int | Unset = UNSET
    tote_count_near: int | Unset = UNSET
    tote_set: bool | Unset = UNSET
    tote_stack: bool | Unset = UNSET
    container_count_level1: int | Unset = UNSET
    container_count_level2: int | Unset = UNSET
    container_count_level3: int | Unset = UNSET
    container_count_level4: int | Unset = UNSET
    container_count_level5: int | Unset = UNSET
    container_count_level6: int | Unset = UNSET
    container_set: bool | Unset = UNSET
    litter_count_container: int | Unset = UNSET
    litter_count_landfill: int | Unset = UNSET
    litter_count_unprocessed: int | Unset = UNSET
    robot_set: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto: None | str | Unset
        if isinstance(self.auto, Unset):
            auto = UNSET
        else:
            auto = self.auto

        auto_points: int | None | Unset
        if isinstance(self.auto_points, Unset):
            auto_points = UNSET
        else:
            auto_points = self.auto_points

        teleop_points = self.teleop_points

        container_points = self.container_points

        tote_points = self.tote_points

        litter_points = self.litter_points

        foul: None | str | Unset
        if isinstance(self.foul, Unset):
            foul = UNSET
        else:
            foul = self.foul

        foul_points: int | None | Unset
        if isinstance(self.foul_points, Unset):
            foul_points = UNSET
        else:
            foul_points = self.foul_points

        adjust_points = self.adjust_points

        total_points = self.total_points

        foul_count = self.foul_count

        tote_count_far = self.tote_count_far

        tote_count_near = self.tote_count_near

        tote_set = self.tote_set

        tote_stack = self.tote_stack

        container_count_level1 = self.container_count_level1

        container_count_level2 = self.container_count_level2

        container_count_level3 = self.container_count_level3

        container_count_level4 = self.container_count_level4

        container_count_level5 = self.container_count_level5

        container_count_level6 = self.container_count_level6

        container_set = self.container_set

        litter_count_container = self.litter_count_container

        litter_count_landfill = self.litter_count_landfill

        litter_count_unprocessed = self.litter_count_unprocessed

        robot_set = self.robot_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto is not UNSET:
            field_dict["auto"] = auto
        if auto_points is not UNSET:
            field_dict["auto_points"] = auto_points
        if teleop_points is not UNSET:
            field_dict["teleop_points"] = teleop_points
        if container_points is not UNSET:
            field_dict["container_points"] = container_points
        if tote_points is not UNSET:
            field_dict["tote_points"] = tote_points
        if litter_points is not UNSET:
            field_dict["litter_points"] = litter_points
        if foul is not UNSET:
            field_dict["foul"] = foul
        if foul_points is not UNSET:
            field_dict["foul_points"] = foul_points
        if adjust_points is not UNSET:
            field_dict["adjust_points"] = adjust_points
        if total_points is not UNSET:
            field_dict["total_points"] = total_points
        if foul_count is not UNSET:
            field_dict["foul_count"] = foul_count
        if tote_count_far is not UNSET:
            field_dict["tote_count_far"] = tote_count_far
        if tote_count_near is not UNSET:
            field_dict["tote_count_near"] = tote_count_near
        if tote_set is not UNSET:
            field_dict["tote_set"] = tote_set
        if tote_stack is not UNSET:
            field_dict["tote_stack"] = tote_stack
        if container_count_level1 is not UNSET:
            field_dict["container_count_level1"] = container_count_level1
        if container_count_level2 is not UNSET:
            field_dict["container_count_level2"] = container_count_level2
        if container_count_level3 is not UNSET:
            field_dict["container_count_level3"] = container_count_level3
        if container_count_level4 is not UNSET:
            field_dict["container_count_level4"] = container_count_level4
        if container_count_level5 is not UNSET:
            field_dict["container_count_level5"] = container_count_level5
        if container_count_level6 is not UNSET:
            field_dict["container_count_level6"] = container_count_level6
        if container_set is not UNSET:
            field_dict["container_set"] = container_set
        if litter_count_container is not UNSET:
            field_dict["litter_count_container"] = litter_count_container
        if litter_count_landfill is not UNSET:
            field_dict["litter_count_landfill"] = litter_count_landfill
        if litter_count_unprocessed is not UNSET:
            field_dict["litter_count_unprocessed"] = litter_count_unprocessed
        if robot_set is not UNSET:
            field_dict["robot_set"] = robot_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_auto(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto = _parse_auto(d.pop("auto", UNSET))

        def _parse_auto_points(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        auto_points = _parse_auto_points(d.pop("auto_points", UNSET))

        teleop_points = d.pop("teleop_points", UNSET)

        container_points = d.pop("container_points", UNSET)

        tote_points = d.pop("tote_points", UNSET)

        litter_points = d.pop("litter_points", UNSET)

        def _parse_foul(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        foul = _parse_foul(d.pop("foul", UNSET))

        def _parse_foul_points(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        foul_points = _parse_foul_points(d.pop("foul_points", UNSET))

        adjust_points = d.pop("adjust_points", UNSET)

        total_points = d.pop("total_points", UNSET)

        foul_count = d.pop("foul_count", UNSET)

        tote_count_far = d.pop("tote_count_far", UNSET)

        tote_count_near = d.pop("tote_count_near", UNSET)

        tote_set = d.pop("tote_set", UNSET)

        tote_stack = d.pop("tote_stack", UNSET)

        container_count_level1 = d.pop("container_count_level1", UNSET)

        container_count_level2 = d.pop("container_count_level2", UNSET)

        container_count_level3 = d.pop("container_count_level3", UNSET)

        container_count_level4 = d.pop("container_count_level4", UNSET)

        container_count_level5 = d.pop("container_count_level5", UNSET)

        container_count_level6 = d.pop("container_count_level6", UNSET)

        container_set = d.pop("container_set", UNSET)

        litter_count_container = d.pop("litter_count_container", UNSET)

        litter_count_landfill = d.pop("litter_count_landfill", UNSET)

        litter_count_unprocessed = d.pop("litter_count_unprocessed", UNSET)

        robot_set = d.pop("robot_set", UNSET)

        match_score_breakdown_2015_alliance = cls(
            auto=auto,
            auto_points=auto_points,
            teleop_points=teleop_points,
            container_points=container_points,
            tote_points=tote_points,
            litter_points=litter_points,
            foul=foul,
            foul_points=foul_points,
            adjust_points=adjust_points,
            total_points=total_points,
            foul_count=foul_count,
            tote_count_far=tote_count_far,
            tote_count_near=tote_count_near,
            tote_set=tote_set,
            tote_stack=tote_stack,
            container_count_level1=container_count_level1,
            container_count_level2=container_count_level2,
            container_count_level3=container_count_level3,
            container_count_level4=container_count_level4,
            container_count_level5=container_count_level5,
            container_count_level6=container_count_level6,
            container_set=container_set,
            litter_count_container=litter_count_container,
            litter_count_landfill=litter_count_landfill,
            litter_count_unprocessed=litter_count_unprocessed,
            robot_set=robot_set,
        )

        match_score_breakdown_2015_alliance.additional_properties = d
        return match_score_breakdown_2015_alliance

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
