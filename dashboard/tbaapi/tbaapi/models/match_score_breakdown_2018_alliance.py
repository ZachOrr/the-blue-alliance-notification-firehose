from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_robot_2018 import AutoRobot2018
from ..models.endgame_robot_2018 import EndgameRobot2018
from ..models.match_score_breakdown_2018_alliance_tba_game_data import MatchScoreBreakdown2018AllianceTbaGameData
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2018Alliance")


@_attrs_define
class MatchScoreBreakdown2018Alliance:
    """
    Attributes:
        auto_ownership_points (int):
        auto_points (int):
        auto_run_points (int):
        auto_scale_ownership_sec (int):
        auto_switch_ownership_sec (int):
        endgame_points (int):
        face_the_boss_ranking_point (bool):
        foul_points (int):
        rp (int):
        teleop_ownership_points (int):
        teleop_points (int):
        teleop_scale_boost_sec (int):
        teleop_scale_ownership_sec (int):
        teleop_switch_boost_sec (int):
        teleop_switch_ownership_sec (int):
        total_points (int):
        vault_boost_played (int):
        vault_boost_total (int):
        vault_force_played (int):
        vault_force_total (int):
        vault_levitate_played (int):
        vault_levitate_total (int):
        vault_points (int):
        adjust_points (int | Unset):
        auto_quest_ranking_point (bool | Unset):
        auto_robot_1 (AutoRobot2018 | Unset):
        auto_robot_2 (AutoRobot2018 | Unset):
        auto_robot_3 (AutoRobot2018 | Unset):
        auto_switch_at_zero (bool | Unset):
        endgame_robot_1 (EndgameRobot2018 | Unset):
        endgame_robot_2 (EndgameRobot2018 | Unset):
        endgame_robot_3 (EndgameRobot2018 | Unset):
        foul_count (int | Unset):
        tech_foul_count (int | Unset):
        teleop_scale_force_sec (int | Unset):
        teleop_switch_force_sec (int | Unset):
        tba_game_data (MatchScoreBreakdown2018AllianceTbaGameData | Unset): Unofficial TBA-computed value of the FMS
            provided GameData given to the alliance teams at the start of the match. 3 Character String containing `L` and
            `R` only. The first character represents the near switch, the 2nd the scale, and the 3rd the far, opposing,
            switch from the alliance's perspective. An `L` in a position indicates the platform on the left will be lit for
            the alliance while an `R` will indicate the right platform will be lit for the alliance. See also [WPI Screen
            Steps](https://wpilib.screenstepslive.com/s/currentCS/m/getting_started/l/826278-2018-game-data-details).
    """

    auto_ownership_points: int
    auto_points: int
    auto_run_points: int
    auto_scale_ownership_sec: int
    auto_switch_ownership_sec: int
    endgame_points: int
    face_the_boss_ranking_point: bool
    foul_points: int
    rp: int
    teleop_ownership_points: int
    teleop_points: int
    teleop_scale_boost_sec: int
    teleop_scale_ownership_sec: int
    teleop_switch_boost_sec: int
    teleop_switch_ownership_sec: int
    total_points: int
    vault_boost_played: int
    vault_boost_total: int
    vault_force_played: int
    vault_force_total: int
    vault_levitate_played: int
    vault_levitate_total: int
    vault_points: int
    adjust_points: int | Unset = UNSET
    auto_quest_ranking_point: bool | Unset = UNSET
    auto_robot_1: AutoRobot2018 | Unset = UNSET
    auto_robot_2: AutoRobot2018 | Unset = UNSET
    auto_robot_3: AutoRobot2018 | Unset = UNSET
    auto_switch_at_zero: bool | Unset = UNSET
    endgame_robot_1: EndgameRobot2018 | Unset = UNSET
    endgame_robot_2: EndgameRobot2018 | Unset = UNSET
    endgame_robot_3: EndgameRobot2018 | Unset = UNSET
    foul_count: int | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    teleop_scale_force_sec: int | Unset = UNSET
    teleop_switch_force_sec: int | Unset = UNSET
    tba_game_data: MatchScoreBreakdown2018AllianceTbaGameData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_ownership_points = self.auto_ownership_points

        auto_points = self.auto_points

        auto_run_points = self.auto_run_points

        auto_scale_ownership_sec = self.auto_scale_ownership_sec

        auto_switch_ownership_sec = self.auto_switch_ownership_sec

        endgame_points = self.endgame_points

        face_the_boss_ranking_point = self.face_the_boss_ranking_point

        foul_points = self.foul_points

        rp = self.rp

        teleop_ownership_points = self.teleop_ownership_points

        teleop_points = self.teleop_points

        teleop_scale_boost_sec = self.teleop_scale_boost_sec

        teleop_scale_ownership_sec = self.teleop_scale_ownership_sec

        teleop_switch_boost_sec = self.teleop_switch_boost_sec

        teleop_switch_ownership_sec = self.teleop_switch_ownership_sec

        total_points = self.total_points

        vault_boost_played = self.vault_boost_played

        vault_boost_total = self.vault_boost_total

        vault_force_played = self.vault_force_played

        vault_force_total = self.vault_force_total

        vault_levitate_played = self.vault_levitate_played

        vault_levitate_total = self.vault_levitate_total

        vault_points = self.vault_points

        adjust_points = self.adjust_points

        auto_quest_ranking_point = self.auto_quest_ranking_point

        auto_robot_1: str | Unset = UNSET
        if not isinstance(self.auto_robot_1, Unset):
            auto_robot_1 = self.auto_robot_1.value

        auto_robot_2: str | Unset = UNSET
        if not isinstance(self.auto_robot_2, Unset):
            auto_robot_2 = self.auto_robot_2.value

        auto_robot_3: str | Unset = UNSET
        if not isinstance(self.auto_robot_3, Unset):
            auto_robot_3 = self.auto_robot_3.value

        auto_switch_at_zero = self.auto_switch_at_zero

        endgame_robot_1: str | Unset = UNSET
        if not isinstance(self.endgame_robot_1, Unset):
            endgame_robot_1 = self.endgame_robot_1.value

        endgame_robot_2: str | Unset = UNSET
        if not isinstance(self.endgame_robot_2, Unset):
            endgame_robot_2 = self.endgame_robot_2.value

        endgame_robot_3: str | Unset = UNSET
        if not isinstance(self.endgame_robot_3, Unset):
            endgame_robot_3 = self.endgame_robot_3.value

        foul_count = self.foul_count

        tech_foul_count = self.tech_foul_count

        teleop_scale_force_sec = self.teleop_scale_force_sec

        teleop_switch_force_sec = self.teleop_switch_force_sec

        tba_game_data: str | Unset = UNSET
        if not isinstance(self.tba_game_data, Unset):
            tba_game_data = self.tba_game_data.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoOwnershipPoints": auto_ownership_points,
                "autoPoints": auto_points,
                "autoRunPoints": auto_run_points,
                "autoScaleOwnershipSec": auto_scale_ownership_sec,
                "autoSwitchOwnershipSec": auto_switch_ownership_sec,
                "endgamePoints": endgame_points,
                "faceTheBossRankingPoint": face_the_boss_ranking_point,
                "foulPoints": foul_points,
                "rp": rp,
                "teleopOwnershipPoints": teleop_ownership_points,
                "teleopPoints": teleop_points,
                "teleopScaleBoostSec": teleop_scale_boost_sec,
                "teleopScaleOwnershipSec": teleop_scale_ownership_sec,
                "teleopSwitchBoostSec": teleop_switch_boost_sec,
                "teleopSwitchOwnershipSec": teleop_switch_ownership_sec,
                "totalPoints": total_points,
                "vaultBoostPlayed": vault_boost_played,
                "vaultBoostTotal": vault_boost_total,
                "vaultForcePlayed": vault_force_played,
                "vaultForceTotal": vault_force_total,
                "vaultLevitatePlayed": vault_levitate_played,
                "vaultLevitateTotal": vault_levitate_total,
                "vaultPoints": vault_points,
            }
        )
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if auto_quest_ranking_point is not UNSET:
            field_dict["autoQuestRankingPoint"] = auto_quest_ranking_point
        if auto_robot_1 is not UNSET:
            field_dict["autoRobot1"] = auto_robot_1
        if auto_robot_2 is not UNSET:
            field_dict["autoRobot2"] = auto_robot_2
        if auto_robot_3 is not UNSET:
            field_dict["autoRobot3"] = auto_robot_3
        if auto_switch_at_zero is not UNSET:
            field_dict["autoSwitchAtZero"] = auto_switch_at_zero
        if endgame_robot_1 is not UNSET:
            field_dict["endgameRobot1"] = endgame_robot_1
        if endgame_robot_2 is not UNSET:
            field_dict["endgameRobot2"] = endgame_robot_2
        if endgame_robot_3 is not UNSET:
            field_dict["endgameRobot3"] = endgame_robot_3
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count
        if teleop_scale_force_sec is not UNSET:
            field_dict["teleopScaleForceSec"] = teleop_scale_force_sec
        if teleop_switch_force_sec is not UNSET:
            field_dict["teleopSwitchForceSec"] = teleop_switch_force_sec
        if tba_game_data is not UNSET:
            field_dict["tba_gameData"] = tba_game_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_ownership_points = d.pop("autoOwnershipPoints")

        auto_points = d.pop("autoPoints")

        auto_run_points = d.pop("autoRunPoints")

        auto_scale_ownership_sec = d.pop("autoScaleOwnershipSec")

        auto_switch_ownership_sec = d.pop("autoSwitchOwnershipSec")

        endgame_points = d.pop("endgamePoints")

        face_the_boss_ranking_point = d.pop("faceTheBossRankingPoint")

        foul_points = d.pop("foulPoints")

        rp = d.pop("rp")

        teleop_ownership_points = d.pop("teleopOwnershipPoints")

        teleop_points = d.pop("teleopPoints")

        teleop_scale_boost_sec = d.pop("teleopScaleBoostSec")

        teleop_scale_ownership_sec = d.pop("teleopScaleOwnershipSec")

        teleop_switch_boost_sec = d.pop("teleopSwitchBoostSec")

        teleop_switch_ownership_sec = d.pop("teleopSwitchOwnershipSec")

        total_points = d.pop("totalPoints")

        vault_boost_played = d.pop("vaultBoostPlayed")

        vault_boost_total = d.pop("vaultBoostTotal")

        vault_force_played = d.pop("vaultForcePlayed")

        vault_force_total = d.pop("vaultForceTotal")

        vault_levitate_played = d.pop("vaultLevitatePlayed")

        vault_levitate_total = d.pop("vaultLevitateTotal")

        vault_points = d.pop("vaultPoints")

        adjust_points = d.pop("adjustPoints", UNSET)

        auto_quest_ranking_point = d.pop("autoQuestRankingPoint", UNSET)

        _auto_robot_1 = d.pop("autoRobot1", UNSET)
        auto_robot_1: AutoRobot2018 | Unset
        if isinstance(_auto_robot_1, Unset):
            auto_robot_1 = UNSET
        else:
            auto_robot_1 = AutoRobot2018(_auto_robot_1)

        _auto_robot_2 = d.pop("autoRobot2", UNSET)
        auto_robot_2: AutoRobot2018 | Unset
        if isinstance(_auto_robot_2, Unset):
            auto_robot_2 = UNSET
        else:
            auto_robot_2 = AutoRobot2018(_auto_robot_2)

        _auto_robot_3 = d.pop("autoRobot3", UNSET)
        auto_robot_3: AutoRobot2018 | Unset
        if isinstance(_auto_robot_3, Unset):
            auto_robot_3 = UNSET
        else:
            auto_robot_3 = AutoRobot2018(_auto_robot_3)

        auto_switch_at_zero = d.pop("autoSwitchAtZero", UNSET)

        _endgame_robot_1 = d.pop("endgameRobot1", UNSET)
        endgame_robot_1: EndgameRobot2018 | Unset
        if isinstance(_endgame_robot_1, Unset):
            endgame_robot_1 = UNSET
        else:
            endgame_robot_1 = EndgameRobot2018(_endgame_robot_1)

        _endgame_robot_2 = d.pop("endgameRobot2", UNSET)
        endgame_robot_2: EndgameRobot2018 | Unset
        if isinstance(_endgame_robot_2, Unset):
            endgame_robot_2 = UNSET
        else:
            endgame_robot_2 = EndgameRobot2018(_endgame_robot_2)

        _endgame_robot_3 = d.pop("endgameRobot3", UNSET)
        endgame_robot_3: EndgameRobot2018 | Unset
        if isinstance(_endgame_robot_3, Unset):
            endgame_robot_3 = UNSET
        else:
            endgame_robot_3 = EndgameRobot2018(_endgame_robot_3)

        foul_count = d.pop("foulCount", UNSET)

        tech_foul_count = d.pop("techFoulCount", UNSET)

        teleop_scale_force_sec = d.pop("teleopScaleForceSec", UNSET)

        teleop_switch_force_sec = d.pop("teleopSwitchForceSec", UNSET)

        _tba_game_data = d.pop("tba_gameData", UNSET)
        tba_game_data: MatchScoreBreakdown2018AllianceTbaGameData | Unset
        if isinstance(_tba_game_data, Unset):
            tba_game_data = UNSET
        else:
            tba_game_data = MatchScoreBreakdown2018AllianceTbaGameData(_tba_game_data)

        match_score_breakdown_2018_alliance = cls(
            auto_ownership_points=auto_ownership_points,
            auto_points=auto_points,
            auto_run_points=auto_run_points,
            auto_scale_ownership_sec=auto_scale_ownership_sec,
            auto_switch_ownership_sec=auto_switch_ownership_sec,
            endgame_points=endgame_points,
            face_the_boss_ranking_point=face_the_boss_ranking_point,
            foul_points=foul_points,
            rp=rp,
            teleop_ownership_points=teleop_ownership_points,
            teleop_points=teleop_points,
            teleop_scale_boost_sec=teleop_scale_boost_sec,
            teleop_scale_ownership_sec=teleop_scale_ownership_sec,
            teleop_switch_boost_sec=teleop_switch_boost_sec,
            teleop_switch_ownership_sec=teleop_switch_ownership_sec,
            total_points=total_points,
            vault_boost_played=vault_boost_played,
            vault_boost_total=vault_boost_total,
            vault_force_played=vault_force_played,
            vault_force_total=vault_force_total,
            vault_levitate_played=vault_levitate_played,
            vault_levitate_total=vault_levitate_total,
            vault_points=vault_points,
            adjust_points=adjust_points,
            auto_quest_ranking_point=auto_quest_ranking_point,
            auto_robot_1=auto_robot_1,
            auto_robot_2=auto_robot_2,
            auto_robot_3=auto_robot_3,
            auto_switch_at_zero=auto_switch_at_zero,
            endgame_robot_1=endgame_robot_1,
            endgame_robot_2=endgame_robot_2,
            endgame_robot_3=endgame_robot_3,
            foul_count=foul_count,
            tech_foul_count=tech_foul_count,
            teleop_scale_force_sec=teleop_scale_force_sec,
            teleop_switch_force_sec=teleop_switch_force_sec,
            tba_game_data=tba_game_data,
        )

        match_score_breakdown_2018_alliance.additional_properties = d
        return match_score_breakdown_2018_alliance

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
