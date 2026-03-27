from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.district import District


T = TypeVar("T", bound="EventSimple")


@_attrs_define
class EventSimple:
    """
    Attributes:
        key (str): TBA event key with the format yyyy[EVENT_CODE], where yyyy is the year, and EVENT_CODE is the event
            code of the event.
        name (str): Official name of event on record either provided by FIRST or organizers of offseason event.
        event_code (str): Event short code, as provided by FIRST.
        event_type (int): Event Type, as defined here: https://github.com/the-blue-alliance/the-blue-
            alliance/blob/main/src/backend/common/consts/event_type.py#L8
        district (District | None):
        city (None | str): City, town, village, etc. the event is located in.
        state_prov (None | str): State or Province the event is located in.
        country (None | str): Country the event is located in.
        start_date (datetime.date): Event start date in `yyyy-mm-dd` format.
        end_date (datetime.date): Event end date in `yyyy-mm-dd` format.
        year (int): Year the event data is for.
    """

    key: str
    name: str
    event_code: str
    event_type: int
    district: District | None
    city: None | str
    state_prov: None | str
    country: None | str
    start_date: datetime.date
    end_date: datetime.date
    year: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.district import District

        key = self.key

        name = self.name

        event_code = self.event_code

        event_type = self.event_type

        district: dict[str, Any] | None
        if isinstance(self.district, District):
            district = self.district.to_dict()
        else:
            district = self.district

        city: None | str
        city = self.city

        state_prov: None | str
        state_prov = self.state_prov

        country: None | str
        country = self.country

        start_date = self.start_date.isoformat()

        end_date = self.end_date.isoformat()

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "name": name,
                "event_code": event_code,
                "event_type": event_type,
                "district": district,
                "city": city,
                "state_prov": state_prov,
                "country": country,
                "start_date": start_date,
                "end_date": end_date,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district import District

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        event_code = d.pop("event_code")

        event_type = d.pop("event_type")

        def _parse_district(data: object) -> District | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                district_type_0 = District.from_dict(data)

                return district_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(District | None, data)

        district = _parse_district(d.pop("district"))

        def _parse_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        city = _parse_city(d.pop("city"))

        def _parse_state_prov(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        state_prov = _parse_state_prov(d.pop("state_prov"))

        def _parse_country(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        country = _parse_country(d.pop("country"))

        start_date = isoparse(d.pop("start_date")).date()

        end_date = isoparse(d.pop("end_date")).date()

        year = d.pop("year")

        event_simple = cls(
            key=key,
            name=name,
            event_code=event_code,
            event_type=event_type,
            district=district,
            city=city,
            state_prov=state_prov,
            country=country,
            start_date=start_date,
            end_date=end_date,
            year=year,
        )

        event_simple.additional_properties = d
        return event_simple

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
