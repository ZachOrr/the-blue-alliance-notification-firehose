from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.robot_auto_2017 import RobotAuto2017
from ..models.touchpad_2017 import Touchpad2017
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2017Alliance")


@_attrs_define
class MatchScoreBreakdown2017Alliance:
    """
    Attributes:
        auto_points (int):
        teleop_points (int):
        foul_points (int):
        total_points (int):
        rotor_1_auto (bool):
        rotor_2_auto (bool):
        auto_fuel_low (int):
        auto_fuel_high (int):
        auto_mobility_points (int):
        auto_rotor_points (int):
        auto_fuel_points (int):
        teleop_fuel_points (int):
        teleop_fuel_low (int):
        teleop_fuel_high (int):
        teleop_rotor_points (int):
        k_pa_ranking_point_achieved (bool):
        teleop_takeoff_points (int):
        k_pa_bonus_points (int):
        rotor_bonus_points (int):
        rotor_1_engaged (bool):
        rotor_2_engaged (bool):
        rotor_3_engaged (bool):
        rotor_4_engaged (bool):
        rotor_ranking_point_achieved (bool):
        adjust_points (int | Unset):
        robot_1_auto (RobotAuto2017 | Unset):
        robot_2_auto (RobotAuto2017 | Unset):
        robot_3_auto (RobotAuto2017 | Unset):
        tba_rp_earned (int | None | Unset):
        tech_foul_count (int | Unset):
        foul_count (int | Unset):
        touchpad_near (Touchpad2017 | Unset):
        touchpad_middle (Touchpad2017 | Unset):
        touchpad_far (Touchpad2017 | Unset):
    """

    auto_points: int
    teleop_points: int
    foul_points: int
    total_points: int
    rotor_1_auto: bool
    rotor_2_auto: bool
    auto_fuel_low: int
    auto_fuel_high: int
    auto_mobility_points: int
    auto_rotor_points: int
    auto_fuel_points: int
    teleop_fuel_points: int
    teleop_fuel_low: int
    teleop_fuel_high: int
    teleop_rotor_points: int
    k_pa_ranking_point_achieved: bool
    teleop_takeoff_points: int
    k_pa_bonus_points: int
    rotor_bonus_points: int
    rotor_1_engaged: bool
    rotor_2_engaged: bool
    rotor_3_engaged: bool
    rotor_4_engaged: bool
    rotor_ranking_point_achieved: bool
    adjust_points: int | Unset = UNSET
    robot_1_auto: RobotAuto2017 | Unset = UNSET
    robot_2_auto: RobotAuto2017 | Unset = UNSET
    robot_3_auto: RobotAuto2017 | Unset = UNSET
    tba_rp_earned: int | None | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    foul_count: int | Unset = UNSET
    touchpad_near: Touchpad2017 | Unset = UNSET
    touchpad_middle: Touchpad2017 | Unset = UNSET
    touchpad_far: Touchpad2017 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_points = self.auto_points

        teleop_points = self.teleop_points

        foul_points = self.foul_points

        total_points = self.total_points

        rotor_1_auto = self.rotor_1_auto

        rotor_2_auto = self.rotor_2_auto

        auto_fuel_low = self.auto_fuel_low

        auto_fuel_high = self.auto_fuel_high

        auto_mobility_points = self.auto_mobility_points

        auto_rotor_points = self.auto_rotor_points

        auto_fuel_points = self.auto_fuel_points

        teleop_fuel_points = self.teleop_fuel_points

        teleop_fuel_low = self.teleop_fuel_low

        teleop_fuel_high = self.teleop_fuel_high

        teleop_rotor_points = self.teleop_rotor_points

        k_pa_ranking_point_achieved = self.k_pa_ranking_point_achieved

        teleop_takeoff_points = self.teleop_takeoff_points

        k_pa_bonus_points = self.k_pa_bonus_points

        rotor_bonus_points = self.rotor_bonus_points

        rotor_1_engaged = self.rotor_1_engaged

        rotor_2_engaged = self.rotor_2_engaged

        rotor_3_engaged = self.rotor_3_engaged

        rotor_4_engaged = self.rotor_4_engaged

        rotor_ranking_point_achieved = self.rotor_ranking_point_achieved

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

        tba_rp_earned: int | None | Unset
        if isinstance(self.tba_rp_earned, Unset):
            tba_rp_earned = UNSET
        else:
            tba_rp_earned = self.tba_rp_earned

        tech_foul_count = self.tech_foul_count

        foul_count = self.foul_count

        touchpad_near: str | Unset = UNSET
        if not isinstance(self.touchpad_near, Unset):
            touchpad_near = self.touchpad_near.value

        touchpad_middle: str | Unset = UNSET
        if not isinstance(self.touchpad_middle, Unset):
            touchpad_middle = self.touchpad_middle.value

        touchpad_far: str | Unset = UNSET
        if not isinstance(self.touchpad_far, Unset):
            touchpad_far = self.touchpad_far.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoPoints": auto_points,
                "teleopPoints": teleop_points,
                "foulPoints": foul_points,
                "totalPoints": total_points,
                "rotor1Auto": rotor_1_auto,
                "rotor2Auto": rotor_2_auto,
                "autoFuelLow": auto_fuel_low,
                "autoFuelHigh": auto_fuel_high,
                "autoMobilityPoints": auto_mobility_points,
                "autoRotorPoints": auto_rotor_points,
                "autoFuelPoints": auto_fuel_points,
                "teleopFuelPoints": teleop_fuel_points,
                "teleopFuelLow": teleop_fuel_low,
                "teleopFuelHigh": teleop_fuel_high,
                "teleopRotorPoints": teleop_rotor_points,
                "kPaRankingPointAchieved": k_pa_ranking_point_achieved,
                "teleopTakeoffPoints": teleop_takeoff_points,
                "kPaBonusPoints": k_pa_bonus_points,
                "rotorBonusPoints": rotor_bonus_points,
                "rotor1Engaged": rotor_1_engaged,
                "rotor2Engaged": rotor_2_engaged,
                "rotor3Engaged": rotor_3_engaged,
                "rotor4Engaged": rotor_4_engaged,
                "rotorRankingPointAchieved": rotor_ranking_point_achieved,
            }
        )
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if robot_1_auto is not UNSET:
            field_dict["robot1Auto"] = robot_1_auto
        if robot_2_auto is not UNSET:
            field_dict["robot2Auto"] = robot_2_auto
        if robot_3_auto is not UNSET:
            field_dict["robot3Auto"] = robot_3_auto
        if tba_rp_earned is not UNSET:
            field_dict["tba_rpEarned"] = tba_rp_earned
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count
        if touchpad_near is not UNSET:
            field_dict["touchpadNear"] = touchpad_near
        if touchpad_middle is not UNSET:
            field_dict["touchpadMiddle"] = touchpad_middle
        if touchpad_far is not UNSET:
            field_dict["touchpadFar"] = touchpad_far

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_points = d.pop("autoPoints")

        teleop_points = d.pop("teleopPoints")

        foul_points = d.pop("foulPoints")

        total_points = d.pop("totalPoints")

        rotor_1_auto = d.pop("rotor1Auto")

        rotor_2_auto = d.pop("rotor2Auto")

        auto_fuel_low = d.pop("autoFuelLow")

        auto_fuel_high = d.pop("autoFuelHigh")

        auto_mobility_points = d.pop("autoMobilityPoints")

        auto_rotor_points = d.pop("autoRotorPoints")

        auto_fuel_points = d.pop("autoFuelPoints")

        teleop_fuel_points = d.pop("teleopFuelPoints")

        teleop_fuel_low = d.pop("teleopFuelLow")

        teleop_fuel_high = d.pop("teleopFuelHigh")

        teleop_rotor_points = d.pop("teleopRotorPoints")

        k_pa_ranking_point_achieved = d.pop("kPaRankingPointAchieved")

        teleop_takeoff_points = d.pop("teleopTakeoffPoints")

        k_pa_bonus_points = d.pop("kPaBonusPoints")

        rotor_bonus_points = d.pop("rotorBonusPoints")

        rotor_1_engaged = d.pop("rotor1Engaged")

        rotor_2_engaged = d.pop("rotor2Engaged")

        rotor_3_engaged = d.pop("rotor3Engaged")

        rotor_4_engaged = d.pop("rotor4Engaged")

        rotor_ranking_point_achieved = d.pop("rotorRankingPointAchieved")

        adjust_points = d.pop("adjustPoints", UNSET)

        _robot_1_auto = d.pop("robot1Auto", UNSET)
        robot_1_auto: RobotAuto2017 | Unset
        if isinstance(_robot_1_auto, Unset):
            robot_1_auto = UNSET
        else:
            robot_1_auto = RobotAuto2017(_robot_1_auto)

        _robot_2_auto = d.pop("robot2Auto", UNSET)
        robot_2_auto: RobotAuto2017 | Unset
        if isinstance(_robot_2_auto, Unset):
            robot_2_auto = UNSET
        else:
            robot_2_auto = RobotAuto2017(_robot_2_auto)

        _robot_3_auto = d.pop("robot3Auto", UNSET)
        robot_3_auto: RobotAuto2017 | Unset
        if isinstance(_robot_3_auto, Unset):
            robot_3_auto = UNSET
        else:
            robot_3_auto = RobotAuto2017(_robot_3_auto)

        def _parse_tba_rp_earned(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tba_rp_earned = _parse_tba_rp_earned(d.pop("tba_rpEarned", UNSET))

        tech_foul_count = d.pop("techFoulCount", UNSET)

        foul_count = d.pop("foulCount", UNSET)

        _touchpad_near = d.pop("touchpadNear", UNSET)
        touchpad_near: Touchpad2017 | Unset
        if isinstance(_touchpad_near, Unset):
            touchpad_near = UNSET
        else:
            touchpad_near = Touchpad2017(_touchpad_near)

        _touchpad_middle = d.pop("touchpadMiddle", UNSET)
        touchpad_middle: Touchpad2017 | Unset
        if isinstance(_touchpad_middle, Unset):
            touchpad_middle = UNSET
        else:
            touchpad_middle = Touchpad2017(_touchpad_middle)

        _touchpad_far = d.pop("touchpadFar", UNSET)
        touchpad_far: Touchpad2017 | Unset
        if isinstance(_touchpad_far, Unset):
            touchpad_far = UNSET
        else:
            touchpad_far = Touchpad2017(_touchpad_far)

        match_score_breakdown_2017_alliance = cls(
            auto_points=auto_points,
            teleop_points=teleop_points,
            foul_points=foul_points,
            total_points=total_points,
            rotor_1_auto=rotor_1_auto,
            rotor_2_auto=rotor_2_auto,
            auto_fuel_low=auto_fuel_low,
            auto_fuel_high=auto_fuel_high,
            auto_mobility_points=auto_mobility_points,
            auto_rotor_points=auto_rotor_points,
            auto_fuel_points=auto_fuel_points,
            teleop_fuel_points=teleop_fuel_points,
            teleop_fuel_low=teleop_fuel_low,
            teleop_fuel_high=teleop_fuel_high,
            teleop_rotor_points=teleop_rotor_points,
            k_pa_ranking_point_achieved=k_pa_ranking_point_achieved,
            teleop_takeoff_points=teleop_takeoff_points,
            k_pa_bonus_points=k_pa_bonus_points,
            rotor_bonus_points=rotor_bonus_points,
            rotor_1_engaged=rotor_1_engaged,
            rotor_2_engaged=rotor_2_engaged,
            rotor_3_engaged=rotor_3_engaged,
            rotor_4_engaged=rotor_4_engaged,
            rotor_ranking_point_achieved=rotor_ranking_point_achieved,
            adjust_points=adjust_points,
            robot_1_auto=robot_1_auto,
            robot_2_auto=robot_2_auto,
            robot_3_auto=robot_3_auto,
            tba_rp_earned=tba_rp_earned,
            tech_foul_count=tech_foul_count,
            foul_count=foul_count,
            touchpad_near=touchpad_near,
            touchpad_middle=touchpad_middle,
            touchpad_far=touchpad_far,
        )

        match_score_breakdown_2017_alliance.additional_properties = d
        return match_score_breakdown_2017_alliance

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
