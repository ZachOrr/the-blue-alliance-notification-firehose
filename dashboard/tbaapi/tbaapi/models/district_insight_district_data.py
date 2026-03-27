from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.district_insight_district_data_region_data_type_0 import DistrictInsightDistrictDataRegionDataType0
    from ..models.district_insight_region_data import DistrictInsightRegionData


T = TypeVar("T", bound="DistrictInsightDistrictData")


@_attrs_define
class DistrictInsightDistrictData:
    """
    Attributes:
        region_data (DistrictInsightDistrictDataRegionDataType0 | None):
        district_wide_data (DistrictInsightRegionData | None):
    """

    region_data: DistrictInsightDistrictDataRegionDataType0 | None
    district_wide_data: DistrictInsightRegionData | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.district_insight_district_data_region_data_type_0 import (
            DistrictInsightDistrictDataRegionDataType0,
        )
        from ..models.district_insight_region_data import DistrictInsightRegionData

        region_data: dict[str, Any] | None
        if isinstance(self.region_data, DistrictInsightDistrictDataRegionDataType0):
            region_data = self.region_data.to_dict()
        else:
            region_data = self.region_data

        district_wide_data: dict[str, Any] | None
        if isinstance(self.district_wide_data, DistrictInsightRegionData):
            district_wide_data = self.district_wide_data.to_dict()
        else:
            district_wide_data = self.district_wide_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_data": region_data,
                "district_wide_data": district_wide_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_insight_district_data_region_data_type_0 import (
            DistrictInsightDistrictDataRegionDataType0,
        )
        from ..models.district_insight_region_data import DistrictInsightRegionData

        d = dict(src_dict)

        def _parse_region_data(data: object) -> DistrictInsightDistrictDataRegionDataType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                region_data_type_0 = DistrictInsightDistrictDataRegionDataType0.from_dict(data)

                return region_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DistrictInsightDistrictDataRegionDataType0 | None, data)

        region_data = _parse_region_data(d.pop("region_data"))

        def _parse_district_wide_data(data: object) -> DistrictInsightRegionData | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                district_wide_data_type_0 = DistrictInsightRegionData.from_dict(data)

                return district_wide_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DistrictInsightRegionData | None, data)

        district_wide_data = _parse_district_wide_data(d.pop("district_wide_data"))

        district_insight_district_data = cls(
            region_data=region_data,
            district_wide_data=district_wide_data,
        )

        district_insight_district_data.additional_properties = d
        return district_insight_district_data

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
