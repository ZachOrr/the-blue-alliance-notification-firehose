from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tower_robot_2026 import TowerRobot2026

if TYPE_CHECKING:
    from ..models.hub_score_2026 import HubScore2026


T = TypeVar("T", bound="MatchScoreBreakdown2026Alliance")


@_attrs_define
class MatchScoreBreakdown2026Alliance:
    """
    Attributes:
        adjust_points (int):
        auto_tower_points (int):
        auto_tower_robot_1 (TowerRobot2026):
        auto_tower_robot_2 (TowerRobot2026):
        auto_tower_robot_3 (TowerRobot2026):
        end_game_tower_points (int):
        end_game_tower_robot_1 (TowerRobot2026):
        end_game_tower_robot_2 (TowerRobot2026):
        end_game_tower_robot_3 (TowerRobot2026):
        energized_achieved (bool):
        foul_points (int):
        g_206_penalty (bool):
        hub_score (HubScore2026):
        major_foul_count (int):
        minor_foul_count (int):
        rp (int):
        supercharged_achieved (bool):
        total_auto_points (int):
        total_points (int):
        total_teleop_points (int):
        total_tower_points (int):
        traversal_achieved (bool):
    """

    adjust_points: int
    auto_tower_points: int
    auto_tower_robot_1: TowerRobot2026
    auto_tower_robot_2: TowerRobot2026
    auto_tower_robot_3: TowerRobot2026
    end_game_tower_points: int
    end_game_tower_robot_1: TowerRobot2026
    end_game_tower_robot_2: TowerRobot2026
    end_game_tower_robot_3: TowerRobot2026
    energized_achieved: bool
    foul_points: int
    g_206_penalty: bool
    hub_score: HubScore2026
    major_foul_count: int
    minor_foul_count: int
    rp: int
    supercharged_achieved: bool
    total_auto_points: int
    total_points: int
    total_teleop_points: int
    total_tower_points: int
    traversal_achieved: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adjust_points = self.adjust_points

        auto_tower_points = self.auto_tower_points

        auto_tower_robot_1 = self.auto_tower_robot_1.value

        auto_tower_robot_2 = self.auto_tower_robot_2.value

        auto_tower_robot_3 = self.auto_tower_robot_3.value

        end_game_tower_points = self.end_game_tower_points

        end_game_tower_robot_1 = self.end_game_tower_robot_1.value

        end_game_tower_robot_2 = self.end_game_tower_robot_2.value

        end_game_tower_robot_3 = self.end_game_tower_robot_3.value

        energized_achieved = self.energized_achieved

        foul_points = self.foul_points

        g_206_penalty = self.g_206_penalty

        hub_score = self.hub_score.to_dict()

        major_foul_count = self.major_foul_count

        minor_foul_count = self.minor_foul_count

        rp = self.rp

        supercharged_achieved = self.supercharged_achieved

        total_auto_points = self.total_auto_points

        total_points = self.total_points

        total_teleop_points = self.total_teleop_points

        total_tower_points = self.total_tower_points

        traversal_achieved = self.traversal_achieved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adjustPoints": adjust_points,
                "autoTowerPoints": auto_tower_points,
                "autoTowerRobot1": auto_tower_robot_1,
                "autoTowerRobot2": auto_tower_robot_2,
                "autoTowerRobot3": auto_tower_robot_3,
                "endGameTowerPoints": end_game_tower_points,
                "endGameTowerRobot1": end_game_tower_robot_1,
                "endGameTowerRobot2": end_game_tower_robot_2,
                "endGameTowerRobot3": end_game_tower_robot_3,
                "energizedAchieved": energized_achieved,
                "foulPoints": foul_points,
                "g206Penalty": g_206_penalty,
                "hubScore": hub_score,
                "majorFoulCount": major_foul_count,
                "minorFoulCount": minor_foul_count,
                "rp": rp,
                "superchargedAchieved": supercharged_achieved,
                "totalAutoPoints": total_auto_points,
                "totalPoints": total_points,
                "totalTeleopPoints": total_teleop_points,
                "totalTowerPoints": total_tower_points,
                "traversalAchieved": traversal_achieved,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hub_score_2026 import HubScore2026

        d = dict(src_dict)
        adjust_points = d.pop("adjustPoints")

        auto_tower_points = d.pop("autoTowerPoints")

        auto_tower_robot_1 = TowerRobot2026(d.pop("autoTowerRobot1"))

        auto_tower_robot_2 = TowerRobot2026(d.pop("autoTowerRobot2"))

        auto_tower_robot_3 = TowerRobot2026(d.pop("autoTowerRobot3"))

        end_game_tower_points = d.pop("endGameTowerPoints")

        end_game_tower_robot_1 = TowerRobot2026(d.pop("endGameTowerRobot1"))

        end_game_tower_robot_2 = TowerRobot2026(d.pop("endGameTowerRobot2"))

        end_game_tower_robot_3 = TowerRobot2026(d.pop("endGameTowerRobot3"))

        energized_achieved = d.pop("energizedAchieved")

        foul_points = d.pop("foulPoints")

        g_206_penalty = d.pop("g206Penalty")

        hub_score = HubScore2026.from_dict(d.pop("hubScore"))

        major_foul_count = d.pop("majorFoulCount")

        minor_foul_count = d.pop("minorFoulCount")

        rp = d.pop("rp")

        supercharged_achieved = d.pop("superchargedAchieved")

        total_auto_points = d.pop("totalAutoPoints")

        total_points = d.pop("totalPoints")

        total_teleop_points = d.pop("totalTeleopPoints")

        total_tower_points = d.pop("totalTowerPoints")

        traversal_achieved = d.pop("traversalAchieved")

        match_score_breakdown_2026_alliance = cls(
            adjust_points=adjust_points,
            auto_tower_points=auto_tower_points,
            auto_tower_robot_1=auto_tower_robot_1,
            auto_tower_robot_2=auto_tower_robot_2,
            auto_tower_robot_3=auto_tower_robot_3,
            end_game_tower_points=end_game_tower_points,
            end_game_tower_robot_1=end_game_tower_robot_1,
            end_game_tower_robot_2=end_game_tower_robot_2,
            end_game_tower_robot_3=end_game_tower_robot_3,
            energized_achieved=energized_achieved,
            foul_points=foul_points,
            g_206_penalty=g_206_penalty,
            hub_score=hub_score,
            major_foul_count=major_foul_count,
            minor_foul_count=minor_foul_count,
            rp=rp,
            supercharged_achieved=supercharged_achieved,
            total_auto_points=total_auto_points,
            total_points=total_points,
            total_teleop_points=total_teleop_points,
            total_tower_points=total_tower_points,
            traversal_achieved=traversal_achieved,
        )

        match_score_breakdown_2026_alliance.additional_properties = d
        return match_score_breakdown_2026_alliance

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
