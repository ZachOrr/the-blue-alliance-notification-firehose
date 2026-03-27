from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EventInsights2018")


@_attrs_define
class EventInsights2018:
    """Insights for FIRST Power Up qualification and elimination matches.

    Attributes:
        auto_quest_achieved (list[float]): An array with three values, number of times auto quest was completed, number
            of opportunities to complete the auto quest, and percentage.
        average_boost_played (float): Average number of boost power up scored (out of 3).
        average_endgame_points (float): Average endgame points.
        average_force_played (float): Average number of force power up scored (out of 3).
        average_foul_score (float): Average foul score.
        average_points_auto (float): Average points scored during auto.
        average_points_teleop (float): Average points scored during teleop.
        average_run_points_auto (float): Average mobility points scored during auto.
        average_scale_ownership_points (float): Average scale ownership points scored.
        average_scale_ownership_points_auto (float): Average scale ownership points scored during auto.
        average_scale_ownership_points_teleop (float): Average scale ownership points scored during teleop.
        average_score (float): Average score.
        average_switch_ownership_points (float): Average switch ownership points scored.
        average_switch_ownership_points_auto (float): Average switch ownership points scored during auto.
        average_switch_ownership_points_teleop (float): Average switch ownership points scored during teleop.
        average_vault_points (float): Average value points scored.
        average_win_margin (float): Average margin of victory.
        average_win_score (float): Average winning score.
        boost_played_counts (list[float]): An array with three values, number of times a boost power up was played,
            number of opportunities to play a boost power up, and percentage.
        climb_counts (list[float]): An array with three values, number of times a climb occurred, number of
            opportunities to climb, and percentage.
        face_the_boss_achieved (list[float]): An array with three values, number of times an alliance faced the boss,
            number of opportunities to face the boss, and percentage.
        force_played_counts (list[float]): An array with three values, number of times a force power up was played,
            number of opportunities to play a force power up, and percentage.
        high_score (list[str]): An array with three values, high score, match key from the match with the high score,
            and the name of the match
        levitate_played_counts (list[float]): An array with three values, number of times a levitate power up was
            played, number of opportunities to play a levitate power up, and percentage.
        run_counts_auto (list[float]): An array with three values, number of times a team scored mobility points in
            auto, number of opportunities to score mobility points in auto, and percentage.
        scale_neutral_percentage (float): Average scale neutral percentage.
        scale_neutral_percentage_auto (float): Average scale neutral percentage during auto.
        scale_neutral_percentage_teleop (float): Average scale neutral percentage during teleop.
        switch_owned_counts_auto (list[float]): An array with three values, number of times a switch was owned during
            auto, number of opportunities to own a switch during auto, and percentage.
        unicorn_matches (list[float]): An array with three values, number of times a unicorn match (Win + Auto Quest +
            Face the Boss) occurred, number of opportunities to have a unicorn match, and percentage.
        winning_opp_switch_denial_percentage_teleop (float): Average opposing switch denail percentage for the winning
            alliance during teleop.
        winning_own_switch_ownership_percentage (float): Average own switch ownership percentage for the winning
            alliance.
        winning_own_switch_ownership_percentage_auto (float): Average own switch ownership percentage for the winning
            alliance during auto.
        winning_own_switch_ownership_percentage_teleop (float): Average own switch ownership percentage for the winning
            alliance during teleop.
        winning_scale_ownership_percentage (float): Average scale ownership percentage for the winning alliance.
        winning_scale_ownership_percentage_auto (float): Average scale ownership percentage for the winning alliance
            during auto.
        winning_scale_ownership_percentage_teleop (float): Average scale ownership percentage for the winning alliance
            during teleop.
    """

    auto_quest_achieved: list[float]
    average_boost_played: float
    average_endgame_points: float
    average_force_played: float
    average_foul_score: float
    average_points_auto: float
    average_points_teleop: float
    average_run_points_auto: float
    average_scale_ownership_points: float
    average_scale_ownership_points_auto: float
    average_scale_ownership_points_teleop: float
    average_score: float
    average_switch_ownership_points: float
    average_switch_ownership_points_auto: float
    average_switch_ownership_points_teleop: float
    average_vault_points: float
    average_win_margin: float
    average_win_score: float
    boost_played_counts: list[float]
    climb_counts: list[float]
    face_the_boss_achieved: list[float]
    force_played_counts: list[float]
    high_score: list[str]
    levitate_played_counts: list[float]
    run_counts_auto: list[float]
    scale_neutral_percentage: float
    scale_neutral_percentage_auto: float
    scale_neutral_percentage_teleop: float
    switch_owned_counts_auto: list[float]
    unicorn_matches: list[float]
    winning_opp_switch_denial_percentage_teleop: float
    winning_own_switch_ownership_percentage: float
    winning_own_switch_ownership_percentage_auto: float
    winning_own_switch_ownership_percentage_teleop: float
    winning_scale_ownership_percentage: float
    winning_scale_ownership_percentage_auto: float
    winning_scale_ownership_percentage_teleop: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_quest_achieved = self.auto_quest_achieved

        average_boost_played = self.average_boost_played

        average_endgame_points = self.average_endgame_points

        average_force_played = self.average_force_played

        average_foul_score = self.average_foul_score

        average_points_auto = self.average_points_auto

        average_points_teleop = self.average_points_teleop

        average_run_points_auto = self.average_run_points_auto

        average_scale_ownership_points = self.average_scale_ownership_points

        average_scale_ownership_points_auto = self.average_scale_ownership_points_auto

        average_scale_ownership_points_teleop = self.average_scale_ownership_points_teleop

        average_score = self.average_score

        average_switch_ownership_points = self.average_switch_ownership_points

        average_switch_ownership_points_auto = self.average_switch_ownership_points_auto

        average_switch_ownership_points_teleop = self.average_switch_ownership_points_teleop

        average_vault_points = self.average_vault_points

        average_win_margin = self.average_win_margin

        average_win_score = self.average_win_score

        boost_played_counts = self.boost_played_counts

        climb_counts = self.climb_counts

        face_the_boss_achieved = self.face_the_boss_achieved

        force_played_counts = self.force_played_counts

        high_score = self.high_score

        levitate_played_counts = self.levitate_played_counts

        run_counts_auto = self.run_counts_auto

        scale_neutral_percentage = self.scale_neutral_percentage

        scale_neutral_percentage_auto = self.scale_neutral_percentage_auto

        scale_neutral_percentage_teleop = self.scale_neutral_percentage_teleop

        switch_owned_counts_auto = self.switch_owned_counts_auto

        unicorn_matches = self.unicorn_matches

        winning_opp_switch_denial_percentage_teleop = self.winning_opp_switch_denial_percentage_teleop

        winning_own_switch_ownership_percentage = self.winning_own_switch_ownership_percentage

        winning_own_switch_ownership_percentage_auto = self.winning_own_switch_ownership_percentage_auto

        winning_own_switch_ownership_percentage_teleop = self.winning_own_switch_ownership_percentage_teleop

        winning_scale_ownership_percentage = self.winning_scale_ownership_percentage

        winning_scale_ownership_percentage_auto = self.winning_scale_ownership_percentage_auto

        winning_scale_ownership_percentage_teleop = self.winning_scale_ownership_percentage_teleop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auto_quest_achieved": auto_quest_achieved,
                "average_boost_played": average_boost_played,
                "average_endgame_points": average_endgame_points,
                "average_force_played": average_force_played,
                "average_foul_score": average_foul_score,
                "average_points_auto": average_points_auto,
                "average_points_teleop": average_points_teleop,
                "average_run_points_auto": average_run_points_auto,
                "average_scale_ownership_points": average_scale_ownership_points,
                "average_scale_ownership_points_auto": average_scale_ownership_points_auto,
                "average_scale_ownership_points_teleop": average_scale_ownership_points_teleop,
                "average_score": average_score,
                "average_switch_ownership_points": average_switch_ownership_points,
                "average_switch_ownership_points_auto": average_switch_ownership_points_auto,
                "average_switch_ownership_points_teleop": average_switch_ownership_points_teleop,
                "average_vault_points": average_vault_points,
                "average_win_margin": average_win_margin,
                "average_win_score": average_win_score,
                "boost_played_counts": boost_played_counts,
                "climb_counts": climb_counts,
                "face_the_boss_achieved": face_the_boss_achieved,
                "force_played_counts": force_played_counts,
                "high_score": high_score,
                "levitate_played_counts": levitate_played_counts,
                "run_counts_auto": run_counts_auto,
                "scale_neutral_percentage": scale_neutral_percentage,
                "scale_neutral_percentage_auto": scale_neutral_percentage_auto,
                "scale_neutral_percentage_teleop": scale_neutral_percentage_teleop,
                "switch_owned_counts_auto": switch_owned_counts_auto,
                "unicorn_matches": unicorn_matches,
                "winning_opp_switch_denial_percentage_teleop": winning_opp_switch_denial_percentage_teleop,
                "winning_own_switch_ownership_percentage": winning_own_switch_ownership_percentage,
                "winning_own_switch_ownership_percentage_auto": winning_own_switch_ownership_percentage_auto,
                "winning_own_switch_ownership_percentage_teleop": winning_own_switch_ownership_percentage_teleop,
                "winning_scale_ownership_percentage": winning_scale_ownership_percentage,
                "winning_scale_ownership_percentage_auto": winning_scale_ownership_percentage_auto,
                "winning_scale_ownership_percentage_teleop": winning_scale_ownership_percentage_teleop,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_quest_achieved = cast(list[float], d.pop("auto_quest_achieved"))

        average_boost_played = d.pop("average_boost_played")

        average_endgame_points = d.pop("average_endgame_points")

        average_force_played = d.pop("average_force_played")

        average_foul_score = d.pop("average_foul_score")

        average_points_auto = d.pop("average_points_auto")

        average_points_teleop = d.pop("average_points_teleop")

        average_run_points_auto = d.pop("average_run_points_auto")

        average_scale_ownership_points = d.pop("average_scale_ownership_points")

        average_scale_ownership_points_auto = d.pop("average_scale_ownership_points_auto")

        average_scale_ownership_points_teleop = d.pop("average_scale_ownership_points_teleop")

        average_score = d.pop("average_score")

        average_switch_ownership_points = d.pop("average_switch_ownership_points")

        average_switch_ownership_points_auto = d.pop("average_switch_ownership_points_auto")

        average_switch_ownership_points_teleop = d.pop("average_switch_ownership_points_teleop")

        average_vault_points = d.pop("average_vault_points")

        average_win_margin = d.pop("average_win_margin")

        average_win_score = d.pop("average_win_score")

        boost_played_counts = cast(list[float], d.pop("boost_played_counts"))

        climb_counts = cast(list[float], d.pop("climb_counts"))

        face_the_boss_achieved = cast(list[float], d.pop("face_the_boss_achieved"))

        force_played_counts = cast(list[float], d.pop("force_played_counts"))

        high_score = cast(list[str], d.pop("high_score"))

        levitate_played_counts = cast(list[float], d.pop("levitate_played_counts"))

        run_counts_auto = cast(list[float], d.pop("run_counts_auto"))

        scale_neutral_percentage = d.pop("scale_neutral_percentage")

        scale_neutral_percentage_auto = d.pop("scale_neutral_percentage_auto")

        scale_neutral_percentage_teleop = d.pop("scale_neutral_percentage_teleop")

        switch_owned_counts_auto = cast(list[float], d.pop("switch_owned_counts_auto"))

        unicorn_matches = cast(list[float], d.pop("unicorn_matches"))

        winning_opp_switch_denial_percentage_teleop = d.pop("winning_opp_switch_denial_percentage_teleop")

        winning_own_switch_ownership_percentage = d.pop("winning_own_switch_ownership_percentage")

        winning_own_switch_ownership_percentage_auto = d.pop("winning_own_switch_ownership_percentage_auto")

        winning_own_switch_ownership_percentage_teleop = d.pop("winning_own_switch_ownership_percentage_teleop")

        winning_scale_ownership_percentage = d.pop("winning_scale_ownership_percentage")

        winning_scale_ownership_percentage_auto = d.pop("winning_scale_ownership_percentage_auto")

        winning_scale_ownership_percentage_teleop = d.pop("winning_scale_ownership_percentage_teleop")

        event_insights_2018 = cls(
            auto_quest_achieved=auto_quest_achieved,
            average_boost_played=average_boost_played,
            average_endgame_points=average_endgame_points,
            average_force_played=average_force_played,
            average_foul_score=average_foul_score,
            average_points_auto=average_points_auto,
            average_points_teleop=average_points_teleop,
            average_run_points_auto=average_run_points_auto,
            average_scale_ownership_points=average_scale_ownership_points,
            average_scale_ownership_points_auto=average_scale_ownership_points_auto,
            average_scale_ownership_points_teleop=average_scale_ownership_points_teleop,
            average_score=average_score,
            average_switch_ownership_points=average_switch_ownership_points,
            average_switch_ownership_points_auto=average_switch_ownership_points_auto,
            average_switch_ownership_points_teleop=average_switch_ownership_points_teleop,
            average_vault_points=average_vault_points,
            average_win_margin=average_win_margin,
            average_win_score=average_win_score,
            boost_played_counts=boost_played_counts,
            climb_counts=climb_counts,
            face_the_boss_achieved=face_the_boss_achieved,
            force_played_counts=force_played_counts,
            high_score=high_score,
            levitate_played_counts=levitate_played_counts,
            run_counts_auto=run_counts_auto,
            scale_neutral_percentage=scale_neutral_percentage,
            scale_neutral_percentage_auto=scale_neutral_percentage_auto,
            scale_neutral_percentage_teleop=scale_neutral_percentage_teleop,
            switch_owned_counts_auto=switch_owned_counts_auto,
            unicorn_matches=unicorn_matches,
            winning_opp_switch_denial_percentage_teleop=winning_opp_switch_denial_percentage_teleop,
            winning_own_switch_ownership_percentage=winning_own_switch_ownership_percentage,
            winning_own_switch_ownership_percentage_auto=winning_own_switch_ownership_percentage_auto,
            winning_own_switch_ownership_percentage_teleop=winning_own_switch_ownership_percentage_teleop,
            winning_scale_ownership_percentage=winning_scale_ownership_percentage,
            winning_scale_ownership_percentage_auto=winning_scale_ownership_percentage_auto,
            winning_scale_ownership_percentage_teleop=winning_scale_ownership_percentage_teleop,
        )

        event_insights_2018.additional_properties = d
        return event_insights_2018

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
