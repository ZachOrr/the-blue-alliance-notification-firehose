from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventInsights2016")


@_attrs_define
class EventInsights2016:
    """Insights for FIRST Stronghold qualification and elimination matches.

    Attributes:
        low_bar (list[float]): For the Low Bar - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        a_cheval_de_frise (list[float]): For the Cheval De Frise - An array with three values, number of times damaged,
            number of opportunities to damage, and percentage.
        a_portcullis (list[float]): For the Portcullis - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        b_ramparts (list[float]): For the Ramparts - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        b_moat (list[float]): For the Moat - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        c_sally_port (list[float]): For the Sally Port - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        c_drawbridge (list[float]): For the Drawbridge - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        d_rough_terrain (list[float]): For the Rough Terrain - An array with three values, number of times damaged,
            number of opportunities to damage, and percentage.
        d_rock_wall (list[float]): For the Rock Wall - An array with three values, number of times damaged, number of
            opportunities to damage, and percentage.
        average_high_goals (float): Average number of high goals scored.
        average_low_goals (float): Average number of low goals scored.
        breaches (list[float]): An array with three values, number of times breached, number of opportunities to breach,
            and percentage.
        scales (list[float]): An array with three values, number of times scaled, number of opportunities to scale, and
            percentage.
        challenges (list[float]): An array with three values, number of times challenged, number of opportunities to
            challenge, and percentage.
        captures (list[float]): An array with three values, number of times captured, number of opportunities to
            capture, and percentage.
        average_win_score (float): Average winning score.
        average_win_margin (float): Average margin of victory.
        average_score (float): Average total score.
        average_auto_score (float): Average autonomous score.
        average_crossing_score (float): Average crossing score.
        average_boulder_score (float): Average boulder score.
        average_tower_score (float): Average tower score.
        average_foul_score (float): Average foul score.
        high_score (list[str]): An array with three values, high score, match key from the match with the high score,
            and the name of the match.
    """

    low_bar: list[float]
    a_cheval_de_frise: list[float]
    a_portcullis: list[float]
    b_ramparts: list[float]
    b_moat: list[float]
    c_sally_port: list[float]
    c_drawbridge: list[float]
    d_rough_terrain: list[float]
    d_rock_wall: list[float]
    average_high_goals: float
    average_low_goals: float
    breaches: list[float]
    scales: list[float]
    challenges: list[float]
    captures: list[float]
    average_win_score: float
    average_win_margin: float
    average_score: float
    average_auto_score: float
    average_crossing_score: float
    average_boulder_score: float
    average_tower_score: float
    average_foul_score: float
    high_score: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        low_bar = self.low_bar

        a_cheval_de_frise = self.a_cheval_de_frise

        a_portcullis = self.a_portcullis

        b_ramparts = self.b_ramparts

        b_moat = self.b_moat

        c_sally_port = self.c_sally_port

        c_drawbridge = self.c_drawbridge

        d_rough_terrain = self.d_rough_terrain

        d_rock_wall = self.d_rock_wall

        average_high_goals = self.average_high_goals

        average_low_goals = self.average_low_goals

        breaches = self.breaches

        scales = self.scales

        challenges = self.challenges

        captures = self.captures

        average_win_score = self.average_win_score

        average_win_margin = self.average_win_margin

        average_score = self.average_score

        average_auto_score = self.average_auto_score

        average_crossing_score = self.average_crossing_score

        average_boulder_score = self.average_boulder_score

        average_tower_score = self.average_tower_score

        average_foul_score = self.average_foul_score

        high_score = self.high_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "LowBar": low_bar,
                "A_ChevalDeFrise": a_cheval_de_frise,
                "A_Portcullis": a_portcullis,
                "B_Ramparts": b_ramparts,
                "B_Moat": b_moat,
                "C_SallyPort": c_sally_port,
                "C_Drawbridge": c_drawbridge,
                "D_RoughTerrain": d_rough_terrain,
                "D_RockWall": d_rock_wall,
                "average_high_goals": average_high_goals,
                "average_low_goals": average_low_goals,
                "breaches": breaches,
                "scales": scales,
                "challenges": challenges,
                "captures": captures,
                "average_win_score": average_win_score,
                "average_win_margin": average_win_margin,
                "average_score": average_score,
                "average_auto_score": average_auto_score,
                "average_crossing_score": average_crossing_score,
                "average_boulder_score": average_boulder_score,
                "average_tower_score": average_tower_score,
                "average_foul_score": average_foul_score,
                "high_score": high_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        low_bar = cast(list[float], d.pop("LowBar"))

        a_cheval_de_frise = cast(list[float], d.pop("A_ChevalDeFrise"))

        a_portcullis = cast(list[float], d.pop("A_Portcullis"))

        b_ramparts = cast(list[float], d.pop("B_Ramparts"))

        b_moat = cast(list[float], d.pop("B_Moat"))

        c_sally_port = cast(list[float], d.pop("C_SallyPort"))

        c_drawbridge = cast(list[float], d.pop("C_Drawbridge"))

        d_rough_terrain = cast(list[float], d.pop("D_RoughTerrain"))

        d_rock_wall = cast(list[float], d.pop("D_RockWall"))

        average_high_goals = d.pop("average_high_goals")

        average_low_goals = d.pop("average_low_goals")

        breaches = cast(list[float], d.pop("breaches"))

        scales = cast(list[float], d.pop("scales"))

        challenges = cast(list[float], d.pop("challenges"))

        captures = cast(list[float], d.pop("captures"))

        average_win_score = d.pop("average_win_score")

        average_win_margin = d.pop("average_win_margin")

        average_score = d.pop("average_score")

        average_auto_score = d.pop("average_auto_score")

        average_crossing_score = d.pop("average_crossing_score")

        average_boulder_score = d.pop("average_boulder_score")

        average_tower_score = d.pop("average_tower_score")

        average_foul_score = d.pop("average_foul_score")

        high_score = cast(list[str], d.pop("high_score"))

        event_insights_2016 = cls(
            low_bar=low_bar,
            a_cheval_de_frise=a_cheval_de_frise,
            a_portcullis=a_portcullis,
            b_ramparts=b_ramparts,
            b_moat=b_moat,
            c_sally_port=c_sally_port,
            c_drawbridge=c_drawbridge,
            d_rough_terrain=d_rough_terrain,
            d_rock_wall=d_rock_wall,
            average_high_goals=average_high_goals,
            average_low_goals=average_low_goals,
            breaches=breaches,
            scales=scales,
            challenges=challenges,
            captures=captures,
            average_win_score=average_win_score,
            average_win_margin=average_win_margin,
            average_score=average_score,
            average_auto_score=average_auto_score,
            average_crossing_score=average_crossing_score,
            average_boulder_score=average_boulder_score,
            average_tower_score=average_tower_score,
            average_foul_score=average_foul_score,
            high_score=high_score,
        )

        event_insights_2016.additional_properties = d
        return event_insights_2016

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
