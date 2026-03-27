from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.district_insight_region_data_yearly_active_team_count import (
        DistrictInsightRegionDataYearlyActiveTeamCount,
    )
    from ..models.district_insight_region_data_yearly_event_count import DistrictInsightRegionDataYearlyEventCount
    from ..models.district_insight_region_data_yearly_gained_teams import DistrictInsightRegionDataYearlyGainedTeams
    from ..models.district_insight_region_data_yearly_lost_teams import DistrictInsightRegionDataYearlyLostTeams


T = TypeVar("T", bound="DistrictInsightRegionData")


@_attrs_define
class DistrictInsightRegionData:
    """
    Attributes:
        yearly_active_team_count (DistrictInsightRegionDataYearlyActiveTeamCount): Map of year to number of active teams
        yearly_event_count (DistrictInsightRegionDataYearlyEventCount): Map of year to number of events
        yearly_gained_teams (DistrictInsightRegionDataYearlyGainedTeams): Map of year to list of team keys gained
        yearly_lost_teams (DistrictInsightRegionDataYearlyLostTeams): Map of year to list of team keys lost
    """

    yearly_active_team_count: DistrictInsightRegionDataYearlyActiveTeamCount
    yearly_event_count: DistrictInsightRegionDataYearlyEventCount
    yearly_gained_teams: DistrictInsightRegionDataYearlyGainedTeams
    yearly_lost_teams: DistrictInsightRegionDataYearlyLostTeams
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yearly_active_team_count = self.yearly_active_team_count.to_dict()

        yearly_event_count = self.yearly_event_count.to_dict()

        yearly_gained_teams = self.yearly_gained_teams.to_dict()

        yearly_lost_teams = self.yearly_lost_teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yearly_active_team_count": yearly_active_team_count,
                "yearly_event_count": yearly_event_count,
                "yearly_gained_teams": yearly_gained_teams,
                "yearly_lost_teams": yearly_lost_teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_insight_region_data_yearly_active_team_count import (
            DistrictInsightRegionDataYearlyActiveTeamCount,
        )
        from ..models.district_insight_region_data_yearly_event_count import DistrictInsightRegionDataYearlyEventCount
        from ..models.district_insight_region_data_yearly_gained_teams import DistrictInsightRegionDataYearlyGainedTeams
        from ..models.district_insight_region_data_yearly_lost_teams import DistrictInsightRegionDataYearlyLostTeams

        d = dict(src_dict)
        yearly_active_team_count = DistrictInsightRegionDataYearlyActiveTeamCount.from_dict(
            d.pop("yearly_active_team_count")
        )

        yearly_event_count = DistrictInsightRegionDataYearlyEventCount.from_dict(d.pop("yearly_event_count"))

        yearly_gained_teams = DistrictInsightRegionDataYearlyGainedTeams.from_dict(d.pop("yearly_gained_teams"))

        yearly_lost_teams = DistrictInsightRegionDataYearlyLostTeams.from_dict(d.pop("yearly_lost_teams"))

        district_insight_region_data = cls(
            yearly_active_team_count=yearly_active_team_count,
            yearly_event_count=yearly_event_count,
            yearly_gained_teams=yearly_gained_teams,
            yearly_lost_teams=yearly_lost_teams,
        )

        district_insight_region_data.additional_properties = d
        return district_insight_region_data

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
