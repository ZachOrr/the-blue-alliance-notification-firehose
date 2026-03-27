from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_line_robot_2024 import AutoLineRobot2024
from ..models.end_game_robot_2024 import EndGameRobot2024
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchScoreBreakdown2024Alliance")


@_attrs_define
class MatchScoreBreakdown2024Alliance:
    """
    Attributes:
        rp (int):
        total_points (int):
        adjust_points (int | Unset):
        auto_amp_note_count (int | Unset):
        auto_amp_note_points (int | Unset):
        auto_leave_points (int | Unset):
        auto_line_robot_1 (AutoLineRobot2024 | Unset):
        auto_line_robot_2 (AutoLineRobot2024 | Unset):
        auto_line_robot_3 (AutoLineRobot2024 | Unset):
        auto_points (int | Unset):
        auto_speaker_note_count (int | Unset):
        auto_speaker_note_points (int | Unset):
        auto_total_note_points (int | Unset):
        coop_note_played (bool | Unset):
        coopertition_bonus_achieved (bool | Unset):
        coopertition_criteria_met (bool | Unset):
        end_game_harmony_points (int | Unset):
        end_game_note_in_trap_points (int | Unset):
        end_game_on_stage_points (int | Unset):
        end_game_park_points (int | Unset):
        end_game_robot_1 (EndGameRobot2024 | Unset):
        end_game_robot_2 (EndGameRobot2024 | Unset):
        end_game_robot_3 (EndGameRobot2024 | Unset):
        end_game_spot_light_bonus_points (int | Unset):
        end_game_total_stage_points (int | Unset):
        ensemble_bonus_achieved (bool | Unset):
        ensemble_bonus_on_stage_robots_threshold (int | Unset):
        ensemble_bonus_stage_points_threshold (int | Unset):
        foul_count (int | Unset):
        foul_points (int | Unset):
        g_206_penalty (bool | Unset):
        g_408_penalty (bool | Unset):
        g_424_penalty (bool | Unset):
        melody_bonus_achieved (bool | Unset):
        melody_bonus_threshold (int | Unset):
        melody_bonus_threshold_coop (int | Unset):
        melody_bonus_threshold_non_coop (int | Unset):
        mic_center_stage (bool | Unset):
        mic_stage_left (bool | Unset):
        mic_stage_right (bool | Unset):
        tech_foul_count (int | Unset):
        teleop_amp_note_count (int | Unset):
        teleop_amp_note_points (int | Unset):
        teleop_points (int | Unset):
        teleop_speaker_note_amplified_count (int | Unset):
        teleop_speaker_note_amplified_points (int | Unset):
        teleop_speaker_note_count (int | Unset):
        teleop_speaker_note_points (int | Unset):
        teleop_total_note_points (int | Unset):
        trap_center_stage (bool | Unset):
        trap_stage_left (bool | Unset):
        trap_stage_right (bool | Unset):
    """

    rp: int
    total_points: int
    adjust_points: int | Unset = UNSET
    auto_amp_note_count: int | Unset = UNSET
    auto_amp_note_points: int | Unset = UNSET
    auto_leave_points: int | Unset = UNSET
    auto_line_robot_1: AutoLineRobot2024 | Unset = UNSET
    auto_line_robot_2: AutoLineRobot2024 | Unset = UNSET
    auto_line_robot_3: AutoLineRobot2024 | Unset = UNSET
    auto_points: int | Unset = UNSET
    auto_speaker_note_count: int | Unset = UNSET
    auto_speaker_note_points: int | Unset = UNSET
    auto_total_note_points: int | Unset = UNSET
    coop_note_played: bool | Unset = UNSET
    coopertition_bonus_achieved: bool | Unset = UNSET
    coopertition_criteria_met: bool | Unset = UNSET
    end_game_harmony_points: int | Unset = UNSET
    end_game_note_in_trap_points: int | Unset = UNSET
    end_game_on_stage_points: int | Unset = UNSET
    end_game_park_points: int | Unset = UNSET
    end_game_robot_1: EndGameRobot2024 | Unset = UNSET
    end_game_robot_2: EndGameRobot2024 | Unset = UNSET
    end_game_robot_3: EndGameRobot2024 | Unset = UNSET
    end_game_spot_light_bonus_points: int | Unset = UNSET
    end_game_total_stage_points: int | Unset = UNSET
    ensemble_bonus_achieved: bool | Unset = UNSET
    ensemble_bonus_on_stage_robots_threshold: int | Unset = UNSET
    ensemble_bonus_stage_points_threshold: int | Unset = UNSET
    foul_count: int | Unset = UNSET
    foul_points: int | Unset = UNSET
    g_206_penalty: bool | Unset = UNSET
    g_408_penalty: bool | Unset = UNSET
    g_424_penalty: bool | Unset = UNSET
    melody_bonus_achieved: bool | Unset = UNSET
    melody_bonus_threshold: int | Unset = UNSET
    melody_bonus_threshold_coop: int | Unset = UNSET
    melody_bonus_threshold_non_coop: int | Unset = UNSET
    mic_center_stage: bool | Unset = UNSET
    mic_stage_left: bool | Unset = UNSET
    mic_stage_right: bool | Unset = UNSET
    tech_foul_count: int | Unset = UNSET
    teleop_amp_note_count: int | Unset = UNSET
    teleop_amp_note_points: int | Unset = UNSET
    teleop_points: int | Unset = UNSET
    teleop_speaker_note_amplified_count: int | Unset = UNSET
    teleop_speaker_note_amplified_points: int | Unset = UNSET
    teleop_speaker_note_count: int | Unset = UNSET
    teleop_speaker_note_points: int | Unset = UNSET
    teleop_total_note_points: int | Unset = UNSET
    trap_center_stage: bool | Unset = UNSET
    trap_stage_left: bool | Unset = UNSET
    trap_stage_right: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rp = self.rp

        total_points = self.total_points

        adjust_points = self.adjust_points

        auto_amp_note_count = self.auto_amp_note_count

        auto_amp_note_points = self.auto_amp_note_points

        auto_leave_points = self.auto_leave_points

        auto_line_robot_1: str | Unset = UNSET
        if not isinstance(self.auto_line_robot_1, Unset):
            auto_line_robot_1 = self.auto_line_robot_1.value

        auto_line_robot_2: str | Unset = UNSET
        if not isinstance(self.auto_line_robot_2, Unset):
            auto_line_robot_2 = self.auto_line_robot_2.value

        auto_line_robot_3: str | Unset = UNSET
        if not isinstance(self.auto_line_robot_3, Unset):
            auto_line_robot_3 = self.auto_line_robot_3.value

        auto_points = self.auto_points

        auto_speaker_note_count = self.auto_speaker_note_count

        auto_speaker_note_points = self.auto_speaker_note_points

        auto_total_note_points = self.auto_total_note_points

        coop_note_played = self.coop_note_played

        coopertition_bonus_achieved = self.coopertition_bonus_achieved

        coopertition_criteria_met = self.coopertition_criteria_met

        end_game_harmony_points = self.end_game_harmony_points

        end_game_note_in_trap_points = self.end_game_note_in_trap_points

        end_game_on_stage_points = self.end_game_on_stage_points

        end_game_park_points = self.end_game_park_points

        end_game_robot_1: str | Unset = UNSET
        if not isinstance(self.end_game_robot_1, Unset):
            end_game_robot_1 = self.end_game_robot_1.value

        end_game_robot_2: str | Unset = UNSET
        if not isinstance(self.end_game_robot_2, Unset):
            end_game_robot_2 = self.end_game_robot_2.value

        end_game_robot_3: str | Unset = UNSET
        if not isinstance(self.end_game_robot_3, Unset):
            end_game_robot_3 = self.end_game_robot_3.value

        end_game_spot_light_bonus_points = self.end_game_spot_light_bonus_points

        end_game_total_stage_points = self.end_game_total_stage_points

        ensemble_bonus_achieved = self.ensemble_bonus_achieved

        ensemble_bonus_on_stage_robots_threshold = self.ensemble_bonus_on_stage_robots_threshold

        ensemble_bonus_stage_points_threshold = self.ensemble_bonus_stage_points_threshold

        foul_count = self.foul_count

        foul_points = self.foul_points

        g_206_penalty = self.g_206_penalty

        g_408_penalty = self.g_408_penalty

        g_424_penalty = self.g_424_penalty

        melody_bonus_achieved = self.melody_bonus_achieved

        melody_bonus_threshold = self.melody_bonus_threshold

        melody_bonus_threshold_coop = self.melody_bonus_threshold_coop

        melody_bonus_threshold_non_coop = self.melody_bonus_threshold_non_coop

        mic_center_stage = self.mic_center_stage

        mic_stage_left = self.mic_stage_left

        mic_stage_right = self.mic_stage_right

        tech_foul_count = self.tech_foul_count

        teleop_amp_note_count = self.teleop_amp_note_count

        teleop_amp_note_points = self.teleop_amp_note_points

        teleop_points = self.teleop_points

        teleop_speaker_note_amplified_count = self.teleop_speaker_note_amplified_count

        teleop_speaker_note_amplified_points = self.teleop_speaker_note_amplified_points

        teleop_speaker_note_count = self.teleop_speaker_note_count

        teleop_speaker_note_points = self.teleop_speaker_note_points

        teleop_total_note_points = self.teleop_total_note_points

        trap_center_stage = self.trap_center_stage

        trap_stage_left = self.trap_stage_left

        trap_stage_right = self.trap_stage_right

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rp": rp,
                "totalPoints": total_points,
            }
        )
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if auto_amp_note_count is not UNSET:
            field_dict["autoAmpNoteCount"] = auto_amp_note_count
        if auto_amp_note_points is not UNSET:
            field_dict["autoAmpNotePoints"] = auto_amp_note_points
        if auto_leave_points is not UNSET:
            field_dict["autoLeavePoints"] = auto_leave_points
        if auto_line_robot_1 is not UNSET:
            field_dict["autoLineRobot1"] = auto_line_robot_1
        if auto_line_robot_2 is not UNSET:
            field_dict["autoLineRobot2"] = auto_line_robot_2
        if auto_line_robot_3 is not UNSET:
            field_dict["autoLineRobot3"] = auto_line_robot_3
        if auto_points is not UNSET:
            field_dict["autoPoints"] = auto_points
        if auto_speaker_note_count is not UNSET:
            field_dict["autoSpeakerNoteCount"] = auto_speaker_note_count
        if auto_speaker_note_points is not UNSET:
            field_dict["autoSpeakerNotePoints"] = auto_speaker_note_points
        if auto_total_note_points is not UNSET:
            field_dict["autoTotalNotePoints"] = auto_total_note_points
        if coop_note_played is not UNSET:
            field_dict["coopNotePlayed"] = coop_note_played
        if coopertition_bonus_achieved is not UNSET:
            field_dict["coopertitionBonusAchieved"] = coopertition_bonus_achieved
        if coopertition_criteria_met is not UNSET:
            field_dict["coopertitionCriteriaMet"] = coopertition_criteria_met
        if end_game_harmony_points is not UNSET:
            field_dict["endGameHarmonyPoints"] = end_game_harmony_points
        if end_game_note_in_trap_points is not UNSET:
            field_dict["endGameNoteInTrapPoints"] = end_game_note_in_trap_points
        if end_game_on_stage_points is not UNSET:
            field_dict["endGameOnStagePoints"] = end_game_on_stage_points
        if end_game_park_points is not UNSET:
            field_dict["endGameParkPoints"] = end_game_park_points
        if end_game_robot_1 is not UNSET:
            field_dict["endGameRobot1"] = end_game_robot_1
        if end_game_robot_2 is not UNSET:
            field_dict["endGameRobot2"] = end_game_robot_2
        if end_game_robot_3 is not UNSET:
            field_dict["endGameRobot3"] = end_game_robot_3
        if end_game_spot_light_bonus_points is not UNSET:
            field_dict["endGameSpotLightBonusPoints"] = end_game_spot_light_bonus_points
        if end_game_total_stage_points is not UNSET:
            field_dict["endGameTotalStagePoints"] = end_game_total_stage_points
        if ensemble_bonus_achieved is not UNSET:
            field_dict["ensembleBonusAchieved"] = ensemble_bonus_achieved
        if ensemble_bonus_on_stage_robots_threshold is not UNSET:
            field_dict["ensembleBonusOnStageRobotsThreshold"] = ensemble_bonus_on_stage_robots_threshold
        if ensemble_bonus_stage_points_threshold is not UNSET:
            field_dict["ensembleBonusStagePointsThreshold"] = ensemble_bonus_stage_points_threshold
        if foul_count is not UNSET:
            field_dict["foulCount"] = foul_count
        if foul_points is not UNSET:
            field_dict["foulPoints"] = foul_points
        if g_206_penalty is not UNSET:
            field_dict["g206Penalty"] = g_206_penalty
        if g_408_penalty is not UNSET:
            field_dict["g408Penalty"] = g_408_penalty
        if g_424_penalty is not UNSET:
            field_dict["g424Penalty"] = g_424_penalty
        if melody_bonus_achieved is not UNSET:
            field_dict["melodyBonusAchieved"] = melody_bonus_achieved
        if melody_bonus_threshold is not UNSET:
            field_dict["melodyBonusThreshold"] = melody_bonus_threshold
        if melody_bonus_threshold_coop is not UNSET:
            field_dict["melodyBonusThresholdCoop"] = melody_bonus_threshold_coop
        if melody_bonus_threshold_non_coop is not UNSET:
            field_dict["melodyBonusThresholdNonCoop"] = melody_bonus_threshold_non_coop
        if mic_center_stage is not UNSET:
            field_dict["micCenterStage"] = mic_center_stage
        if mic_stage_left is not UNSET:
            field_dict["micStageLeft"] = mic_stage_left
        if mic_stage_right is not UNSET:
            field_dict["micStageRight"] = mic_stage_right
        if tech_foul_count is not UNSET:
            field_dict["techFoulCount"] = tech_foul_count
        if teleop_amp_note_count is not UNSET:
            field_dict["teleopAmpNoteCount"] = teleop_amp_note_count
        if teleop_amp_note_points is not UNSET:
            field_dict["teleopAmpNotePoints"] = teleop_amp_note_points
        if teleop_points is not UNSET:
            field_dict["teleopPoints"] = teleop_points
        if teleop_speaker_note_amplified_count is not UNSET:
            field_dict["teleopSpeakerNoteAmplifiedCount"] = teleop_speaker_note_amplified_count
        if teleop_speaker_note_amplified_points is not UNSET:
            field_dict["teleopSpeakerNoteAmplifiedPoints"] = teleop_speaker_note_amplified_points
        if teleop_speaker_note_count is not UNSET:
            field_dict["teleopSpeakerNoteCount"] = teleop_speaker_note_count
        if teleop_speaker_note_points is not UNSET:
            field_dict["teleopSpeakerNotePoints"] = teleop_speaker_note_points
        if teleop_total_note_points is not UNSET:
            field_dict["teleopTotalNotePoints"] = teleop_total_note_points
        if trap_center_stage is not UNSET:
            field_dict["trapCenterStage"] = trap_center_stage
        if trap_stage_left is not UNSET:
            field_dict["trapStageLeft"] = trap_stage_left
        if trap_stage_right is not UNSET:
            field_dict["trapStageRight"] = trap_stage_right

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rp = d.pop("rp")

        total_points = d.pop("totalPoints")

        adjust_points = d.pop("adjustPoints", UNSET)

        auto_amp_note_count = d.pop("autoAmpNoteCount", UNSET)

        auto_amp_note_points = d.pop("autoAmpNotePoints", UNSET)

        auto_leave_points = d.pop("autoLeavePoints", UNSET)

        _auto_line_robot_1 = d.pop("autoLineRobot1", UNSET)
        auto_line_robot_1: AutoLineRobot2024 | Unset
        if isinstance(_auto_line_robot_1, Unset):
            auto_line_robot_1 = UNSET
        else:
            auto_line_robot_1 = AutoLineRobot2024(_auto_line_robot_1)

        _auto_line_robot_2 = d.pop("autoLineRobot2", UNSET)
        auto_line_robot_2: AutoLineRobot2024 | Unset
        if isinstance(_auto_line_robot_2, Unset):
            auto_line_robot_2 = UNSET
        else:
            auto_line_robot_2 = AutoLineRobot2024(_auto_line_robot_2)

        _auto_line_robot_3 = d.pop("autoLineRobot3", UNSET)
        auto_line_robot_3: AutoLineRobot2024 | Unset
        if isinstance(_auto_line_robot_3, Unset):
            auto_line_robot_3 = UNSET
        else:
            auto_line_robot_3 = AutoLineRobot2024(_auto_line_robot_3)

        auto_points = d.pop("autoPoints", UNSET)

        auto_speaker_note_count = d.pop("autoSpeakerNoteCount", UNSET)

        auto_speaker_note_points = d.pop("autoSpeakerNotePoints", UNSET)

        auto_total_note_points = d.pop("autoTotalNotePoints", UNSET)

        coop_note_played = d.pop("coopNotePlayed", UNSET)

        coopertition_bonus_achieved = d.pop("coopertitionBonusAchieved", UNSET)

        coopertition_criteria_met = d.pop("coopertitionCriteriaMet", UNSET)

        end_game_harmony_points = d.pop("endGameHarmonyPoints", UNSET)

        end_game_note_in_trap_points = d.pop("endGameNoteInTrapPoints", UNSET)

        end_game_on_stage_points = d.pop("endGameOnStagePoints", UNSET)

        end_game_park_points = d.pop("endGameParkPoints", UNSET)

        _end_game_robot_1 = d.pop("endGameRobot1", UNSET)
        end_game_robot_1: EndGameRobot2024 | Unset
        if isinstance(_end_game_robot_1, Unset):
            end_game_robot_1 = UNSET
        else:
            end_game_robot_1 = EndGameRobot2024(_end_game_robot_1)

        _end_game_robot_2 = d.pop("endGameRobot2", UNSET)
        end_game_robot_2: EndGameRobot2024 | Unset
        if isinstance(_end_game_robot_2, Unset):
            end_game_robot_2 = UNSET
        else:
            end_game_robot_2 = EndGameRobot2024(_end_game_robot_2)

        _end_game_robot_3 = d.pop("endGameRobot3", UNSET)
        end_game_robot_3: EndGameRobot2024 | Unset
        if isinstance(_end_game_robot_3, Unset):
            end_game_robot_3 = UNSET
        else:
            end_game_robot_3 = EndGameRobot2024(_end_game_robot_3)

        end_game_spot_light_bonus_points = d.pop("endGameSpotLightBonusPoints", UNSET)

        end_game_total_stage_points = d.pop("endGameTotalStagePoints", UNSET)

        ensemble_bonus_achieved = d.pop("ensembleBonusAchieved", UNSET)

        ensemble_bonus_on_stage_robots_threshold = d.pop("ensembleBonusOnStageRobotsThreshold", UNSET)

        ensemble_bonus_stage_points_threshold = d.pop("ensembleBonusStagePointsThreshold", UNSET)

        foul_count = d.pop("foulCount", UNSET)

        foul_points = d.pop("foulPoints", UNSET)

        g_206_penalty = d.pop("g206Penalty", UNSET)

        g_408_penalty = d.pop("g408Penalty", UNSET)

        g_424_penalty = d.pop("g424Penalty", UNSET)

        melody_bonus_achieved = d.pop("melodyBonusAchieved", UNSET)

        melody_bonus_threshold = d.pop("melodyBonusThreshold", UNSET)

        melody_bonus_threshold_coop = d.pop("melodyBonusThresholdCoop", UNSET)

        melody_bonus_threshold_non_coop = d.pop("melodyBonusThresholdNonCoop", UNSET)

        mic_center_stage = d.pop("micCenterStage", UNSET)

        mic_stage_left = d.pop("micStageLeft", UNSET)

        mic_stage_right = d.pop("micStageRight", UNSET)

        tech_foul_count = d.pop("techFoulCount", UNSET)

        teleop_amp_note_count = d.pop("teleopAmpNoteCount", UNSET)

        teleop_amp_note_points = d.pop("teleopAmpNotePoints", UNSET)

        teleop_points = d.pop("teleopPoints", UNSET)

        teleop_speaker_note_amplified_count = d.pop("teleopSpeakerNoteAmplifiedCount", UNSET)

        teleop_speaker_note_amplified_points = d.pop("teleopSpeakerNoteAmplifiedPoints", UNSET)

        teleop_speaker_note_count = d.pop("teleopSpeakerNoteCount", UNSET)

        teleop_speaker_note_points = d.pop("teleopSpeakerNotePoints", UNSET)

        teleop_total_note_points = d.pop("teleopTotalNotePoints", UNSET)

        trap_center_stage = d.pop("trapCenterStage", UNSET)

        trap_stage_left = d.pop("trapStageLeft", UNSET)

        trap_stage_right = d.pop("trapStageRight", UNSET)

        match_score_breakdown_2024_alliance = cls(
            rp=rp,
            total_points=total_points,
            adjust_points=adjust_points,
            auto_amp_note_count=auto_amp_note_count,
            auto_amp_note_points=auto_amp_note_points,
            auto_leave_points=auto_leave_points,
            auto_line_robot_1=auto_line_robot_1,
            auto_line_robot_2=auto_line_robot_2,
            auto_line_robot_3=auto_line_robot_3,
            auto_points=auto_points,
            auto_speaker_note_count=auto_speaker_note_count,
            auto_speaker_note_points=auto_speaker_note_points,
            auto_total_note_points=auto_total_note_points,
            coop_note_played=coop_note_played,
            coopertition_bonus_achieved=coopertition_bonus_achieved,
            coopertition_criteria_met=coopertition_criteria_met,
            end_game_harmony_points=end_game_harmony_points,
            end_game_note_in_trap_points=end_game_note_in_trap_points,
            end_game_on_stage_points=end_game_on_stage_points,
            end_game_park_points=end_game_park_points,
            end_game_robot_1=end_game_robot_1,
            end_game_robot_2=end_game_robot_2,
            end_game_robot_3=end_game_robot_3,
            end_game_spot_light_bonus_points=end_game_spot_light_bonus_points,
            end_game_total_stage_points=end_game_total_stage_points,
            ensemble_bonus_achieved=ensemble_bonus_achieved,
            ensemble_bonus_on_stage_robots_threshold=ensemble_bonus_on_stage_robots_threshold,
            ensemble_bonus_stage_points_threshold=ensemble_bonus_stage_points_threshold,
            foul_count=foul_count,
            foul_points=foul_points,
            g_206_penalty=g_206_penalty,
            g_408_penalty=g_408_penalty,
            g_424_penalty=g_424_penalty,
            melody_bonus_achieved=melody_bonus_achieved,
            melody_bonus_threshold=melody_bonus_threshold,
            melody_bonus_threshold_coop=melody_bonus_threshold_coop,
            melody_bonus_threshold_non_coop=melody_bonus_threshold_non_coop,
            mic_center_stage=mic_center_stage,
            mic_stage_left=mic_stage_left,
            mic_stage_right=mic_stage_right,
            tech_foul_count=tech_foul_count,
            teleop_amp_note_count=teleop_amp_note_count,
            teleop_amp_note_points=teleop_amp_note_points,
            teleop_points=teleop_points,
            teleop_speaker_note_amplified_count=teleop_speaker_note_amplified_count,
            teleop_speaker_note_amplified_points=teleop_speaker_note_amplified_points,
            teleop_speaker_note_count=teleop_speaker_note_count,
            teleop_speaker_note_points=teleop_speaker_note_points,
            teleop_total_note_points=teleop_total_note_points,
            trap_center_stage=trap_center_stage,
            trap_stage_left=trap_stage_left,
            trap_stage_right=trap_stage_right,
        )

        match_score_breakdown_2024_alliance.additional_properties = d
        return match_score_breakdown_2024_alliance

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
