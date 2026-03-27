from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wlt_record import WLTRecord


T = TypeVar("T", bound="DistrictInsightTeamDataType0AdditionalProperty")


@_attrs_define
class DistrictInsightTeamDataType0AdditionalProperty:
    """
    Attributes:
        district_seasons (int):
        total_district_points (int):
        total_pre_dcmp_district_points (int):
        district_event_wins (int):
        dcmp_wins (int):
        team_awards (int):
        individual_awards (int):
        quals_record (WLTRecord): A Win-Loss-Tie record for a team, or an alliance.
        elims_record (WLTRecord): A Win-Loss-Tie record for a team, or an alliance.
        in_district_extra_play_count (int):
        total_matches_played (int):
        dcmp_appearances (int):
        cmp_appearances (int):
    """

    district_seasons: int
    total_district_points: int
    total_pre_dcmp_district_points: int
    district_event_wins: int
    dcmp_wins: int
    team_awards: int
    individual_awards: int
    quals_record: WLTRecord
    elims_record: WLTRecord
    in_district_extra_play_count: int
    total_matches_played: int
    dcmp_appearances: int
    cmp_appearances: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_seasons = self.district_seasons

        total_district_points = self.total_district_points

        total_pre_dcmp_district_points = self.total_pre_dcmp_district_points

        district_event_wins = self.district_event_wins

        dcmp_wins = self.dcmp_wins

        team_awards = self.team_awards

        individual_awards = self.individual_awards

        quals_record = self.quals_record.to_dict()

        elims_record = self.elims_record.to_dict()

        in_district_extra_play_count = self.in_district_extra_play_count

        total_matches_played = self.total_matches_played

        dcmp_appearances = self.dcmp_appearances

        cmp_appearances = self.cmp_appearances

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "district_seasons": district_seasons,
                "total_district_points": total_district_points,
                "total_pre_dcmp_district_points": total_pre_dcmp_district_points,
                "district_event_wins": district_event_wins,
                "dcmp_wins": dcmp_wins,
                "team_awards": team_awards,
                "individual_awards": individual_awards,
                "quals_record": quals_record,
                "elims_record": elims_record,
                "in_district_extra_play_count": in_district_extra_play_count,
                "total_matches_played": total_matches_played,
                "dcmp_appearances": dcmp_appearances,
                "cmp_appearances": cmp_appearances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wlt_record import WLTRecord

        d = dict(src_dict)
        district_seasons = d.pop("district_seasons")

        total_district_points = d.pop("total_district_points")

        total_pre_dcmp_district_points = d.pop("total_pre_dcmp_district_points")

        district_event_wins = d.pop("district_event_wins")

        dcmp_wins = d.pop("dcmp_wins")

        team_awards = d.pop("team_awards")

        individual_awards = d.pop("individual_awards")

        quals_record = WLTRecord.from_dict(d.pop("quals_record"))

        elims_record = WLTRecord.from_dict(d.pop("elims_record"))

        in_district_extra_play_count = d.pop("in_district_extra_play_count")

        total_matches_played = d.pop("total_matches_played")

        dcmp_appearances = d.pop("dcmp_appearances")

        cmp_appearances = d.pop("cmp_appearances")

        district_insight_team_data_type_0_additional_property = cls(
            district_seasons=district_seasons,
            total_district_points=total_district_points,
            total_pre_dcmp_district_points=total_pre_dcmp_district_points,
            district_event_wins=district_event_wins,
            dcmp_wins=dcmp_wins,
            team_awards=team_awards,
            individual_awards=individual_awards,
            quals_record=quals_record,
            elims_record=elims_record,
            in_district_extra_play_count=in_district_extra_play_count,
            total_matches_played=total_matches_played,
            dcmp_appearances=dcmp_appearances,
            cmp_appearances=cmp_appearances,
        )

        district_insight_team_data_type_0_additional_property.additional_properties = d
        return district_insight_team_data_type_0_additional_property

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
