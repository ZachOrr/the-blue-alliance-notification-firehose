from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.endgame_robot_2020 import EndgameRobot2020
from ..models.endgame_rung_is_level_2020 import EndgameRungIsLevel2020
from ..models.init_line_robot_2020 import InitLineRobot2020
from ..models.stage_3_target_color_2020 import Stage3TargetColor2020
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2020Alliance")


@_attrs_define
class MatchScoreBreakdown2020Alliance:
    """
    Attributes:
        init_line_robot_1 (InitLineRobot2020):
        endgame_robot_1 (EndgameRobot2020):
        init_line_robot_2 (InitLineRobot2020):
        endgame_robot_2 (EndgameRobot2020):
        init_line_robot_3 (InitLineRobot2020):
        endgame_robot_3 (EndgameRobot2020):
        auto_cells_bottom (int):
        auto_cells_outer (int):
        auto_cells_inner (int):
        teleop_cells_bottom (int):
        teleop_cells_outer (int):
        teleop_cells_inner (int):
        stage_1_activated (bool):
        stage_2_activated (bool):
        stage_3_activated (bool):
        stage_3_target_color (Stage3TargetColor2020):
        endgame_rung_is_level (EndgameRungIsLevel2020):
        auto_init_line_points (int):
        auto_cell_points (int):
        auto_points (int):
        teleop_cell_points (int):
        control_panel_points (int):
        endgame_points (int):
        teleop_points (int):
        shield_operational_ranking_point (bool):
        shield_energized_ranking_point (bool):
        foul_count (int):
        tech_foul_count (int):
        foul_points (int):
        total_points (int):
        tba_shield_energized_ranking_point_from_foul (bool | Unset): Unofficial TBA-computed value that indicates
            whether the shieldEnergizedRankingPoint was earned normally or awarded due to a foul.
        tba_num_robots_hanging (int | Unset): Unofficial TBA-computed value that counts the number of robots who were
            hanging at the end of the match.
        adjust_points (int | Unset):
        rp (int | Unset):
    """

    init_line_robot_1: InitLineRobot2020
    endgame_robot_1: EndgameRobot2020
    init_line_robot_2: InitLineRobot2020
    endgame_robot_2: EndgameRobot2020
    init_line_robot_3: InitLineRobot2020
    endgame_robot_3: EndgameRobot2020
    auto_cells_bottom: int
    auto_cells_outer: int
    auto_cells_inner: int
    teleop_cells_bottom: int
    teleop_cells_outer: int
    teleop_cells_inner: int
    stage_1_activated: bool
    stage_2_activated: bool
    stage_3_activated: bool
    stage_3_target_color: Stage3TargetColor2020
    endgame_rung_is_level: EndgameRungIsLevel2020
    auto_init_line_points: int
    auto_cell_points: int
    auto_points: int
    teleop_cell_points: int
    control_panel_points: int
    endgame_points: int
    teleop_points: int
    shield_operational_ranking_point: bool
    shield_energized_ranking_point: bool
    foul_count: int
    tech_foul_count: int
    foul_points: int
    total_points: int
    tba_shield_energized_ranking_point_from_foul: bool | Unset = UNSET
    tba_num_robots_hanging: int | Unset = UNSET
    adjust_points: int | Unset = UNSET
    rp: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        init_line_robot_1 = self.init_line_robot_1.value

        endgame_robot_1 = self.endgame_robot_1.value

        init_line_robot_2 = self.init_line_robot_2.value

        endgame_robot_2 = self.endgame_robot_2.value

        init_line_robot_3 = self.init_line_robot_3.value

        endgame_robot_3 = self.endgame_robot_3.value

        auto_cells_bottom = self.auto_cells_bottom

        auto_cells_outer = self.auto_cells_outer

        auto_cells_inner = self.auto_cells_inner

        teleop_cells_bottom = self.teleop_cells_bottom

        teleop_cells_outer = self.teleop_cells_outer

        teleop_cells_inner = self.teleop_cells_inner

        stage_1_activated = self.stage_1_activated

        stage_2_activated = self.stage_2_activated

        stage_3_activated = self.stage_3_activated

        stage_3_target_color = self.stage_3_target_color.value

        endgame_rung_is_level = self.endgame_rung_is_level.value

        auto_init_line_points = self.auto_init_line_points

        auto_cell_points = self.auto_cell_points

        auto_points = self.auto_points

        teleop_cell_points = self.teleop_cell_points

        control_panel_points = self.control_panel_points

        endgame_points = self.endgame_points

        teleop_points = self.teleop_points

        shield_operational_ranking_point = self.shield_operational_ranking_point

        shield_energized_ranking_point = self.shield_energized_ranking_point

        foul_count = self.foul_count

        tech_foul_count = self.tech_foul_count

        foul_points = self.foul_points

        total_points = self.total_points

        tba_shield_energized_ranking_point_from_foul = self.tba_shield_energized_ranking_point_from_foul

        tba_num_robots_hanging = self.tba_num_robots_hanging

        adjust_points = self.adjust_points

        rp = self.rp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "initLineRobot1": init_line_robot_1,
                "endgameRobot1": endgame_robot_1,
                "initLineRobot2": init_line_robot_2,
                "endgameRobot2": endgame_robot_2,
                "initLineRobot3": init_line_robot_3,
                "endgameRobot3": endgame_robot_3,
                "autoCellsBottom": auto_cells_bottom,
                "autoCellsOuter": auto_cells_outer,
                "autoCellsInner": auto_cells_inner,
                "teleopCellsBottom": teleop_cells_bottom,
                "teleopCellsOuter": teleop_cells_outer,
                "teleopCellsInner": teleop_cells_inner,
                "stage1Activated": stage_1_activated,
                "stage2Activated": stage_2_activated,
                "stage3Activated": stage_3_activated,
                "stage3TargetColor": stage_3_target_color,
                "endgameRungIsLevel": endgame_rung_is_level,
                "autoInitLinePoints": auto_init_line_points,
                "autoCellPoints": auto_cell_points,
                "autoPoints": auto_points,
                "teleopCellPoints": teleop_cell_points,
                "controlPanelPoints": control_panel_points,
                "endgamePoints": endgame_points,
                "teleopPoints": teleop_points,
                "shieldOperationalRankingPoint": shield_operational_ranking_point,
                "shieldEnergizedRankingPoint": shield_energized_ranking_point,
                "foulCount": foul_count,
                "techFoulCount": tech_foul_count,
                "foulPoints": foul_points,
                "totalPoints": total_points,
            }
        )
        if tba_shield_energized_ranking_point_from_foul is not UNSET:
            field_dict["tba_shieldEnergizedRankingPointFromFoul"] = tba_shield_energized_ranking_point_from_foul
        if tba_num_robots_hanging is not UNSET:
            field_dict["tba_numRobotsHanging"] = tba_num_robots_hanging
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if rp is not UNSET:
            field_dict["rp"] = rp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        init_line_robot_1 = InitLineRobot2020(d.pop("initLineRobot1"))

        endgame_robot_1 = EndgameRobot2020(d.pop("endgameRobot1"))

        init_line_robot_2 = InitLineRobot2020(d.pop("initLineRobot2"))

        endgame_robot_2 = EndgameRobot2020(d.pop("endgameRobot2"))

        init_line_robot_3 = InitLineRobot2020(d.pop("initLineRobot3"))

        endgame_robot_3 = EndgameRobot2020(d.pop("endgameRobot3"))

        auto_cells_bottom = d.pop("autoCellsBottom")

        auto_cells_outer = d.pop("autoCellsOuter")

        auto_cells_inner = d.pop("autoCellsInner")

        teleop_cells_bottom = d.pop("teleopCellsBottom")

        teleop_cells_outer = d.pop("teleopCellsOuter")

        teleop_cells_inner = d.pop("teleopCellsInner")

        stage_1_activated = d.pop("stage1Activated")

        stage_2_activated = d.pop("stage2Activated")

        stage_3_activated = d.pop("stage3Activated")

        stage_3_target_color = Stage3TargetColor2020(d.pop("stage3TargetColor"))

        endgame_rung_is_level = EndgameRungIsLevel2020(d.pop("endgameRungIsLevel"))

        auto_init_line_points = d.pop("autoInitLinePoints")

        auto_cell_points = d.pop("autoCellPoints")

        auto_points = d.pop("autoPoints")

        teleop_cell_points = d.pop("teleopCellPoints")

        control_panel_points = d.pop("controlPanelPoints")

        endgame_points = d.pop("endgamePoints")

        teleop_points = d.pop("teleopPoints")

        shield_operational_ranking_point = d.pop("shieldOperationalRankingPoint")

        shield_energized_ranking_point = d.pop("shieldEnergizedRankingPoint")

        foul_count = d.pop("foulCount")

        tech_foul_count = d.pop("techFoulCount")

        foul_points = d.pop("foulPoints")

        total_points = d.pop("totalPoints")

        tba_shield_energized_ranking_point_from_foul = d.pop("tba_shieldEnergizedRankingPointFromFoul", UNSET)

        tba_num_robots_hanging = d.pop("tba_numRobotsHanging", UNSET)

        adjust_points = d.pop("adjustPoints", UNSET)

        rp = d.pop("rp", UNSET)

        match_score_breakdown_2020_alliance = cls(
            init_line_robot_1=init_line_robot_1,
            endgame_robot_1=endgame_robot_1,
            init_line_robot_2=init_line_robot_2,
            endgame_robot_2=endgame_robot_2,
            init_line_robot_3=init_line_robot_3,
            endgame_robot_3=endgame_robot_3,
            auto_cells_bottom=auto_cells_bottom,
            auto_cells_outer=auto_cells_outer,
            auto_cells_inner=auto_cells_inner,
            teleop_cells_bottom=teleop_cells_bottom,
            teleop_cells_outer=teleop_cells_outer,
            teleop_cells_inner=teleop_cells_inner,
            stage_1_activated=stage_1_activated,
            stage_2_activated=stage_2_activated,
            stage_3_activated=stage_3_activated,
            stage_3_target_color=stage_3_target_color,
            endgame_rung_is_level=endgame_rung_is_level,
            auto_init_line_points=auto_init_line_points,
            auto_cell_points=auto_cell_points,
            auto_points=auto_points,
            teleop_cell_points=teleop_cell_points,
            control_panel_points=control_panel_points,
            endgame_points=endgame_points,
            teleop_points=teleop_points,
            shield_operational_ranking_point=shield_operational_ranking_point,
            shield_energized_ranking_point=shield_energized_ranking_point,
            foul_count=foul_count,
            tech_foul_count=tech_foul_count,
            foul_points=foul_points,
            total_points=total_points,
            tba_shield_energized_ranking_point_from_foul=tba_shield_energized_ranking_point_from_foul,
            tba_num_robots_hanging=tba_num_robots_hanging,
            adjust_points=adjust_points,
            rp=rp,
        )

        match_score_breakdown_2020_alliance.additional_properties = d
        return match_score_breakdown_2020_alliance

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
