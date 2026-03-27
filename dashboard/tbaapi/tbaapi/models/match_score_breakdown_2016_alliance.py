from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_2016 import Position2016
from ..models.robot_auto_2016_with_unknown import RobotAuto2016WithUnknown
from ..models.robot_auto_2016_without_unknown import RobotAuto2016WithoutUnknown
from ..models.tower_face_2016 import TowerFace2016
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2016Alliance")


@_attrs_define
class MatchScoreBreakdown2016Alliance:
    """
    Attributes:
        auto_points (int):
        breach_points (int):
        foul_points (int):
        capture_points (int):
        total_points (int):
        tba_rp_earned (int | None):
        auto_reach_points (int):
        auto_crossing_points (int):
        auto_boulder_points (int):
        teleop_crossing_points (int):
        teleop_boulders_low (int):
        teleop_boulders_high (int):
        teleop_boulder_points (int):
        teleop_defenses_breached (bool):
        teleop_challenge_points (int):
        teleop_scale_points (int):
        teleop_tower_captured (bool):
        position2 (Position2016):
        position3 (Position2016):
        position4 (Position2016):
        position5 (Position2016):
        position1crossings (int):
        position2crossings (int):
        position3crossings (int):
        position4crossings (int):
        position5crossings (int):
        teleop_points (int | Unset):
        adjust_points (int | Unset):
        robot_1_auto (RobotAuto2016WithUnknown | Unset):
        robot_2_auto (RobotAuto2016WithoutUnknown | Unset):
        robot_3_auto (RobotAuto2016WithUnknown | Unset):
        auto_boulders_low (int | Unset):
        auto_boulders_high (int | Unset):
        tower_face_a (TowerFace2016 | Unset):
        tower_face_b (TowerFace2016 | Unset):
        tower_face_c (TowerFace2016 | Unset):
        tower_end_strength (int | Unset):
        tech_foul_count (int | Unset):
        foul_count (int | Unset):
    """

    auto_points: int
    breach_points: int
    foul_points: int
    capture_points: int
    total_points: int
    tba_rp_earned: int | None
    auto_reach_points: int
    auto_crossing_points: int
    auto_boulder_points: int
    teleop_crossing_points: int
    teleop_boulders_low: int
    teleop_boulders_high: int
    teleop_boulder_points: int
    teleop_defenses_breached: bool
    teleop_challenge_points: int
    teleop_scale_points: int
    teleop_tower_captured: bool
    position2: Position2016
    position3: Position2016
    position4: Position2016
    position5: Position2016
    position1crossings: int
    position2crossings: int
    position3crossings: int
    position4crossings: int
    position5crossings: int
    teleop_points: int | Unset = UNSET
    adjust_points: int | Unset = UNSET
    robot_1_auto: RobotAuto2016WithUnknown | Unset = UNSET
    robot_2_auto: RobotAuto2016WithoutUnknown | Unset = UNSET
    robot_3_auto: RobotAuto2016WithUnknown | Unset = UNSET
    auto_boulders_low: int | Unset = UNSET
    auto_boulders_high: int | Unset = UNSET
    tower_face_a: TowerFace2016 | Unset = UNSET
    tower_face_b: TowerFace2016 | Unset = UNSET
    tower_face_c: TowerFace2016 | Unset = UNSET
    tower_end_strength: int | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    foul_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_points = self.auto_points

        breach_points = self.breach_points

        foul_points = self.foul_points

        capture_points = self.capture_points

        total_points = self.total_points

        tba_rp_earned: int | None
        tba_rp_earned = self.tba_rp_earned

        auto_reach_points = self.auto_reach_points

        auto_crossing_points = self.auto_crossing_points

        auto_boulder_points = self.auto_boulder_points

        teleop_crossing_points = self.teleop_crossing_points

        teleop_boulders_low = self.teleop_boulders_low

        teleop_boulders_high = self.teleop_boulders_high

        teleop_boulder_points = self.teleop_boulder_points

        teleop_defenses_breached = self.teleop_defenses_breached

        teleop_challenge_points = self.teleop_challenge_points

        teleop_scale_points = self.teleop_scale_points

        teleop_tower_captured = self.teleop_tower_captured

        position2 = self.position2.value

        position3 = self.position3.value

        position4 = self.position4.value

        position5 = self.position5.value

        position1crossings = self.position1crossings

        position2crossings = self.position2crossings

        position3crossings = self.position3crossings

        position4crossings = self.position4crossings

        position5crossings = self.position5crossings

        teleop_points = self.teleop_points

        adjust_points = self.adjust_points

        robot_1_auto: str | Unset = UNSET
        if not isinstance(self.robot_1_auto, Unset):
            robot_1_auto = self.robot_1_auto.value

        robot_2_auto: str | Unset = UNSET
        if not isinstance(self.robot_2_auto, Unset):
            robot_2_auto = self.robot_2_auto.value

        robot_3_auto: str | Unset = UNSET
        if not isinstance(self.robot_3_auto, Unset):
            robot_3_auto = self.robot_3_auto.value

        auto_boulders_low = self.auto_boulders_low

        auto_boulders_high = self.auto_boulders_high

        tower_face_a: str | Unset = UNSET
        if not isinstance(self.tower_face_a, Unset):
            tower_face_a = self.tower_face_a.value

        tower_face_b: str | Unset = UNSET
        if not isinstance(self.tower_face_b, Unset):
            tower_face_b = self.tower_face_b.value

        tower_face_c: str | Unset = UNSET
        if not isinstance(self.tower_face_c, Unset):
            tower_face_c = self.tower_face_c.value

        tower_end_strength = self.tower_end_strength

        tech_foul_count = self.tech_foul_count

        foul_count = self.foul_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoPoints": auto_points,
                "breachPoints": breach_points,
                "foulPoints": foul_points,
                "capturePoints": capture_points,
                "totalPoints": total_points,
                "tba_rpEarned": tba_rp_earned,
                "autoReachPoints": auto_reach_points,
                "autoCrossingPoints": auto_crossing_points,
                "autoBoulderPoints": auto_boulder_points,
                "teleopCrossingPoints": teleop_crossing_points,
                "teleopBouldersLow": teleop_boulders_low,
                "teleopBouldersHigh": teleop_boulders_high,
                "teleopBoulderPoints": teleop_boulder_points,
                "teleopDefensesBreached": teleop_defenses_breached,
                "teleopChallengePoints": teleop_challenge_points,
                "teleopScalePoints": teleop_scale_points,
                "teleopTowerCaptured": teleop_tower_captured,
                "position2": position2,
                "position3": position3,
                "position4": position4,
                "position5": position5,
                "position1crossings": position1crossings,
                "position2crossings": position2crossings,
                "position3crossings": position3crossings,
                "position4crossings": position4crossings,
                "position5crossings": position5crossings,
            }
        )
        if teleop_points is not UNSET:
            field_dict["teleopPoints"] = teleop_points
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if robot_1_auto is not UNSET:
            field_dict["robot1Auto"] = robot_1_auto
        if robot_2_auto is not UNSET:
            field_dict["robot2Auto"] = robot_2_auto
        if robot_3_auto is not UNSET:
            field_dict["robot3Auto"] = robot_3_auto
        if auto_boulders_low is not UNSET:
            field_dict["autoBouldersLow"] = auto_boulders_low
        if auto_boulders_high is not UNSET:
            field_dict["autoBouldersHigh"] = auto_boulders_high
        if tower_face_a is not UNSET:
            field_dict["towerFaceA"] = tower_face_a
        if tower_face_b is not UNSET:
            field_dict["towerFaceB"] = tower_face_b
        if tower_face_c is not UNSET:
            field_dict["towerFaceC"] = tower_face_c
        if tower_end_strength is not UNSET:
            field_dict["towerEndStrength"] = tower_end_strength
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_points = d.pop("autoPoints")

        breach_points = d.pop("breachPoints")

        foul_points = d.pop("foulPoints")

        capture_points = d.pop("capturePoints")

        total_points = d.pop("totalPoints")

        def _parse_tba_rp_earned(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        tba_rp_earned = _parse_tba_rp_earned(d.pop("tba_rpEarned"))

        auto_reach_points = d.pop("autoReachPoints")

        auto_crossing_points = d.pop("autoCrossingPoints")

        auto_boulder_points = d.pop("autoBoulderPoints")

        teleop_crossing_points = d.pop("teleopCrossingPoints")

        teleop_boulders_low = d.pop("teleopBouldersLow")

        teleop_boulders_high = d.pop("teleopBouldersHigh")

        teleop_boulder_points = d.pop("teleopBoulderPoints")

        teleop_defenses_breached = d.pop("teleopDefensesBreached")

        teleop_challenge_points = d.pop("teleopChallengePoints")

        teleop_scale_points = d.pop("teleopScalePoints")

        teleop_tower_captured = d.pop("teleopTowerCaptured")

        position2 = Position2016(d.pop("position2"))

        position3 = Position2016(d.pop("position3"))

        position4 = Position2016(d.pop("position4"))

        position5 = Position2016(d.pop("position5"))

        position1crossings = d.pop("position1crossings")

        position2crossings = d.pop("position2crossings")

        position3crossings = d.pop("position3crossings")

        position4crossings = d.pop("position4crossings")

        position5crossings = d.pop("position5crossings")

        teleop_points = d.pop("teleopPoints", UNSET)

        adjust_points = d.pop("adjustPoints", UNSET)

        _robot_1_auto = d.pop("robot1Auto", UNSET)
        robot_1_auto: RobotAuto2016WithUnknown | Unset
        if isinstance(_robot_1_auto, Unset):
            robot_1_auto = UNSET
        else:
            robot_1_auto = RobotAuto2016WithUnknown(_robot_1_auto)

        _robot_2_auto = d.pop("robot2Auto", UNSET)
        robot_2_auto: RobotAuto2016WithoutUnknown | Unset
        if isinstance(_robot_2_auto, Unset):
            robot_2_auto = UNSET
        else:
            robot_2_auto = RobotAuto2016WithoutUnknown(_robot_2_auto)

        _robot_3_auto = d.pop("robot3Auto", UNSET)
        robot_3_auto: RobotAuto2016WithUnknown | Unset
        if isinstance(_robot_3_auto, Unset):
            robot_3_auto = UNSET
        else:
            robot_3_auto = RobotAuto2016WithUnknown(_robot_3_auto)

        auto_boulders_low = d.pop("autoBouldersLow", UNSET)

        auto_boulders_high = d.pop("autoBouldersHigh", UNSET)

        _tower_face_a = d.pop("towerFaceA", UNSET)
        tower_face_a: TowerFace2016 | Unset
        if isinstance(_tower_face_a, Unset):
            tower_face_a = UNSET
        else:
            tower_face_a = TowerFace2016(_tower_face_a)

        _tower_face_b = d.pop("towerFaceB", UNSET)
        tower_face_b: TowerFace2016 | Unset
        if isinstance(_tower_face_b, Unset):
            tower_face_b = UNSET
        else:
            tower_face_b = TowerFace2016(_tower_face_b)

        _tower_face_c = d.pop("towerFaceC", UNSET)
        tower_face_c: TowerFace2016 | Unset
        if isinstance(_tower_face_c, Unset):
            tower_face_c = UNSET
        else:
            tower_face_c = TowerFace2016(_tower_face_c)

        tower_end_strength = d.pop("towerEndStrength", UNSET)

        tech_foul_count = d.pop("techFoulCount", UNSET)

        foul_count = d.pop("foulCount", UNSET)

        match_score_breakdown_2016_alliance = cls(
            auto_points=auto_points,
            breach_points=breach_points,
            foul_points=foul_points,
            capture_points=capture_points,
            total_points=total_points,
            tba_rp_earned=tba_rp_earned,
            auto_reach_points=auto_reach_points,
            auto_crossing_points=auto_crossing_points,
            auto_boulder_points=auto_boulder_points,
            teleop_crossing_points=teleop_crossing_points,
            teleop_boulders_low=teleop_boulders_low,
            teleop_boulders_high=teleop_boulders_high,
            teleop_boulder_points=teleop_boulder_points,
            teleop_defenses_breached=teleop_defenses_breached,
            teleop_challenge_points=teleop_challenge_points,
            teleop_scale_points=teleop_scale_points,
            teleop_tower_captured=teleop_tower_captured,
            position2=position2,
            position3=position3,
            position4=position4,
            position5=position5,
            position1crossings=position1crossings,
            position2crossings=position2crossings,
            position3crossings=position3crossings,
            position4crossings=position4crossings,
            position5crossings=position5crossings,
            teleop_points=teleop_points,
            adjust_points=adjust_points,
            robot_1_auto=robot_1_auto,
            robot_2_auto=robot_2_auto,
            robot_3_auto=robot_3_auto,
            auto_boulders_low=auto_boulders_low,
            auto_boulders_high=auto_boulders_high,
            tower_face_a=tower_face_a,
            tower_face_b=tower_face_b,
            tower_face_c=tower_face_c,
            tower_end_strength=tower_end_strength,
            tech_foul_count=tech_foul_count,
            foul_count=foul_count,
        )

        match_score_breakdown_2016_alliance.additional_properties = d
        return match_score_breakdown_2016_alliance

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
