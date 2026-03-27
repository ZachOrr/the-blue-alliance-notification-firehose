from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventInsights2017")


@_attrs_define
class EventInsights2017:
    """Insights for FIRST STEAMWORKS qualification and elimination matches.

    Attributes:
        average_foul_score (float): Average foul score.
        average_fuel_points (float): Average fuel points scored.
        average_fuel_points_auto (float): Average fuel points scored during auto.
        average_fuel_points_teleop (float): Average fuel points scored during teleop.
        average_high_goals (float): Average points scored in the high goal.
        average_high_goals_auto (float): Average points scored in the high goal during auto.
        average_high_goals_teleop (float): Average points scored in the high goal during teleop.
        average_low_goals (float): Average points scored in the low goal.
        average_low_goals_auto (float): Average points scored in the low goal during auto.
        average_low_goals_teleop (float): Average points scored in the low goal during teleop.
        average_mobility_points_auto (float): Average mobility points scored during auto.
        average_points_auto (float): Average points scored during auto.
        average_points_teleop (float): Average points scored during teleop.
        average_rotor_points (float): Average rotor points scored.
        average_rotor_points_auto (float): Average rotor points scored during auto.
        average_rotor_points_teleop (float): Average rotor points scored during teleop.
        average_score (float): Average score.
        average_takeoff_points_teleop (float): Average takeoff points scored during teleop.
        average_win_margin (float): Average margin of victory.
        average_win_score (float): Average winning score.
        high_kpa (list[str]): An array with three values, kPa scored, match key from the match with the high kPa, and
            the name of the match
        high_score (list[str]): An array with three values, high score, match key from the match with the high score,
            and the name of the match
        kpa_achieved (list[float]): An array with three values, number of times kPa bonus achieved, number of
            opportunities to bonus, and percentage.
        mobility_counts (list[float]): An array with three values, number of times mobility bonus achieved, number of
            opportunities to bonus, and percentage.
        rotor_1_engaged (list[float]): An array with three values, number of times rotor 1 engaged, number of
            opportunities to engage, and percentage.
        rotor_1_engaged_auto (list[float]): An array with three values, number of times rotor 1 engaged in auto, number
            of opportunities to engage in auto, and percentage.
        rotor_2_engaged (list[float]): An array with three values, number of times rotor 2 engaged, number of
            opportunities to engage, and percentage.
        rotor_2_engaged_auto (list[float]): An array with three values, number of times rotor 2 engaged in auto, number
            of opportunities to engage in auto, and percentage.
        rotor_3_engaged (list[float]): An array with three values, number of times rotor 3 engaged, number of
            opportunities to engage, and percentage.
        rotor_4_engaged (list[float]): An array with three values, number of times rotor 4 engaged, number of
            opportunities to engage, and percentage.
        takeoff_counts (list[float]): An array with three values, number of times takeoff was counted, number of
            opportunities to takeoff, and percentage.
        unicorn_matches (list[float]): An array with three values, number of times a unicorn match (Win + kPa & Rotor
            Bonuses) occured, number of opportunities to have a unicorn match, and percentage.
    """

    average_foul_score: float
    average_fuel_points: float
    average_fuel_points_auto: float
    average_fuel_points_teleop: float
    average_high_goals: float
    average_high_goals_auto: float
    average_high_goals_teleop: float
    average_low_goals: float
    average_low_goals_auto: float
    average_low_goals_teleop: float
    average_mobility_points_auto: float
    average_points_auto: float
    average_points_teleop: float
    average_rotor_points: float
    average_rotor_points_auto: float
    average_rotor_points_teleop: float
    average_score: float
    average_takeoff_points_teleop: float
    average_win_margin: float
    average_win_score: float
    high_kpa: list[str]
    high_score: list[str]
    kpa_achieved: list[float]
    mobility_counts: list[float]
    rotor_1_engaged: list[float]
    rotor_1_engaged_auto: list[float]
    rotor_2_engaged: list[float]
    rotor_2_engaged_auto: list[float]
    rotor_3_engaged: list[float]
    rotor_4_engaged: list[float]
    takeoff_counts: list[float]
    unicorn_matches: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average_foul_score = self.average_foul_score

        average_fuel_points = self.average_fuel_points

        average_fuel_points_auto = self.average_fuel_points_auto

        average_fuel_points_teleop = self.average_fuel_points_teleop

        average_high_goals = self.average_high_goals

        average_high_goals_auto = self.average_high_goals_auto

        average_high_goals_teleop = self.average_high_goals_teleop

        average_low_goals = self.average_low_goals

        average_low_goals_auto = self.average_low_goals_auto

        average_low_goals_teleop = self.average_low_goals_teleop

        average_mobility_points_auto = self.average_mobility_points_auto

        average_points_auto = self.average_points_auto

        average_points_teleop = self.average_points_teleop

        average_rotor_points = self.average_rotor_points

        average_rotor_points_auto = self.average_rotor_points_auto

        average_rotor_points_teleop = self.average_rotor_points_teleop

        average_score = self.average_score

        average_takeoff_points_teleop = self.average_takeoff_points_teleop

        average_win_margin = self.average_win_margin

        average_win_score = self.average_win_score

        high_kpa = self.high_kpa

        high_score = self.high_score

        kpa_achieved = self.kpa_achieved

        mobility_counts = self.mobility_counts

        rotor_1_engaged = self.rotor_1_engaged

        rotor_1_engaged_auto = self.rotor_1_engaged_auto

        rotor_2_engaged = self.rotor_2_engaged

        rotor_2_engaged_auto = self.rotor_2_engaged_auto

        rotor_3_engaged = self.rotor_3_engaged

        rotor_4_engaged = self.rotor_4_engaged

        takeoff_counts = self.takeoff_counts

        unicorn_matches = self.unicorn_matches

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "average_foul_score": average_foul_score,
                "average_fuel_points": average_fuel_points,
                "average_fuel_points_auto": average_fuel_points_auto,
                "average_fuel_points_teleop": average_fuel_points_teleop,
                "average_high_goals": average_high_goals,
                "average_high_goals_auto": average_high_goals_auto,
                "average_high_goals_teleop": average_high_goals_teleop,
                "average_low_goals": average_low_goals,
                "average_low_goals_auto": average_low_goals_auto,
                "average_low_goals_teleop": average_low_goals_teleop,
                "average_mobility_points_auto": average_mobility_points_auto,
                "average_points_auto": average_points_auto,
                "average_points_teleop": average_points_teleop,
                "average_rotor_points": average_rotor_points,
                "average_rotor_points_auto": average_rotor_points_auto,
                "average_rotor_points_teleop": average_rotor_points_teleop,
                "average_score": average_score,
                "average_takeoff_points_teleop": average_takeoff_points_teleop,
                "average_win_margin": average_win_margin,
                "average_win_score": average_win_score,
                "high_kpa": high_kpa,
                "high_score": high_score,
                "kpa_achieved": kpa_achieved,
                "mobility_counts": mobility_counts,
                "rotor_1_engaged": rotor_1_engaged,
                "rotor_1_engaged_auto": rotor_1_engaged_auto,
                "rotor_2_engaged": rotor_2_engaged,
                "rotor_2_engaged_auto": rotor_2_engaged_auto,
                "rotor_3_engaged": rotor_3_engaged,
                "rotor_4_engaged": rotor_4_engaged,
                "takeoff_counts": takeoff_counts,
                "unicorn_matches": unicorn_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average_foul_score = d.pop("average_foul_score")

        average_fuel_points = d.pop("average_fuel_points")

        average_fuel_points_auto = d.pop("average_fuel_points_auto")

        average_fuel_points_teleop = d.pop("average_fuel_points_teleop")

        average_high_goals = d.pop("average_high_goals")

        average_high_goals_auto = d.pop("average_high_goals_auto")

        average_high_goals_teleop = d.pop("average_high_goals_teleop")

        average_low_goals = d.pop("average_low_goals")

        average_low_goals_auto = d.pop("average_low_goals_auto")

        average_low_goals_teleop = d.pop("average_low_goals_teleop")

        average_mobility_points_auto = d.pop("average_mobility_points_auto")

        average_points_auto = d.pop("average_points_auto")

        average_points_teleop = d.pop("average_points_teleop")

        average_rotor_points = d.pop("average_rotor_points")

        average_rotor_points_auto = d.pop("average_rotor_points_auto")

        average_rotor_points_teleop = d.pop("average_rotor_points_teleop")

        average_score = d.pop("average_score")

        average_takeoff_points_teleop = d.pop("average_takeoff_points_teleop")

        average_win_margin = d.pop("average_win_margin")

        average_win_score = d.pop("average_win_score")

        high_kpa = cast(list[str], d.pop("high_kpa"))

        high_score = cast(list[str], d.pop("high_score"))

        kpa_achieved = cast(list[float], d.pop("kpa_achieved"))

        mobility_counts = cast(list[float], d.pop("mobility_counts"))

        rotor_1_engaged = cast(list[float], d.pop("rotor_1_engaged"))

        rotor_1_engaged_auto = cast(list[float], d.pop("rotor_1_engaged_auto"))

        rotor_2_engaged = cast(list[float], d.pop("rotor_2_engaged"))

        rotor_2_engaged_auto = cast(list[float], d.pop("rotor_2_engaged_auto"))

        rotor_3_engaged = cast(list[float], d.pop("rotor_3_engaged"))

        rotor_4_engaged = cast(list[float], d.pop("rotor_4_engaged"))

        takeoff_counts = cast(list[float], d.pop("takeoff_counts"))

        unicorn_matches = cast(list[float], d.pop("unicorn_matches"))

        event_insights_2017 = cls(
            average_foul_score=average_foul_score,
            average_fuel_points=average_fuel_points,
            average_fuel_points_auto=average_fuel_points_auto,
            average_fuel_points_teleop=average_fuel_points_teleop,
            average_high_goals=average_high_goals,
            average_high_goals_auto=average_high_goals_auto,
            average_high_goals_teleop=average_high_goals_teleop,
            average_low_goals=average_low_goals,
            average_low_goals_auto=average_low_goals_auto,
            average_low_goals_teleop=average_low_goals_teleop,
            average_mobility_points_auto=average_mobility_points_auto,
            average_points_auto=average_points_auto,
            average_points_teleop=average_points_teleop,
            average_rotor_points=average_rotor_points,
            average_rotor_points_auto=average_rotor_points_auto,
            average_rotor_points_teleop=average_rotor_points_teleop,
            average_score=average_score,
            average_takeoff_points_teleop=average_takeoff_points_teleop,
            average_win_margin=average_win_margin,
            average_win_score=average_win_score,
            high_kpa=high_kpa,
            high_score=high_score,
            kpa_achieved=kpa_achieved,
            mobility_counts=mobility_counts,
            rotor_1_engaged=rotor_1_engaged,
            rotor_1_engaged_auto=rotor_1_engaged_auto,
            rotor_2_engaged=rotor_2_engaged,
            rotor_2_engaged_auto=rotor_2_engaged_auto,
            rotor_3_engaged=rotor_3_engaged,
            rotor_4_engaged=rotor_4_engaged,
            takeoff_counts=takeoff_counts,
            unicorn_matches=unicorn_matches,
        )

        event_insights_2017.additional_properties = d
        return event_insights_2017

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
