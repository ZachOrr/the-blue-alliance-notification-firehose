from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchTimeseries2018")


@_attrs_define
class MatchTimeseries2018:
    """Timeseries data for the 2018 game *FIRST* POWER UP.
    *WARNING:* This is *not* official data, and is subject to a significant possibility of error, or missing data. Do
    not rely on this data for any purpose. In fact, pretend we made it up.
    *WARNING:* This model is currently under active development and may change at any time, including in breaking ways.

        Attributes:
            event_key (str | Unset): TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE
                is the event code of the event.
            match_id (str | Unset): Match ID consisting of the level, match number, and set number, eg `qm45` or `f1m1`.
            mode (str | Unset): Current mode of play, can be `pre_match`, `auto`, `telop`, or `post_match`.
            play (int | Unset):
            time_remaining (int | Unset): Amount of time remaining in the match, only valid during `auto` and `teleop`
                modes.
            blue_auto_quest (int | Unset): 1 if the blue alliance is credited with the AUTO QUEST, 0 if not.
            blue_boost_count (int | Unset): Number of POWER CUBES in the BOOST section of the blue alliance VAULT.
            blue_boost_played (int | Unset): Returns 1 if the blue alliance BOOST was played, or 0 if not played.
            blue_current_powerup (str | Unset): Name of the current blue alliance POWER UP being played, or `null`.
            blue_face_the_boss (int | Unset): 1 if the blue alliance is credited with FACING THE BOSS, 0 if not.
            blue_force_count (int | Unset): Number of POWER CUBES in the FORCE section of the blue alliance VAULT.
            blue_force_played (int | Unset): Returns 1 if the blue alliance FORCE was played, or 0 if not played.
            blue_levitate_count (int | Unset): Number of POWER CUBES in the LEVITATE section of the blue alliance VAULT.
            blue_levitate_played (int | Unset): Returns 1 if the blue alliance LEVITATE was played, or 0 if not played.
            blue_powerup_time_remaining (str | Unset): Number of seconds remaining in the blue alliance POWER UP time, or 0
                if none is active.
            blue_scale_owned (int | Unset): 1 if the blue alliance owns the SCALE, 0 if not.
            blue_score (int | Unset): Current score for the blue alliance.
            blue_switch_owned (int | Unset): 1 if the blue alliance owns their SWITCH, 0 if not.
            red_auto_quest (int | Unset): 1 if the red alliance is credited with the AUTO QUEST, 0 if not.
            red_boost_count (int | Unset): Number of POWER CUBES in the BOOST section of the red alliance VAULT.
            red_boost_played (int | Unset): Returns 1 if the red alliance BOOST was played, or 0 if not played.
            red_current_powerup (str | Unset): Name of the current red alliance POWER UP being played, or `null`.
            red_face_the_boss (int | Unset): 1 if the red alliance is credited with FACING THE BOSS, 0 if not.
            red_force_count (int | Unset): Number of POWER CUBES in the FORCE section of the red alliance VAULT.
            red_force_played (int | Unset): Returns 1 if the red alliance FORCE was played, or 0 if not played.
            red_levitate_count (int | Unset): Number of POWER CUBES in the LEVITATE section of the red alliance VAULT.
            red_levitate_played (int | Unset): Returns 1 if the red alliance LEVITATE was played, or 0 if not played.
            red_powerup_time_remaining (str | Unset): Number of seconds remaining in the red alliance POWER UP time, or 0 if
                none is active.
            red_scale_owned (int | Unset): 1 if the red alliance owns the SCALE, 0 if not.
            red_score (int | Unset): Current score for the red alliance.
            red_switch_owned (int | Unset): 1 if the red alliance owns their SWITCH, 0 if not.
    """

    event_key: str | Unset = UNSET
    match_id: str | Unset = UNSET
    mode: str | Unset = UNSET
    play: int | Unset = UNSET
    time_remaining: int | Unset = UNSET
    blue_auto_quest: int | Unset = UNSET
    blue_boost_count: int | Unset = UNSET
    blue_boost_played: int | Unset = UNSET
    blue_current_powerup: str | Unset = UNSET
    blue_face_the_boss: int | Unset = UNSET
    blue_force_count: int | Unset = UNSET
    blue_force_played: int | Unset = UNSET
    blue_levitate_count: int | Unset = UNSET
    blue_levitate_played: int | Unset = UNSET
    blue_powerup_time_remaining: str | Unset = UNSET
    blue_scale_owned: int | Unset = UNSET
    blue_score: int | Unset = UNSET
    blue_switch_owned: int | Unset = UNSET
    red_auto_quest: int | Unset = UNSET
    red_boost_count: int | Unset = UNSET
    red_boost_played: int | Unset = UNSET
    red_current_powerup: str | Unset = UNSET
    red_face_the_boss: int | Unset = UNSET
    red_force_count: int | Unset = UNSET
    red_force_played: int | Unset = UNSET
    red_levitate_count: int | Unset = UNSET
    red_levitate_played: int | Unset = UNSET
    red_powerup_time_remaining: str | Unset = UNSET
    red_scale_owned: int | Unset = UNSET
    red_score: int | Unset = UNSET
    red_switch_owned: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_key = self.event_key

        match_id = self.match_id

        mode = self.mode

        play = self.play

        time_remaining = self.time_remaining

        blue_auto_quest = self.blue_auto_quest

        blue_boost_count = self.blue_boost_count

        blue_boost_played = self.blue_boost_played

        blue_current_powerup = self.blue_current_powerup

        blue_face_the_boss = self.blue_face_the_boss

        blue_force_count = self.blue_force_count

        blue_force_played = self.blue_force_played

        blue_levitate_count = self.blue_levitate_count

        blue_levitate_played = self.blue_levitate_played

        blue_powerup_time_remaining = self.blue_powerup_time_remaining

        blue_scale_owned = self.blue_scale_owned

        blue_score = self.blue_score

        blue_switch_owned = self.blue_switch_owned

        red_auto_quest = self.red_auto_quest

        red_boost_count = self.red_boost_count

        red_boost_played = self.red_boost_played

        red_current_powerup = self.red_current_powerup

        red_face_the_boss = self.red_face_the_boss

        red_force_count = self.red_force_count

        red_force_played = self.red_force_played

        red_levitate_count = self.red_levitate_count

        red_levitate_played = self.red_levitate_played

        red_powerup_time_remaining = self.red_powerup_time_remaining

        red_scale_owned = self.red_scale_owned

        red_score = self.red_score

        red_switch_owned = self.red_switch_owned

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_key is not UNSET:
            field_dict["event_key"] = event_key
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if play is not UNSET:
            field_dict["play"] = play
        if time_remaining is not UNSET:
            field_dict["time_remaining"] = time_remaining
        if blue_auto_quest is not UNSET:
            field_dict["blue_auto_quest"] = blue_auto_quest
        if blue_boost_count is not UNSET:
            field_dict["blue_boost_count"] = blue_boost_count
        if blue_boost_played is not UNSET:
            field_dict["blue_boost_played"] = blue_boost_played
        if blue_current_powerup is not UNSET:
            field_dict["blue_current_powerup"] = blue_current_powerup
        if blue_face_the_boss is not UNSET:
            field_dict["blue_face_the_boss"] = blue_face_the_boss
        if blue_force_count is not UNSET:
            field_dict["blue_force_count"] = blue_force_count
        if blue_force_played is not UNSET:
            field_dict["blue_force_played"] = blue_force_played
        if blue_levitate_count is not UNSET:
            field_dict["blue_levitate_count"] = blue_levitate_count
        if blue_levitate_played is not UNSET:
            field_dict["blue_levitate_played"] = blue_levitate_played
        if blue_powerup_time_remaining is not UNSET:
            field_dict["blue_powerup_time_remaining"] = blue_powerup_time_remaining
        if blue_scale_owned is not UNSET:
            field_dict["blue_scale_owned"] = blue_scale_owned
        if blue_score is not UNSET:
            field_dict["blue_score"] = blue_score
        if blue_switch_owned is not UNSET:
            field_dict["blue_switch_owned"] = blue_switch_owned
        if red_auto_quest is not UNSET:
            field_dict["red_auto_quest"] = red_auto_quest
        if red_boost_count is not UNSET:
            field_dict["red_boost_count"] = red_boost_count
        if red_boost_played is not UNSET:
            field_dict["red_boost_played"] = red_boost_played
        if red_current_powerup is not UNSET:
            field_dict["red_current_powerup"] = red_current_powerup
        if red_face_the_boss is not UNSET:
            field_dict["red_face_the_boss"] = red_face_the_boss
        if red_force_count is not UNSET:
            field_dict["red_force_count"] = red_force_count
        if red_force_played is not UNSET:
            field_dict["red_force_played"] = red_force_played
        if red_levitate_count is not UNSET:
            field_dict["red_levitate_count"] = red_levitate_count
        if red_levitate_played is not UNSET:
            field_dict["red_levitate_played"] = red_levitate_played
        if red_powerup_time_remaining is not UNSET:
            field_dict["red_powerup_time_remaining"] = red_powerup_time_remaining
        if red_scale_owned is not UNSET:
            field_dict["red_scale_owned"] = red_scale_owned
        if red_score is not UNSET:
            field_dict["red_score"] = red_score
        if red_switch_owned is not UNSET:
            field_dict["red_switch_owned"] = red_switch_owned

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_key = d.pop("event_key", UNSET)

        match_id = d.pop("match_id", UNSET)

        mode = d.pop("mode", UNSET)

        play = d.pop("play", UNSET)

        time_remaining = d.pop("time_remaining", UNSET)

        blue_auto_quest = d.pop("blue_auto_quest", UNSET)

        blue_boost_count = d.pop("blue_boost_count", UNSET)

        blue_boost_played = d.pop("blue_boost_played", UNSET)

        blue_current_powerup = d.pop("blue_current_powerup", UNSET)

        blue_face_the_boss = d.pop("blue_face_the_boss", UNSET)

        blue_force_count = d.pop("blue_force_count", UNSET)

        blue_force_played = d.pop("blue_force_played", UNSET)

        blue_levitate_count = d.pop("blue_levitate_count", UNSET)

        blue_levitate_played = d.pop("blue_levitate_played", UNSET)

        blue_powerup_time_remaining = d.pop("blue_powerup_time_remaining", UNSET)

        blue_scale_owned = d.pop("blue_scale_owned", UNSET)

        blue_score = d.pop("blue_score", UNSET)

        blue_switch_owned = d.pop("blue_switch_owned", UNSET)

        red_auto_quest = d.pop("red_auto_quest", UNSET)

        red_boost_count = d.pop("red_boost_count", UNSET)

        red_boost_played = d.pop("red_boost_played", UNSET)

        red_current_powerup = d.pop("red_current_powerup", UNSET)

        red_face_the_boss = d.pop("red_face_the_boss", UNSET)

        red_force_count = d.pop("red_force_count", UNSET)

        red_force_played = d.pop("red_force_played", UNSET)

        red_levitate_count = d.pop("red_levitate_count", UNSET)

        red_levitate_played = d.pop("red_levitate_played", UNSET)

        red_powerup_time_remaining = d.pop("red_powerup_time_remaining", UNSET)

        red_scale_owned = d.pop("red_scale_owned", UNSET)

        red_score = d.pop("red_score", UNSET)

        red_switch_owned = d.pop("red_switch_owned", UNSET)

        match_timeseries_2018 = cls(
            event_key=event_key,
            match_id=match_id,
            mode=mode,
            play=play,
            time_remaining=time_remaining,
            blue_auto_quest=blue_auto_quest,
            blue_boost_count=blue_boost_count,
            blue_boost_played=blue_boost_played,
            blue_current_powerup=blue_current_powerup,
            blue_face_the_boss=blue_face_the_boss,
            blue_force_count=blue_force_count,
            blue_force_played=blue_force_played,
            blue_levitate_count=blue_levitate_count,
            blue_levitate_played=blue_levitate_played,
            blue_powerup_time_remaining=blue_powerup_time_remaining,
            blue_scale_owned=blue_scale_owned,
            blue_score=blue_score,
            blue_switch_owned=blue_switch_owned,
            red_auto_quest=red_auto_quest,
            red_boost_count=red_boost_count,
            red_boost_played=red_boost_played,
            red_current_powerup=red_current_powerup,
            red_face_the_boss=red_face_the_boss,
            red_force_count=red_force_count,
            red_force_played=red_force_played,
            red_levitate_count=red_levitate_count,
            red_levitate_played=red_levitate_played,
            red_powerup_time_remaining=red_powerup_time_remaining,
            red_scale_owned=red_scale_owned,
            red_score=red_score,
            red_switch_owned=red_switch_owned,
        )

        match_timeseries_2018.additional_properties = d
        return match_timeseries_2018

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
