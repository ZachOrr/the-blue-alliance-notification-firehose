from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auto_charge_station_robot_2023 import AutoChargeStationRobot2023
from ..models.bridge_state_2023 import BridgeState2023
from ..models.end_game_charge_station_robot_2023 import EndGameChargeStationRobot2023
from ..models.mobility_robot_2023 import MobilityRobot2023
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_score_breakdown_2023_alliance_auto_community import MatchScoreBreakdown2023AllianceAutoCommunity
    from ..models.match_score_breakdown_2023_alliance_links_type_0_item import (
        MatchScoreBreakdown2023AllianceLinksType0Item,
    )
    from ..models.match_score_breakdown_2023_alliance_teleop_community import (
        MatchScoreBreakdown2023AllianceTeleopCommunity,
    )


T = TypeVar("T", bound="MatchScoreBreakdown2023Alliance")


@_attrs_define
class MatchScoreBreakdown2023Alliance:
    """
    Attributes:
        auto_mobility_points (int):
        mobility_robot_1 (MobilityRobot2023):
        mobility_robot_2 (MobilityRobot2023):
        mobility_robot_3 (MobilityRobot2023):
        auto_points (int):
        foul_count (int):
        foul_points (int):
        tech_foul_count (int):
        teleop_points (int):
        rp (int):
        total_points (int):
        activation_bonus_achieved (bool | Unset):
        adjust_points (int | Unset):
        auto_bridge_state (BridgeState2023 | Unset):
        auto_charge_station_points (int | Unset):
        auto_charge_station_robot_1 (AutoChargeStationRobot2023 | Unset):
        auto_charge_station_robot_2 (AutoChargeStationRobot2023 | Unset):
        auto_charge_station_robot_3 (AutoChargeStationRobot2023 | Unset):
        auto_docked (bool | Unset):
        auto_community (MatchScoreBreakdown2023AllianceAutoCommunity | Unset):
        auto_game_piece_count (int | Unset):
        auto_game_piece_points (int | Unset):
        coop_game_piece_count (int | Unset):
        coopertition_criteria_met (bool | Unset):
        end_game_bridge_state (BridgeState2023 | Unset):
        end_game_charge_station_points (int | Unset):
        end_game_charge_station_robot_1 (EndGameChargeStationRobot2023 | Unset):
        end_game_charge_station_robot_2 (EndGameChargeStationRobot2023 | Unset):
        end_game_charge_station_robot_3 (EndGameChargeStationRobot2023 | Unset):
        end_game_park_points (int | Unset):
        extra_game_piece_count (int | Unset):
        link_points (int | Unset):
        links (list[MatchScoreBreakdown2023AllianceLinksType0Item] | None | Unset):
        sustainability_bonus_achieved (bool | Unset):
        teleop_community (MatchScoreBreakdown2023AllianceTeleopCommunity | Unset):
        teleop_game_piece_count (int | Unset):
        teleop_game_piece_points (int | Unset):
        total_charge_station_points (int | Unset):
    """

    auto_mobility_points: int
    mobility_robot_1: MobilityRobot2023
    mobility_robot_2: MobilityRobot2023
    mobility_robot_3: MobilityRobot2023
    auto_points: int
    foul_count: int
    foul_points: int
    tech_foul_count: int
    teleop_points: int
    rp: int
    total_points: int
    activation_bonus_achieved: bool | Unset = UNSET
    adjust_points: int | Unset = UNSET
    auto_bridge_state: BridgeState2023 | Unset = UNSET
    auto_charge_station_points: int | Unset = UNSET
    auto_charge_station_robot_1: AutoChargeStationRobot2023 | Unset = UNSET
    auto_charge_station_robot_2: AutoChargeStationRobot2023 | Unset = UNSET
    auto_charge_station_robot_3: AutoChargeStationRobot2023 | Unset = UNSET
    auto_docked: bool | Unset = UNSET
    auto_community: MatchScoreBreakdown2023AllianceAutoCommunity | Unset = UNSET
    auto_game_piece_count: int | Unset = UNSET
    auto_game_piece_points: int | Unset = UNSET
    coop_game_piece_count: int | Unset = UNSET
    coopertition_criteria_met: bool | Unset = UNSET
    end_game_bridge_state: BridgeState2023 | Unset = UNSET
    end_game_charge_station_points: int | Unset = UNSET
    end_game_charge_station_robot_1: EndGameChargeStationRobot2023 | Unset = UNSET
    end_game_charge_station_robot_2: EndGameChargeStationRobot2023 | Unset = UNSET
    end_game_charge_station_robot_3: EndGameChargeStationRobot2023 | Unset = UNSET
    end_game_park_points: int | Unset = UNSET
    extra_game_piece_count: int | Unset = UNSET
    link_points: int | Unset = UNSET
    links: list[MatchScoreBreakdown2023AllianceLinksType0Item] | None | Unset = UNSET
    sustainability_bonus_achieved: bool | Unset = UNSET
    teleop_community: MatchScoreBreakdown2023AllianceTeleopCommunity | Unset = UNSET
    teleop_game_piece_count: int | Unset = UNSET
    teleop_game_piece_points: int | Unset = UNSET
    total_charge_station_points: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_mobility_points = self.auto_mobility_points

        mobility_robot_1 = self.mobility_robot_1.value

        mobility_robot_2 = self.mobility_robot_2.value

        mobility_robot_3 = self.mobility_robot_3.value

        auto_points = self.auto_points

        foul_count = self.foul_count

        foul_points = self.foul_points

        tech_foul_count = self.tech_foul_count

        teleop_points = self.teleop_points

        rp = self.rp

        total_points = self.total_points

        activation_bonus_achieved = self.activation_bonus_achieved

        adjust_points = self.adjust_points

        auto_bridge_state: str | Unset = UNSET
        if not isinstance(self.auto_bridge_state, Unset):
            auto_bridge_state = self.auto_bridge_state.value

        auto_charge_station_points = self.auto_charge_station_points

        auto_charge_station_robot_1: str | Unset = UNSET
        if not isinstance(self.auto_charge_station_robot_1, Unset):
            auto_charge_station_robot_1 = self.auto_charge_station_robot_1.value

        auto_charge_station_robot_2: str | Unset = UNSET
        if not isinstance(self.auto_charge_station_robot_2, Unset):
            auto_charge_station_robot_2 = self.auto_charge_station_robot_2.value

        auto_charge_station_robot_3: str | Unset = UNSET
        if not isinstance(self.auto_charge_station_robot_3, Unset):
            auto_charge_station_robot_3 = self.auto_charge_station_robot_3.value

        auto_docked = self.auto_docked

        auto_community: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_community, Unset):
            auto_community = self.auto_community.to_dict()

        auto_game_piece_count = self.auto_game_piece_count

        auto_game_piece_points = self.auto_game_piece_points

        coop_game_piece_count = self.coop_game_piece_count

        coopertition_criteria_met = self.coopertition_criteria_met

        end_game_bridge_state: str | Unset = UNSET
        if not isinstance(self.end_game_bridge_state, Unset):
            end_game_bridge_state = self.end_game_bridge_state.value

        end_game_charge_station_points = self.end_game_charge_station_points

        end_game_charge_station_robot_1: str | Unset = UNSET
        if not isinstance(self.end_game_charge_station_robot_1, Unset):
            end_game_charge_station_robot_1 = self.end_game_charge_station_robot_1.value

        end_game_charge_station_robot_2: str | Unset = UNSET
        if not isinstance(self.end_game_charge_station_robot_2, Unset):
            end_game_charge_station_robot_2 = self.end_game_charge_station_robot_2.value

        end_game_charge_station_robot_3: str | Unset = UNSET
        if not isinstance(self.end_game_charge_station_robot_3, Unset):
            end_game_charge_station_robot_3 = self.end_game_charge_station_robot_3.value

        end_game_park_points = self.end_game_park_points

        extra_game_piece_count = self.extra_game_piece_count

        link_points = self.link_points

        links: list[dict[str, Any]] | None | Unset
        if isinstance(self.links, Unset):
            links = UNSET
        elif isinstance(self.links, list):
            links = []
            for links_type_0_item_data in self.links:
                links_type_0_item = links_type_0_item_data.to_dict()
                links.append(links_type_0_item)

        else:
            links = self.links

        sustainability_bonus_achieved = self.sustainability_bonus_achieved

        teleop_community: dict[str, Any] | Unset = UNSET
        if not isinstance(self.teleop_community, Unset):
            teleop_community = self.teleop_community.to_dict()

        teleop_game_piece_count = self.teleop_game_piece_count

        teleop_game_piece_points = self.teleop_game_piece_points

        total_charge_station_points = self.total_charge_station_points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoMobilityPoints": auto_mobility_points,
                "mobilityRobot1": mobility_robot_1,
                "mobilityRobot2": mobility_robot_2,
                "mobilityRobot3": mobility_robot_3,
                "autoPoints": auto_points,
                "foulCount": foul_count,
                "foulPoints": foul_points,
                "techFoulCount": tech_foul_count,
                "teleopPoints": teleop_points,
                "rp": rp,
                "totalPoints": total_points,
            }
        )
        if activation_bonus_achieved is not UNSET:
            field_dict["activationBonusAchieved"] = activation_bonus_achieved
        if adjust_points is not UNSET:
            field_dict["adjustPoints"] = adjust_points
        if auto_bridge_state is not UNSET:
            field_dict["autoBridgeState"] = auto_bridge_state
        if auto_charge_station_points is not UNSET:
            field_dict["autoChargeStationPoints"] = auto_charge_station_points
        if auto_charge_station_robot_1 is not UNSET:
            field_dict["autoChargeStationRobot1"] = auto_charge_station_robot_1
        if auto_charge_station_robot_2 is not UNSET:
            field_dict["autoChargeStationRobot2"] = auto_charge_station_robot_2
        if auto_charge_station_robot_3 is not UNSET:
            field_dict["autoChargeStationRobot3"] = auto_charge_station_robot_3
        if auto_docked is not UNSET:
            field_dict["autoDocked"] = auto_docked
        if auto_community is not UNSET:
            field_dict["autoCommunity"] = auto_community
        if auto_game_piece_count is not UNSET:
            field_dict["autoGamePieceCount"] = auto_game_piece_count
        if auto_game_piece_points is not UNSET:
            field_dict["autoGamePiecePoints"] = auto_game_piece_points
        if coop_game_piece_count is not UNSET:
            field_dict["coopGamePieceCount"] = coop_game_piece_count
        if coopertition_criteria_met is not UNSET:
            field_dict["coopertitionCriteriaMet"] = coopertition_criteria_met
        if end_game_bridge_state is not UNSET:
            field_dict["endGameBridgeState"] = end_game_bridge_state
        if end_game_charge_station_points is not UNSET:
            field_dict["endGameChargeStationPoints"] = end_game_charge_station_points
        if end_game_charge_station_robot_1 is not UNSET:
            field_dict["endGameChargeStationRobot1"] = end_game_charge_station_robot_1
        if end_game_charge_station_robot_2 is not UNSET:
            field_dict["endGameChargeStationRobot2"] = end_game_charge_station_robot_2
        if end_game_charge_station_robot_3 is not UNSET:
            field_dict["endGameChargeStationRobot3"] = end_game_charge_station_robot_3
        if end_game_park_points is not UNSET:
            field_dict["endGameParkPoints"] = end_game_park_points
        if extra_game_piece_count is not UNSET:
            field_dict["extraGamePieceCount"] = extra_game_piece_count
        if link_points is not UNSET:
            field_dict["linkPoints"] = link_points
        if links is not UNSET:
            field_dict["links"] = links
        if sustainability_bonus_achieved is not UNSET:
            field_dict["sustainabilityBonusAchieved"] = sustainability_bonus_achieved
        if teleop_community is not UNSET:
            field_dict["teleopCommunity"] = teleop_community
        if teleop_game_piece_count is not UNSET:
            field_dict["teleopGamePieceCount"] = teleop_game_piece_count
        if teleop_game_piece_points is not UNSET:
            field_dict["teleopGamePiecePoints"] = teleop_game_piece_points
        if total_charge_station_points is not UNSET:
            field_dict["totalChargeStationPoints"] = total_charge_station_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_score_breakdown_2023_alliance_auto_community import (
            MatchScoreBreakdown2023AllianceAutoCommunity,
        )
        from ..models.match_score_breakdown_2023_alliance_links_type_0_item import (
            MatchScoreBreakdown2023AllianceLinksType0Item,
        )
        from ..models.match_score_breakdown_2023_alliance_teleop_community import (
            MatchScoreBreakdown2023AllianceTeleopCommunity,
        )

        d = dict(src_dict)
        auto_mobility_points = d.pop("autoMobilityPoints")

        mobility_robot_1 = MobilityRobot2023(d.pop("mobilityRobot1"))

        mobility_robot_2 = MobilityRobot2023(d.pop("mobilityRobot2"))

        mobility_robot_3 = MobilityRobot2023(d.pop("mobilityRobot3"))

        auto_points = d.pop("autoPoints")

        foul_count = d.pop("foulCount")

        foul_points = d.pop("foulPoints")

        tech_foul_count = d.pop("techFoulCount")

        teleop_points = d.pop("teleopPoints")

        rp = d.pop("rp")

        total_points = d.pop("totalPoints")

        activation_bonus_achieved = d.pop("activationBonusAchieved", UNSET)

        adjust_points = d.pop("adjustPoints", UNSET)

        _auto_bridge_state = d.pop("autoBridgeState", UNSET)
        auto_bridge_state: BridgeState2023 | Unset
        if isinstance(_auto_bridge_state, Unset):
            auto_bridge_state = UNSET
        else:
            auto_bridge_state = BridgeState2023(_auto_bridge_state)

        auto_charge_station_points = d.pop("autoChargeStationPoints", UNSET)

        _auto_charge_station_robot_1 = d.pop("autoChargeStationRobot1", UNSET)
        auto_charge_station_robot_1: AutoChargeStationRobot2023 | Unset
        if isinstance(_auto_charge_station_robot_1, Unset):
            auto_charge_station_robot_1 = UNSET
        else:
            auto_charge_station_robot_1 = AutoChargeStationRobot2023(_auto_charge_station_robot_1)

        _auto_charge_station_robot_2 = d.pop("autoChargeStationRobot2", UNSET)
        auto_charge_station_robot_2: AutoChargeStationRobot2023 | Unset
        if isinstance(_auto_charge_station_robot_2, Unset):
            auto_charge_station_robot_2 = UNSET
        else:
            auto_charge_station_robot_2 = AutoChargeStationRobot2023(_auto_charge_station_robot_2)

        _auto_charge_station_robot_3 = d.pop("autoChargeStationRobot3", UNSET)
        auto_charge_station_robot_3: AutoChargeStationRobot2023 | Unset
        if isinstance(_auto_charge_station_robot_3, Unset):
            auto_charge_station_robot_3 = UNSET
        else:
            auto_charge_station_robot_3 = AutoChargeStationRobot2023(_auto_charge_station_robot_3)

        auto_docked = d.pop("autoDocked", UNSET)

        _auto_community = d.pop("autoCommunity", UNSET)
        auto_community: MatchScoreBreakdown2023AllianceAutoCommunity | Unset
        if isinstance(_auto_community, Unset):
            auto_community = UNSET
        else:
            auto_community = MatchScoreBreakdown2023AllianceAutoCommunity.from_dict(_auto_community)

        auto_game_piece_count = d.pop("autoGamePieceCount", UNSET)

        auto_game_piece_points = d.pop("autoGamePiecePoints", UNSET)

        coop_game_piece_count = d.pop("coopGamePieceCount", UNSET)

        coopertition_criteria_met = d.pop("coopertitionCriteriaMet", UNSET)

        _end_game_bridge_state = d.pop("endGameBridgeState", UNSET)
        end_game_bridge_state: BridgeState2023 | Unset
        if isinstance(_end_game_bridge_state, Unset):
            end_game_bridge_state = UNSET
        else:
            end_game_bridge_state = BridgeState2023(_end_game_bridge_state)

        end_game_charge_station_points = d.pop("endGameChargeStationPoints", UNSET)

        _end_game_charge_station_robot_1 = d.pop("endGameChargeStationRobot1", UNSET)
        end_game_charge_station_robot_1: EndGameChargeStationRobot2023 | Unset
        if isinstance(_end_game_charge_station_robot_1, Unset):
            end_game_charge_station_robot_1 = UNSET
        else:
            end_game_charge_station_robot_1 = EndGameChargeStationRobot2023(_end_game_charge_station_robot_1)

        _end_game_charge_station_robot_2 = d.pop("endGameChargeStationRobot2", UNSET)
        end_game_charge_station_robot_2: EndGameChargeStationRobot2023 | Unset
        if isinstance(_end_game_charge_station_robot_2, Unset):
            end_game_charge_station_robot_2 = UNSET
        else:
            end_game_charge_station_robot_2 = EndGameChargeStationRobot2023(_end_game_charge_station_robot_2)

        _end_game_charge_station_robot_3 = d.pop("endGameChargeStationRobot3", UNSET)
        end_game_charge_station_robot_3: EndGameChargeStationRobot2023 | Unset
        if isinstance(_end_game_charge_station_robot_3, Unset):
            end_game_charge_station_robot_3 = UNSET
        else:
            end_game_charge_station_robot_3 = EndGameChargeStationRobot2023(_end_game_charge_station_robot_3)

        end_game_park_points = d.pop("endGameParkPoints", UNSET)

        extra_game_piece_count = d.pop("extraGamePieceCount", UNSET)

        link_points = d.pop("linkPoints", UNSET)

        def _parse_links(data: object) -> list[MatchScoreBreakdown2023AllianceLinksType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                links_type_0 = []
                _links_type_0 = data
                for links_type_0_item_data in _links_type_0:
                    links_type_0_item = MatchScoreBreakdown2023AllianceLinksType0Item.from_dict(links_type_0_item_data)

                    links_type_0.append(links_type_0_item)

                return links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MatchScoreBreakdown2023AllianceLinksType0Item] | None | Unset, data)

        links = _parse_links(d.pop("links", UNSET))

        sustainability_bonus_achieved = d.pop("sustainabilityBonusAchieved", UNSET)

        _teleop_community = d.pop("teleopCommunity", UNSET)
        teleop_community: MatchScoreBreakdown2023AllianceTeleopCommunity | Unset
        if isinstance(_teleop_community, Unset):
            teleop_community = UNSET
        else:
            teleop_community = MatchScoreBreakdown2023AllianceTeleopCommunity.from_dict(_teleop_community)

        teleop_game_piece_count = d.pop("teleopGamePieceCount", UNSET)

        teleop_game_piece_points = d.pop("teleopGamePiecePoints", UNSET)

        total_charge_station_points = d.pop("totalChargeStationPoints", UNSET)

        match_score_breakdown_2023_alliance = cls(
            auto_mobility_points=auto_mobility_points,
            mobility_robot_1=mobility_robot_1,
            mobility_robot_2=mobility_robot_2,
            mobility_robot_3=mobility_robot_3,
            auto_points=auto_points,
            foul_count=foul_count,
            foul_points=foul_points,
            tech_foul_count=tech_foul_count,
            teleop_points=teleop_points,
            rp=rp,
            total_points=total_points,
            activation_bonus_achieved=activation_bonus_achieved,
            adjust_points=adjust_points,
            auto_bridge_state=auto_bridge_state,
            auto_charge_station_points=auto_charge_station_points,
            auto_charge_station_robot_1=auto_charge_station_robot_1,
            auto_charge_station_robot_2=auto_charge_station_robot_2,
            auto_charge_station_robot_3=auto_charge_station_robot_3,
            auto_docked=auto_docked,
            auto_community=auto_community,
            auto_game_piece_count=auto_game_piece_count,
            auto_game_piece_points=auto_game_piece_points,
            coop_game_piece_count=coop_game_piece_count,
            coopertition_criteria_met=coopertition_criteria_met,
            end_game_bridge_state=end_game_bridge_state,
            end_game_charge_station_points=end_game_charge_station_points,
            end_game_charge_station_robot_1=end_game_charge_station_robot_1,
            end_game_charge_station_robot_2=end_game_charge_station_robot_2,
            end_game_charge_station_robot_3=end_game_charge_station_robot_3,
            end_game_park_points=end_game_park_points,
            extra_game_piece_count=extra_game_piece_count,
            link_points=link_points,
            links=links,
            sustainability_bonus_achieved=sustainability_bonus_achieved,
            teleop_community=teleop_community,
            teleop_game_piece_count=teleop_game_piece_count,
            teleop_game_piece_points=teleop_game_piece_points,
            total_charge_station_points=total_charge_station_points,
        )

        match_score_breakdown_2023_alliance.additional_properties = d
        return match_score_breakdown_2023_alliance

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
