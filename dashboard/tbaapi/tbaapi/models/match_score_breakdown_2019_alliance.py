from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bay_2019 import Bay2019
from ..models.endgame_robot_2019 import EndgameRobot2019
from ..models.hab_line_2019 import HabLine2019
from ..models.pre_match_bay_2019 import PreMatchBay2019
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2019Alliance")


@_attrs_define
class MatchScoreBreakdown2019Alliance:
    """
    Attributes:
        bay1 (Bay2019):
        bay2 (Bay2019):
        bay3 (Bay2019):
        bay4 (Bay2019):
        bay5 (Bay2019):
        bay6 (Bay2019):
        bay7 (Bay2019):
        bay8 (Bay2019):
        cargo_points (int):
        complete_rocket_ranking_point (bool):
        endgame_robot_1 (EndgameRobot2019):
        endgame_robot_2 (EndgameRobot2019):
        endgame_robot_3 (EndgameRobot2019):
        foul_points (int):
        hab_climb_points (int):
        hab_docking_ranking_point (bool):
        hab_line_robot_1 (HabLine2019):
        hab_line_robot_2 (HabLine2019):
        hab_line_robot_3 (HabLine2019):
        hatch_panel_points (int):
        low_left_rocket_far (Bay2019):
        low_left_rocket_near (Bay2019):
        low_right_rocket_far (Bay2019):
        low_right_rocket_near (Bay2019):
        mid_left_rocket_far (Bay2019):
        mid_left_rocket_near (Bay2019):
        mid_right_rocket_far (Bay2019):
        mid_right_rocket_near (Bay2019):
        pre_match_bay_1 (PreMatchBay2019):
        pre_match_bay_2 (PreMatchBay2019):
        pre_match_bay_3 (PreMatchBay2019):
        pre_match_bay_6 (PreMatchBay2019):
        pre_match_bay_7 (PreMatchBay2019):
        pre_match_bay_8 (PreMatchBay2019):
        pre_match_level_robot_1 (EndgameRobot2019):
        pre_match_level_robot_2 (EndgameRobot2019):
        pre_match_level_robot_3 (EndgameRobot2019):
        rp (int):
        sand_storm_bonus_points (int):
        teleop_points (int):
        top_left_rocket_far (Bay2019):
        top_left_rocket_near (Bay2019):
        top_right_rocket_far (Bay2019):
        top_right_rocket_near (Bay2019):
        total_points (int):
        adjust_points (int | Unset):
        auto_points (int | Unset):
        completed_rocket_far (bool | Unset):
        completed_rocket_near (bool | Unset):
        foul_count (int | Unset):
        tech_foul_count (int | Unset):
    """

    bay1: Bay2019
    bay2: Bay2019
    bay3: Bay2019
    bay4: Bay2019
    bay5: Bay2019
    bay6: Bay2019
    bay7: Bay2019
    bay8: Bay2019
    cargo_points: int
    complete_rocket_ranking_point: bool
    endgame_robot_1: EndgameRobot2019
    endgame_robot_2: EndgameRobot2019
    endgame_robot_3: EndgameRobot2019
    foul_points: int
    hab_climb_points: int
    hab_docking_ranking_point: bool
    hab_line_robot_1: HabLine2019
    hab_line_robot_2: HabLine2019
    hab_line_robot_3: HabLine2019
    hatch_panel_points: int
    low_left_rocket_far: Bay2019
    low_left_rocket_near: Bay2019
    low_right_rocket_far: Bay2019
    low_right_rocket_near: Bay2019
    mid_left_rocket_far: Bay2019
    mid_left_rocket_near: Bay2019
    mid_right_rocket_far: Bay2019
    mid_right_rocket_near: Bay2019
    pre_match_bay_1: PreMatchBay2019
    pre_match_bay_2: PreMatchBay2019
    pre_match_bay_3: PreMatchBay2019
    pre_match_bay_6: PreMatchBay2019
    pre_match_bay_7: PreMatchBay2019
    pre_match_bay_8: PreMatchBay2019
    pre_match_level_robot_1: EndgameRobot2019
    pre_match_level_robot_2: EndgameRobot2019
    pre_match_level_robot_3: EndgameRobot2019
    rp: int
    sand_storm_bonus_points: int
    teleop_points: int
    top_left_rocket_far: Bay2019
    top_left_rocket_near: Bay2019
    top_right_rocket_far: Bay2019
    top_right_rocket_near: Bay2019
    total_points: int
    adjust_points: int | Unset = UNSET
    auto_points: int | Unset = UNSET
    completed_rocket_far: bool | Unset = UNSET
    completed_rocket_near: bool | Unset = UNSET
    foul_count: int | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bay1 = self.bay1.value

        bay2 = self.bay2.value

        bay3 = self.bay3.value

        bay4 = self.bay4.value

        bay5 = self.bay5.value

        bay6 = self.bay6.value

        bay7 = self.bay7.value

        bay8 = self.bay8.value

        cargo_points = self.cargo_points

        complete_rocket_ranking_point = self.complete_rocket_ranking_point

        endgame_robot_1 = self.endgame_robot_1.value

        endgame_robot_2 = self.endgame_robot_2.value

        endgame_robot_3 = self.endgame_robot_3.value

        foul_points = self.foul_points

        hab_climb_points = self.hab_climb_points

        hab_docking_ranking_point = self.hab_docking_ranking_point

        hab_line_robot_1 = self.hab_line_robot_1.value

        hab_line_robot_2 = self.hab_line_robot_2.value

        hab_line_robot_3 = self.hab_line_robot_3.value

        hatch_panel_points = self.hatch_panel_points

        low_left_rocket_far = self.low_left_rocket_far.value

        low_left_rocket_near = self.low_left_rocket_near.value

        low_right_rocket_far = self.low_right_rocket_far.value

        low_right_rocket_near = self.low_right_rocket_near.value

        mid_left_rocket_far = self.mid_left_rocket_far.value

        mid_left_rocket_near = self.mid_left_rocket_near.value

        mid_right_rocket_far = self.mid_right_rocket_far.value

        mid_right_rocket_near = self.mid_right_rocket_near.value

        pre_match_bay_1 = self.pre_match_bay_1.value

        pre_match_bay_2 = self.pre_match_bay_2.value

        pre_match_bay_3 = self.pre_match_bay_3.value

        pre_match_bay_6 = self.pre_match_bay_6.value

        pre_match_bay_7 = self.pre_match_bay_7.value

        pre_match_bay_8 = self.pre_match_bay_8.value

        pre_match_level_robot_1 = self.pre_match_level_robot_1.value

        pre_match_level_robot_2 = self.pre_match_level_robot_2.value

        pre_match_level_robot_3 = self.pre_match_level_robot_3.value

        rp = self.rp

        sand_storm_bonus_points = self.sand_storm_bonus_points

        teleop_points = self.teleop_points

        top_left_rocket_far = self.top_left_rocket_far.value

        top_left_rocket_near = self.top_left_rocket_near.value

        top_right_rocket_far = self.top_right_rocket_far.value

        top_right_rocket_near = self.top_right_rocket_near.value

        total_points = self.total_points

        adjust_points = self.adjust_points

        auto_points = self.auto_points

        completed_rocket_far = self.completed_rocket_far

        completed_rocket_near = self.completed_rocket_near

        foul_count = self.foul_count

        tech_foul_count = self.tech_foul_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bay1": bay1,
                "bay2": bay2,
                "bay3": bay3,
                "bay4": bay4,
                "bay5": bay5,
                "bay6": bay6,
                "bay7": bay7,
                "bay8": bay8,
                "cargoPoints": cargo_points,
                "completeRocketRankingPoint": complete_rocket_ranking_point,
                "endgameRobot1": endgame_robot_1,
                "endgameRobot2": endgame_robot_2,
                "endgameRobot3": endgame_robot_3,
                "foulPoints": foul_points,
                "habClimbPoints": hab_climb_points,
                "habDockingRankingPoint": hab_docking_ranking_point,
                "habLineRobot1": hab_line_robot_1,
                "habLineRobot2": hab_line_robot_2,
                "habLineRobot3": hab_line_robot_3,
                "hatchPanelPoints": hatch_panel_points,
                "lowLeftRocketFar": low_left_rocket_far,
                "lowLeftRocketNear": low_left_rocket_near,
                "lowRightRocketFar": low_right_rocket_far,
                "lowRightRocketNear": low_right_rocket_near,
                "midLeftRocketFar": mid_left_rocket_far,
                "midLeftRocketNear": mid_left_rocket_near,
                "midRightRocketFar": mid_right_rocket_far,
                "midRightRocketNear": mid_right_rocket_near,
                "preMatchBay1": pre_match_bay_1,
                "preMatchBay2": pre_match_bay_2,
                "preMatchBay3": pre_match_bay_3,
                "preMatchBay6": pre_match_bay_6,
                "preMatchBay7": pre_match_bay_7,
                "preMatchBay8": pre_match_bay_8,
                "preMatchLevelRobot1": pre_match_level_robot_1,
                "preMatchLevelRobot2": pre_match_level_robot_2,
                "preMatchLevelRobot3": pre_match_level_robot_3,
                "rp": rp,
                "sandStormBonusPoints": sand_storm_bonus_points,
                "teleopPoints": teleop_points,
                "topLeftRocketFar": top_left_rocket_far,
                "topLeftRocketNear": top_left_rocket_near,
                "topRightRocketFar": top_right_rocket_far,
                "topRightRocketNear": top_right_rocket_near,
                "totalPoints": total_points,
            }
        )
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if completed_rocket_far is not UNSET:
            field_dict["completedRocketFar"] = completed_rocket_far
        if completed_rocket_near is not UNSET:
            field_dict["completedRocketNear"] = completed_rocket_near
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bay1 = Bay2019(d.pop("bay1"))

        bay2 = Bay2019(d.pop("bay2"))

        bay3 = Bay2019(d.pop("bay3"))

        bay4 = Bay2019(d.pop("bay4"))

        bay5 = Bay2019(d.pop("bay5"))

        bay6 = Bay2019(d.pop("bay6"))

        bay7 = Bay2019(d.pop("bay7"))

        bay8 = Bay2019(d.pop("bay8"))

        cargo_points = d.pop("cargoPoints")

        complete_rocket_ranking_point = d.pop("completeRocketRankingPoint")

        endgame_robot_1 = EndgameRobot2019(d.pop("endgameRobot1"))

        endgame_robot_2 = EndgameRobot2019(d.pop("endgameRobot2"))

        endgame_robot_3 = EndgameRobot2019(d.pop("endgameRobot3"))

        foul_points = d.pop("foulPoints")

        hab_climb_points = d.pop("habClimbPoints")

        hab_docking_ranking_point = d.pop("habDockingRankingPoint")

        hab_line_robot_1 = HabLine2019(d.pop("habLineRobot1"))

        hab_line_robot_2 = HabLine2019(d.pop("habLineRobot2"))

        hab_line_robot_3 = HabLine2019(d.pop("habLineRobot3"))

        hatch_panel_points = d.pop("hatchPanelPoints")

        low_left_rocket_far = Bay2019(d.pop("lowLeftRocketFar"))

        low_left_rocket_near = Bay2019(d.pop("lowLeftRocketNear"))

        low_right_rocket_far = Bay2019(d.pop("lowRightRocketFar"))

        low_right_rocket_near = Bay2019(d.pop("lowRightRocketNear"))

        mid_left_rocket_far = Bay2019(d.pop("midLeftRocketFar"))

        mid_left_rocket_near = Bay2019(d.pop("midLeftRocketNear"))

        mid_right_rocket_far = Bay2019(d.pop("midRightRocketFar"))

        mid_right_rocket_near = Bay2019(d.pop("midRightRocketNear"))

        pre_match_bay_1 = PreMatchBay2019(d.pop("preMatchBay1"))

        pre_match_bay_2 = PreMatchBay2019(d.pop("preMatchBay2"))

        pre_match_bay_3 = PreMatchBay2019(d.pop("preMatchBay3"))

        pre_match_bay_6 = PreMatchBay2019(d.pop("preMatchBay6"))

        pre_match_bay_7 = PreMatchBay2019(d.pop("preMatchBay7"))

        pre_match_bay_8 = PreMatchBay2019(d.pop("preMatchBay8"))

        pre_match_level_robot_1 = EndgameRobot2019(d.pop("preMatchLevelRobot1"))

        pre_match_level_robot_2 = EndgameRobot2019(d.pop("preMatchLevelRobot2"))

        pre_match_level_robot_3 = EndgameRobot2019(d.pop("preMatchLevelRobot3"))

        rp = d.pop("rp")

        sand_storm_bonus_points = d.pop("sandStormBonusPoints")

        teleop_points = d.pop("teleopPoints")

        top_left_rocket_far = Bay2019(d.pop("topLeftRocketFar"))

        top_left_rocket_near = Bay2019(d.pop("topLeftRocketNear"))

        top_right_rocket_far = Bay2019(d.pop("topRightRocketFar"))

        top_right_rocket_near = Bay2019(d.pop("topRightRocketNear"))

        total_points = d.pop("totalPoints")

        adjust_points = d.pop("adjustPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        completed_rocket_far = d.pop("completedRocketFar", UNSET)

        completed_rocket_near = d.pop("completedRocketNear", UNSET)

        foul_count = d.pop("foulCount", UNSET)

        tech_foul_count = d.pop("techFoulCount", UNSET)

        match_score_breakdown_2019_alliance = cls(
            bay1=bay1,
            bay2=bay2,
            bay3=bay3,
            bay4=bay4,
            bay5=bay5,
            bay6=bay6,
            bay7=bay7,
            bay8=bay8,
            cargo_points=cargo_points,
            complete_rocket_ranking_point=complete_rocket_ranking_point,
            endgame_robot_1=endgame_robot_1,
            endgame_robot_2=endgame_robot_2,
            endgame_robot_3=endgame_robot_3,
            foul_points=foul_points,
            hab_climb_points=hab_climb_points,
            hab_docking_ranking_point=hab_docking_ranking_point,
            hab_line_robot_1=hab_line_robot_1,
            hab_line_robot_2=hab_line_robot_2,
            hab_line_robot_3=hab_line_robot_3,
            hatch_panel_points=hatch_panel_points,
            low_left_rocket_far=low_left_rocket_far,
            low_left_rocket_near=low_left_rocket_near,
            low_right_rocket_far=low_right_rocket_far,
            low_right_rocket_near=low_right_rocket_near,
            mid_left_rocket_far=mid_left_rocket_far,
            mid_left_rocket_near=mid_left_rocket_near,
            mid_right_rocket_far=mid_right_rocket_far,
            mid_right_rocket_near=mid_right_rocket_near,
            pre_match_bay_1=pre_match_bay_1,
            pre_match_bay_2=pre_match_bay_2,
            pre_match_bay_3=pre_match_bay_3,
            pre_match_bay_6=pre_match_bay_6,
            pre_match_bay_7=pre_match_bay_7,
            pre_match_bay_8=pre_match_bay_8,
            pre_match_level_robot_1=pre_match_level_robot_1,
            pre_match_level_robot_2=pre_match_level_robot_2,
            pre_match_level_robot_3=pre_match_level_robot_3,
            rp=rp,
            sand_storm_bonus_points=sand_storm_bonus_points,
            teleop_points=teleop_points,
            top_left_rocket_far=top_left_rocket_far,
            top_left_rocket_near=top_left_rocket_near,
            top_right_rocket_far=top_right_rocket_far,
            top_right_rocket_near=top_right_rocket_near,
            total_points=total_points,
            adjust_points=adjust_points,
            auto_points=auto_points,
            completed_rocket_far=completed_rocket_far,
            completed_rocket_near=completed_rocket_near,
            foul_count=foul_count,
            tech_foul_count=tech_foul_count,
        )

        match_score_breakdown_2019_alliance.additional_properties = d
        return match_score_breakdown_2019_alliance

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
