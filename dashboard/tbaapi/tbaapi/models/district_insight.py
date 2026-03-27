from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.district_insight_district_data import DistrictInsightDistrictData
    from ..models.district_insight_team_data_type_0 import DistrictInsightTeamDataType0


T = TypeVar("T", bound="DistrictInsight")


@_attrs_define
class DistrictInsight:
    """
    Attributes:
        district_data (DistrictInsightDistrictData):
        team_data (DistrictInsightTeamDataType0 | None):
    """

    district_data: DistrictInsightDistrictData
    team_data: DistrictInsightTeamDataType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.district_insight_team_data_type_0 import DistrictInsightTeamDataType0

        district_data = self.district_data.to_dict()

        team_data: dict[str, Any] | None
        if isinstance(self.team_data, DistrictInsightTeamDataType0):
            team_data = self.team_data.to_dict()
        else:
            team_data = self.team_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "district_data": district_data,
                "team_data": team_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_insight_district_data import DistrictInsightDistrictData
        from ..models.district_insight_team_data_type_0 import DistrictInsightTeamDataType0

        d = dict(src_dict)
        district_data = DistrictInsightDistrictData.from_dict(d.pop("district_data"))

        def _parse_team_data(data: object) -> DistrictInsightTeamDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                team_data_type_0 = DistrictInsightTeamDataType0.from_dict(data)

                return team_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DistrictInsightTeamDataType0 | None, data)

        team_data = _parse_team_data(d.pop("team_data"))

        district_insight = cls(
            district_data=district_data,
            team_data=team_data,
        )

        district_insight.additional_properties = d
        return district_insight

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
