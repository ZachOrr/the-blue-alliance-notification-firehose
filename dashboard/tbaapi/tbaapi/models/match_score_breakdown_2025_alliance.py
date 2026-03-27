from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_line_robot_2024 import AutoLineRobot2024
from ..models.end_game_robot_2025 import EndGameRobot2025
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_score_breakdown_2025_alliance_auto_reef import MatchScoreBreakdown2025AllianceAutoReef
    from ..models.match_score_breakdown_2025_alliance_teleop_reef import MatchScoreBreakdown2025AllianceTeleopReef


T = TypeVar("T", bound="MatchScoreBreakdown2025Alliance")


@_attrs_define
class MatchScoreBreakdown2025Alliance:
    """
    Attributes:
        algae_points (int):
        auto_coral_count (int):
        auto_coral_points (int):
        auto_line_robot_1 (AutoLineRobot2024):
        auto_line_robot_2 (AutoLineRobot2024):
        auto_line_robot_3 (AutoLineRobot2024):
        auto_mobility_points (int):
        auto_points (int):
        auto_reef (MatchScoreBreakdown2025AllianceAutoReef):
        end_game_barge_points (int):
        end_game_robot_1 (EndGameRobot2025):
        end_game_robot_2 (EndGameRobot2025):
        end_game_robot_3 (EndGameRobot2025):
        foul_count (int):
        foul_points (int):
        g_206_penalty (bool):
        g_410_penalty (bool):
        g_418_penalty (bool):
        g_428_penalty (bool):
        net_algae_count (int):
        rp (int):
        tech_foul_count (int):
        teleop_coral_count (int):
        teleop_coral_points (int):
        teleop_points (int):
        teleop_reef (MatchScoreBreakdown2025AllianceTeleopReef):
        total_points (int):
        wall_algae_count (int):
        adjust_points (int | Unset):
        auto_bonus_achieved (bool | Unset):
        barge_bonus_achieved (bool | Unset):
        coopertition_criteria_met (bool | Unset):
        coral_bonus_achieved (bool | Unset):
    """

    algae_points: int
    auto_coral_count: int
    auto_coral_points: int
    auto_line_robot_1: AutoLineRobot2024
    auto_line_robot_2: AutoLineRobot2024
    auto_line_robot_3: AutoLineRobot2024
    auto_mobility_points: int
    auto_points: int
    auto_reef: MatchScoreBreakdown2025AllianceAutoReef
    end_game_barge_points: int
    end_game_robot_1: EndGameRobot2025
    end_game_robot_2: EndGameRobot2025
    end_game_robot_3: EndGameRobot2025
    foul_count: int
    foul_points: int
    g_206_penalty: bool
    g_410_penalty: bool
    g_418_penalty: bool
    g_428_penalty: bool
    net_algae_count: int
    rp: int
    tech_foul_count: int
    teleop_coral_count: int
    teleop_coral_points: int
    teleop_points: int
    teleop_reef: MatchScoreBreakdown2025AllianceTeleopReef
    total_points: int
    wall_algae_count: int
    adjust_points: int | Unset = UNSET
    auto_bonus_achieved: bool | Unset = UNSET
    barge_bonus_achieved: bool | Unset = UNSET
    coopertition_criteria_met: bool | Unset = UNSET
    coral_bonus_achieved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algae_points = self.algae_points

        auto_coral_count = self.auto_coral_count

        auto_coral_points = self.auto_coral_points

        auto_line_robot_1 = self.auto_line_robot_1.value

        auto_line_robot_2 = self.auto_line_robot_2.value

        auto_line_robot_3 = self.auto_line_robot_3.value

        auto_mobility_points = self.auto_mobility_points

        auto_points = self.auto_points

        auto_reef = self.auto_reef.to_dict()

        end_game_barge_points = self.end_game_barge_points

        end_game_robot_1 = self.end_game_robot_1.value

        end_game_robot_2 = self.end_game_robot_2.value

        end_game_robot_3 = self.end_game_robot_3.value

        foul_count = self.foul_count

        foul_points = self.foul_points

        g_206_penalty = self.g_206_penalty

        g_410_penalty = self.g_410_penalty

        g_418_penalty = self.g_418_penalty

        g_428_penalty = self.g_428_penalty

        net_algae_count = self.net_algae_count

        rp = self.rp

        tech_foul_count = self.tech_foul_count

        teleop_coral_count = self.teleop_coral_count

        teleop_coral_points = self.teleop_coral_points

        teleop_points = self.teleop_points

        teleop_reef = self.teleop_reef.to_dict()

        total_points = self.total_points

        wall_algae_count = self.wall_algae_count

        adjust_points = self.adjust_points

        auto_bonus_achieved = self.auto_bonus_achieved

        barge_bonus_achieved = self.barge_bonus_achieved

        coopertition_criteria_met = self.coopertition_criteria_met

        coral_bonus_achieved = self.coral_bonus_achieved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algaePoints": algae_points,
                "autoCoralCount": auto_coral_count,
                "autoCoralPoints": auto_coral_points,
                "autoLineRobot1": auto_line_robot_1,
                "autoLineRobot2": auto_line_robot_2,
                "autoLineRobot3": auto_line_robot_3,
                "autoMobilityPoints": auto_mobility_points,
                "autoPoints": auto_points,
                "autoReef": auto_reef,
                "endGameBargePoints": end_game_barge_points,
                "endGameRobot1": end_game_robot_1,
                "endGameRobot2": end_game_robot_2,
                "endGameRobot3": end_game_robot_3,
                "foulCount": foul_count,
                "foulPoints": foul_points,
                "g206Penalty": g_206_penalty,
                "g410Penalty": g_410_penalty,
                "g418Penalty": g_418_penalty,
                "g428Penalty": g_428_penalty,
                "netAlgaeCount": net_algae_count,
                "rp": rp,
                "techFoulCount": tech_foul_count,
                "teleopCoralCount": teleop_coral_count,
                "teleopCoralPoints": teleop_coral_points,
                "teleopPoints": teleop_points,
                "teleopReef": teleop_reef,
                "totalPoints": total_points,
                "wallAlgaeCount": wall_algae_count,
            }
        )
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if auto_bonus_achieved is not UNSET:
            field_dict["autoBonusAchieved"] = auto_bonus_achieved
        if barge_bonus_achieved is not UNSET:
            field_dict["bargeBonusAchieved"] = barge_bonus_achieved
        if coopertition_criteria_met is not UNSET:
            field_dict["coopertitionCriteriaMet"] = coopertition_criteria_met
        if coral_bonus_achieved is not UNSET:
            field_dict["coralBonusAchieved"] = coral_bonus_achieved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_score_breakdown_2025_alliance_auto_reef import MatchScoreBreakdown2025AllianceAutoReef
        from ..models.match_score_breakdown_2025_alliance_teleop_reef import MatchScoreBreakdown2025AllianceTeleopReef

        d = dict(src_dict)
        algae_points = d.pop("algaePoints")

        auto_coral_count = d.pop("autoCoralCount")

        auto_coral_points = d.pop("autoCoralPoints")

        auto_line_robot_1 = AutoLineRobot2024(d.pop("autoLineRobot1"))

        auto_line_robot_2 = AutoLineRobot2024(d.pop("autoLineRobot2"))

        auto_line_robot_3 = AutoLineRobot2024(d.pop("autoLineRobot3"))

        auto_mobility_points = d.pop("autoMobilityPoints")

        auto_points = d.pop("autoPoints")

        auto_reef = MatchScoreBreakdown2025AllianceAutoReef.from_dict(d.pop("autoReef"))

        end_game_barge_points = d.pop("endGameBargePoints")

        end_game_robot_1 = EndGameRobot2025(d.pop("endGameRobot1"))

        end_game_robot_2 = EndGameRobot2025(d.pop("endGameRobot2"))

        end_game_robot_3 = EndGameRobot2025(d.pop("endGameRobot3"))

        foul_count = d.pop("foulCount")

        foul_points = d.pop("foulPoints")

        g_206_penalty = d.pop("g206Penalty")

        g_410_penalty = d.pop("g410Penalty")

        g_418_penalty = d.pop("g418Penalty")

        g_428_penalty = d.pop("g428Penalty")

        net_algae_count = d.pop("netAlgaeCount")

        rp = d.pop("rp")

        tech_foul_count = d.pop("techFoulCount")

        teleop_coral_count = d.pop("teleopCoralCount")

        teleop_coral_points = d.pop("teleopCoralPoints")

        teleop_points = d.pop("teleopPoints")

        teleop_reef = MatchScoreBreakdown2025AllianceTeleopReef.from_dict(d.pop("teleopReef"))

        total_points = d.pop("totalPoints")

        wall_algae_count = d.pop("wallAlgaeCount")

        adjust_points = d.pop("adjustPoints", UNSET)

        auto_bonus_achieved = d.pop("autoBonusAchieved", UNSET)

        barge_bonus_achieved = d.pop("bargeBonusAchieved", UNSET)

        coopertition_criteria_met = d.pop("coopertitionCriteriaMet", UNSET)

        coral_bonus_achieved = d.pop("coralBonusAchieved", UNSET)

        match_score_breakdown_2025_alliance = cls(
            algae_points=algae_points,
            auto_coral_count=auto_coral_count,
            auto_coral_points=auto_coral_points,
            auto_line_robot_1=auto_line_robot_1,
            auto_line_robot_2=auto_line_robot_2,
            auto_line_robot_3=auto_line_robot_3,
            auto_mobility_points=auto_mobility_points,
            auto_points=auto_points,
            auto_reef=auto_reef,
            end_game_barge_points=end_game_barge_points,
            end_game_robot_1=end_game_robot_1,
            end_game_robot_2=end_game_robot_2,
            end_game_robot_3=end_game_robot_3,
            foul_count=foul_count,
            foul_points=foul_points,
            g_206_penalty=g_206_penalty,
            g_410_penalty=g_410_penalty,
            g_418_penalty=g_418_penalty,
            g_428_penalty=g_428_penalty,
            net_algae_count=net_algae_count,
            rp=rp,
            tech_foul_count=tech_foul_count,
            teleop_coral_count=teleop_coral_count,
            teleop_coral_points=teleop_coral_points,
            teleop_points=teleop_points,
            teleop_reef=teleop_reef,
            total_points=total_points,
            wall_algae_count=wall_algae_count,
            adjust_points=adjust_points,
            auto_bonus_achieved=auto_bonus_achieved,
            barge_bonus_achieved=barge_bonus_achieved,
            coopertition_criteria_met=coopertition_criteria_met,
            coral_bonus_achieved=coral_bonus_achieved,
        )

        match_score_breakdown_2025_alliance.additional_properties = d
        return match_score_breakdown_2025_alliance

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
