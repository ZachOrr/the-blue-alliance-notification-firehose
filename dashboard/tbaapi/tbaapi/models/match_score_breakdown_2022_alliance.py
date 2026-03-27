from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.endgame_robot_2022 import EndgameRobot2022
from ..models.taxi_robot_2022 import TaxiRobot2022
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2022Alliance")


@_attrs_define
class MatchScoreBreakdown2022Alliance:
    """
    Attributes:
        taxi_robot_1 (TaxiRobot2022 | Unset):
        endgame_robot_1 (EndgameRobot2022 | Unset):
        taxi_robot_2 (TaxiRobot2022 | Unset):
        endgame_robot_2 (EndgameRobot2022 | Unset):
        taxi_robot_3 (TaxiRobot2022 | Unset):
        endgame_robot_3 (EndgameRobot2022 | Unset):
        auto_cargo_lower_near (int | Unset):
        auto_cargo_lower_far (int | Unset):
        auto_cargo_lower_blue (int | Unset):
        auto_cargo_lower_red (int | Unset):
        auto_cargo_upper_near (int | Unset):
        auto_cargo_upper_far (int | Unset):
        auto_cargo_upper_blue (int | Unset):
        auto_cargo_upper_red (int | Unset):
        auto_cargo_total (int | Unset):
        teleop_cargo_lower_near (int | Unset):
        teleop_cargo_lower_far (int | Unset):
        teleop_cargo_lower_blue (int | Unset):
        teleop_cargo_lower_red (int | Unset):
        teleop_cargo_upper_near (int | Unset):
        teleop_cargo_upper_far (int | Unset):
        teleop_cargo_upper_blue (int | Unset):
        teleop_cargo_upper_red (int | Unset):
        teleop_cargo_total (int | Unset):
        match_cargo_total (int | Unset):
        auto_taxi_points (int | Unset):
        auto_cargo_points (int | Unset):
        auto_points (int | Unset):
        quintet_achieved (bool | Unset):
        teleop_cargo_points (int | Unset):
        endgame_points (int | Unset):
        teleop_points (int | Unset):
        cargo_bonus_ranking_point (bool | Unset):
        hangar_bonus_ranking_point (bool | Unset):
        foul_count (int | Unset):
        tech_foul_count (int | Unset):
        adjust_points (int | Unset):
        foul_points (int | Unset):
        rp (int | None | Unset):
        total_points (int | Unset):
    """

    taxi_robot_1: TaxiRobot2022 | Unset = UNSET
    endgame_robot_1: EndgameRobot2022 | Unset = UNSET
    taxi_robot_2: TaxiRobot2022 | Unset = UNSET
    endgame_robot_2: EndgameRobot2022 | Unset = UNSET
    taxi_robot_3: TaxiRobot2022 | Unset = UNSET
    endgame_robot_3: EndgameRobot2022 | Unset = UNSET
    auto_cargo_lower_near: int | Unset = UNSET
    auto_cargo_lower_far: int | Unset = UNSET
    auto_cargo_lower_blue: int | Unset = UNSET
    auto_cargo_lower_red: int | Unset = UNSET
    auto_cargo_upper_near: int | Unset = UNSET
    auto_cargo_upper_far: int | Unset = UNSET
    auto_cargo_upper_blue: int | Unset = UNSET
    auto_cargo_upper_red: int | Unset = UNSET
    auto_cargo_total: int | Unset = UNSET
    teleop_cargo_lower_near: int | Unset = UNSET
    teleop_cargo_lower_far: int | Unset = UNSET
    teleop_cargo_lower_blue: int | Unset = UNSET
    teleop_cargo_lower_red: int | Unset = UNSET
    teleop_cargo_upper_near: int | Unset = UNSET
    teleop_cargo_upper_far: int | Unset = UNSET
    teleop_cargo_upper_blue: int | Unset = UNSET
    teleop_cargo_upper_red: int | Unset = UNSET
    teleop_cargo_total: int | Unset = UNSET
    match_cargo_total: int | Unset = UNSET
    auto_taxi_points: int | Unset = UNSET
    auto_cargo_points: int | Unset = UNSET
    auto_points: int | Unset = UNSET
    quintet_achieved: bool | Unset = UNSET
    teleop_cargo_points: int | Unset = UNSET
    endgame_points: int | Unset = UNSET
    teleop_points: int | Unset = UNSET
    cargo_bonus_ranking_point: bool | Unset = UNSET
    hangar_bonus_ranking_point: bool | Unset = UNSET
    foul_count: int | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    adjust_points: int | Unset = UNSET
    foul_points: int | Unset = UNSET
    rp: int | None | Unset = UNSET
    total_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxi_robot_1: str | Unset = UNSET
        if not isinstance(self.taxi_robot_1, Unset):
            taxi_robot_1 = self.taxi_robot_1.value

        endgame_robot_1: str | Unset = UNSET
        if not isinstance(self.endgame_robot_1, Unset):
            endgame_robot_1 = self.endgame_robot_1.value

        taxi_robot_2: str | Unset = UNSET
        if not isinstance(self.taxi_robot_2, Unset):
            taxi_robot_2 = self.taxi_robot_2.value

        endgame_robot_2: str | Unset = UNSET
        if not isinstance(self.endgame_robot_2, Unset):
            endgame_robot_2 = self.endgame_robot_2.value

        taxi_robot_3: str | Unset = UNSET
        if not isinstance(self.taxi_robot_3, Unset):
            taxi_robot_3 = self.taxi_robot_3.value

        endgame_robot_3: str | Unset = UNSET
        if not isinstance(self.endgame_robot_3, Unset):
            endgame_robot_3 = self.endgame_robot_3.value

        auto_cargo_lower_near = self.auto_cargo_lower_near

        auto_cargo_lower_far = self.auto_cargo_lower_far

        auto_cargo_lower_blue = self.auto_cargo_lower_blue

        auto_cargo_lower_red = self.auto_cargo_lower_red

        auto_cargo_upper_near = self.auto_cargo_upper_near

        auto_cargo_upper_far = self.auto_cargo_upper_far

        auto_cargo_upper_blue = self.auto_cargo_upper_blue

        auto_cargo_upper_red = self.auto_cargo_upper_red

        auto_cargo_total = self.auto_cargo_total

        teleop_cargo_lower_near = self.teleop_cargo_lower_near

        teleop_cargo_lower_far = self.teleop_cargo_lower_far

        teleop_cargo_lower_blue = self.teleop_cargo_lower_blue

        teleop_cargo_lower_red = self.teleop_cargo_lower_red

        teleop_cargo_upper_near = self.teleop_cargo_upper_near

        teleop_cargo_upper_far = self.teleop_cargo_upper_far

        teleop_cargo_upper_blue = self.teleop_cargo_upper_blue

        teleop_cargo_upper_red = self.teleop_cargo_upper_red

        teleop_cargo_total = self.teleop_cargo_total

        match_cargo_total = self.match_cargo_total

        auto_taxi_points = self.auto_taxi_points

        auto_cargo_points = self.auto_cargo_points

        auto_points = self.auto_points

        quintet_achieved = self.quintet_achieved

        teleop_cargo_points = self.teleop_cargo_points

        endgame_points = self.endgame_points

        teleop_points = self.teleop_points

        cargo_bonus_ranking_point = self.cargo_bonus_ranking_point

        hangar_bonus_ranking_point = self.hangar_bonus_ranking_point

        foul_count = self.foul_count

        tech_foul_count = self.tech_foul_count

        adjust_points = self.adjust_points

        foul_points = self.foul_points

        rp: int | None | Unset
        if isinstance(self.rp, Unset):
            rp = UNSET
        else:
            rp = self.rp

        total_points = self.total_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxi_robot_1 is not UNSET:
            field_dict["taxiRobot1"] = taxi_robot_1
        if endgame_robot_1 is not UNSET:
            field_dict["endgameRobot1"] = endgame_robot_1
        if taxi_robot_2 is not UNSET:
            field_dict["taxiRobot2"] = taxi_robot_2
        if endgame_robot_2 is not UNSET:
            field_dict["endgameRobot2"] = endgame_robot_2
        if taxi_robot_3 is not UNSET:
            field_dict["taxiRobot3"] = taxi_robot_3
        if endgame_robot_3 is not UNSET:
            field_dict["endgameRobot3"] = endgame_robot_3
        if auto_cargo_lower_near is not UNSET:
            field_dict["autoCargoLowerNear"] = auto_cargo_lower_near
        if auto_cargo_lower_far is not UNSET:
            field_dict["autoCargoLowerFar"] = auto_cargo_lower_far
        if auto_cargo_lower_blue is not UNSET:
            field_dict["autoCargoLowerBlue"] = auto_cargo_lower_blue
        if auto_cargo_lower_red is not UNSET:
            field_dict["autoCargoLowerRed"] = auto_cargo_lower_red
        if auto_cargo_upper_near is not UNSET:
            field_dict["autoCargoUpperNear"] = auto_cargo_upper_near
        if auto_cargo_upper_far is not UNSET:
            field_dict["autoCargoUpperFar"] = auto_cargo_upper_far
        if auto_cargo_upper_blue is not UNSET:
            field_dict["autoCargoUpperBlue"] = auto_cargo_upper_blue
        if auto_cargo_upper_red is not UNSET:
            field_dict["autoCargoUpperRed"] = auto_cargo_upper_red
        if auto_cargo_total is not UNSET:
            field_dict["autoCargoTotal"] = auto_cargo_total
        if teleop_cargo_lower_near is not UNSET:
            field_dict["teleopCargoLowerNear"] = teleop_cargo_lower_near
        if teleop_cargo_lower_far is not UNSET:
            field_dict["teleopCargoLowerFar"] = teleop_cargo_lower_far
        if teleop_cargo_lower_blue is not UNSET:
            field_dict["teleopCargoLowerBlue"] = teleop_cargo_lower_blue
        if teleop_cargo_lower_red is not UNSET:
            field_dict["teleopCargoLowerRed"] = teleop_cargo_lower_red
        if teleop_cargo_upper_near is not UNSET:
            field_dict["teleopCargoUpperNear"] = teleop_cargo_upper_near
        if teleop_cargo_upper_far is not UNSET:
            field_dict["teleopCargoUpperFar"] = teleop_cargo_upper_far
        if teleop_cargo_upper_blue is not UNSET:
            field_dict["teleopCargoUpperBlue"] = teleop_cargo_upper_blue
        if teleop_cargo_upper_red is not UNSET:
            field_dict["teleopCargoUpperRed"] = teleop_cargo_upper_red
        if teleop_cargo_total is not UNSET:
            field_dict["teleopCargoTotal"] = teleop_cargo_total
        if match_cargo_total is not UNSET:
            field_dict["matchCargoTotal"] = match_cargo_total
        if auto_taxi_points is not UNSET:
            field_dict["autoTaxiPoints"] = auto_taxi_points
        if auto_cargo_points is not UNSET:
            field_dict["autoCargoPoints"] = auto_cargo_points
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if quintet_achieved is not UNSET:
            field_dict["quintetAchieved"] = quintet_achieved
        if teleop_cargo_points is not UNSET:
            field_dict["teleopCargoPoints"] = teleop_cargo_points
        if endgame_points is not UNSET:
            field_dict["endgamePoints"] = endgame_points
        if teleop_points is not UNSET:
            field_dict["teleopPoints"] = teleop_points
        if cargo_bonus_ranking_point is not UNSET:
            field_dict["cargoBonusRankingPoint"] = cargo_bonus_ranking_point
        if hangar_bonus_ranking_point is not UNSET:
            field_dict["hangarBonusRankingPoint"] = hangar_bonus_ranking_point
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if foul_points is not UNSET:
            field_dict["foulPoints"] = foul_points
        if rp is not UNSET:
            field_dict["rp"] = rp
        if total_points is not UNSET:
            field_dict["totalPoints"] = total_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _taxi_robot_1 = d.pop("taxiRobot1", UNSET)
        taxi_robot_1: TaxiRobot2022 | Unset
        if isinstance(_taxi_robot_1, Unset):
            taxi_robot_1 = UNSET
        else:
            taxi_robot_1 = TaxiRobot2022(_taxi_robot_1)

        _endgame_robot_1 = d.pop("endgameRobot1", UNSET)
        endgame_robot_1: EndgameRobot2022 | Unset
        if isinstance(_endgame_robot_1, Unset):
            endgame_robot_1 = UNSET
        else:
            endgame_robot_1 = EndgameRobot2022(_endgame_robot_1)

        _taxi_robot_2 = d.pop("taxiRobot2", UNSET)
        taxi_robot_2: TaxiRobot2022 | Unset
        if isinstance(_taxi_robot_2, Unset):
            taxi_robot_2 = UNSET
        else:
            taxi_robot_2 = TaxiRobot2022(_taxi_robot_2)

        _endgame_robot_2 = d.pop("endgameRobot2", UNSET)
        endgame_robot_2: EndgameRobot2022 | Unset
        if isinstance(_endgame_robot_2, Unset):
            endgame_robot_2 = UNSET
        else:
            endgame_robot_2 = EndgameRobot2022(_endgame_robot_2)

        _taxi_robot_3 = d.pop("taxiRobot3", UNSET)
        taxi_robot_3: TaxiRobot2022 | Unset
        if isinstance(_taxi_robot_3, Unset):
            taxi_robot_3 = UNSET
        else:
            taxi_robot_3 = TaxiRobot2022(_taxi_robot_3)

        _endgame_robot_3 = d.pop("endgameRobot3", UNSET)
        endgame_robot_3: EndgameRobot2022 | Unset
        if isinstance(_endgame_robot_3, Unset):
            endgame_robot_3 = UNSET
        else:
            endgame_robot_3 = EndgameRobot2022(_endgame_robot_3)

        auto_cargo_lower_near = d.pop("autoCargoLowerNear", UNSET)

        auto_cargo_lower_far = d.pop("autoCargoLowerFar", UNSET)

        auto_cargo_lower_blue = d.pop("autoCargoLowerBlue", UNSET)

        auto_cargo_lower_red = d.pop("autoCargoLowerRed", UNSET)

        auto_cargo_upper_near = d.pop("autoCargoUpperNear", UNSET)

        auto_cargo_upper_far = d.pop("autoCargoUpperFar", UNSET)

        auto_cargo_upper_blue = d.pop("autoCargoUpperBlue", UNSET)

        auto_cargo_upper_red = d.pop("autoCargoUpperRed", UNSET)

        auto_cargo_total = d.pop("autoCargoTotal", UNSET)

        teleop_cargo_lower_near = d.pop("teleopCargoLowerNear", UNSET)

        teleop_cargo_lower_far = d.pop("teleopCargoLowerFar", UNSET)

        teleop_cargo_lower_blue = d.pop("teleopCargoLowerBlue", UNSET)

        teleop_cargo_lower_red = d.pop("teleopCargoLowerRed", UNSET)

        teleop_cargo_upper_near = d.pop("teleopCargoUpperNear", UNSET)

        teleop_cargo_upper_far = d.pop("teleopCargoUpperFar", UNSET)

        teleop_cargo_upper_blue = d.pop("teleopCargoUpperBlue", UNSET)

        teleop_cargo_upper_red = d.pop("teleopCargoUpperRed", UNSET)

        teleop_cargo_total = d.pop("teleopCargoTotal", UNSET)

        match_cargo_total = d.pop("matchCargoTotal", UNSET)

        auto_taxi_points = d.pop("autoTaxiPoints", UNSET)

        auto_cargo_points = d.pop("autoCargoPoints", UNSET)

        auto_points = d.pop("autoPoints", UNSET)

        quintet_achieved = d.pop("quintetAchieved", UNSET)

        teleop_cargo_points = d.pop("teleopCargoPoints", UNSET)

        endgame_points = d.pop("endgamePoints", UNSET)

        teleop_points = d.pop("teleopPoints", UNSET)

        cargo_bonus_ranking_point = d.pop("cargoBonusRankingPoint", UNSET)

        hangar_bonus_ranking_point = d.pop("hangarBonusRankingPoint", UNSET)

        foul_count = d.pop("foulCount", UNSET)

        tech_foul_count = d.pop("techFoulCount", UNSET)

        adjust_points = d.pop("adjustPoints", UNSET)

        foul_points = d.pop("foulPoints", UNSET)

        def _parse_rp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rp = _parse_rp(d.pop("rp", UNSET))

        total_points = d.pop("totalPoints", UNSET)

        match_score_breakdown_2022_alliance = cls(
            taxi_robot_1=taxi_robot_1,
            endgame_robot_1=endgame_robot_1,
            taxi_robot_2=taxi_robot_2,
            endgame_robot_2=endgame_robot_2,
            taxi_robot_3=taxi_robot_3,
            endgame_robot_3=endgame_robot_3,
            auto_cargo_lower_near=auto_cargo_lower_near,
            auto_cargo_lower_far=auto_cargo_lower_far,
            auto_cargo_lower_blue=auto_cargo_lower_blue,
            auto_cargo_lower_red=auto_cargo_lower_red,
            auto_cargo_upper_near=auto_cargo_upper_near,
            auto_cargo_upper_far=auto_cargo_upper_far,
            auto_cargo_upper_blue=auto_cargo_upper_blue,
            auto_cargo_upper_red=auto_cargo_upper_red,
            auto_cargo_total=auto_cargo_total,
            teleop_cargo_lower_near=teleop_cargo_lower_near,
            teleop_cargo_lower_far=teleop_cargo_lower_far,
            teleop_cargo_lower_blue=teleop_cargo_lower_blue,
            teleop_cargo_lower_red=teleop_cargo_lower_red,
            teleop_cargo_upper_near=teleop_cargo_upper_near,
            teleop_cargo_upper_far=teleop_cargo_upper_far,
            teleop_cargo_upper_blue=teleop_cargo_upper_blue,
            teleop_cargo_upper_red=teleop_cargo_upper_red,
            teleop_cargo_total=teleop_cargo_total,
            match_cargo_total=match_cargo_total,
            auto_taxi_points=auto_taxi_points,
            auto_cargo_points=auto_cargo_points,
            auto_points=auto_points,
            quintet_achieved=quintet_achieved,
            teleop_cargo_points=teleop_cargo_points,
            endgame_points=endgame_points,
            teleop_points=teleop_points,
            cargo_bonus_ranking_point=cargo_bonus_ranking_point,
            hangar_bonus_ranking_point=hangar_bonus_ranking_point,
            foul_count=foul_count,
            tech_foul_count=tech_foul_count,
            adjust_points=adjust_points,
            foul_points=foul_points,
            rp=rp,
            total_points=total_points,
        )

        match_score_breakdown_2022_alliance.additional_properties = d
        return match_score_breakdown_2022_alliance

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
