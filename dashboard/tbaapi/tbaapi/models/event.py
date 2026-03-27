from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.district import District
    from ..models.event_remap_teams_type_0 import EventRemapTeamsType0
    from ..models.webcast import Webcast


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
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
        short_name (None | str): Same as `name` but doesn't include event specifiers, such as 'Regional' or 'District'.
            May be null.
        event_type_string (str): Event Type, eg Regional, District, or Offseason.
        week (int | None): Week of the event relative to the first official season event, zero-indexed. Only valid for
            Regionals, Districts, and District Championships. Null otherwise. (Eg. A season with a week 0 'preseason' event
            does not count, and week 1 events will show 0 here. Seasons with a week 0.5 regional event will show week 0 for
            those event(s) and week 1 for week 1 events and so on.)
        address (None | str): Address of the event's venue, if available.
        postal_code (None | str): Postal code from the event address.
        gmaps_place_id (None | str): Google Maps Place ID for the event address. Will be NULL, for future development.
        gmaps_url (None | str): Link to address location on Google Maps. Will be NULL, for future development.
        lat (float | None): Latitude for the event address. Will be NULL, for future development.
        lng (float | None): Longitude for the event address. Will be NULL, for future development.
        location_name (None | str): Name of the location at the address for the event, eg. Blue Alliance High School.
        timezone (None | str): IANA Timezone identifier.
        website (None | str): The event's website, if any.
        first_event_id (None | str): The FIRST internal Event ID, used to link to the event on the FRC webpage.
        first_event_code (None | str): Public facing event code used by FIRST (on frc-events.firstinspires.org, for
            example)
        webcasts (list[Webcast]):
        division_keys (list[str]): An array of event keys for the divisions at this event.
        parent_event_key (None | str): The TBA Event key that represents the event's parent. Used to link back to the
            event from a division event. It is also the inverse relation of `divison_keys`.
        playoff_type (int | None): Playoff Type, as defined under `PlayoffType`: https://github.com/the-blue-
            alliance/the-blue-alliance/blob/main/src/backend/common/consts/playoff_type.py#L37, or null.
        playoff_type_string (None | str): String representation of the `playoff_type`, or null.
        remap_teams (EventRemapTeamsType0 | None): Map of temporary "off-season demo" team numbers to pre-rookie and B
            teams. Both keys and values are team keys in the format 'frc####'. Key is the old team key ('frc' + numeric
            only), value is the new team key ('frc' + numeric + may include a letter suffix).
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
    short_name: None | str
    event_type_string: str
    week: int | None
    address: None | str
    postal_code: None | str
    gmaps_place_id: None | str
    gmaps_url: None | str
    lat: float | None
    lng: float | None
    location_name: None | str
    timezone: None | str
    website: None | str
    first_event_id: None | str
    first_event_code: None | str
    webcasts: list[Webcast]
    division_keys: list[str]
    parent_event_key: None | str
    playoff_type: int | None
    playoff_type_string: None | str
    remap_teams: EventRemapTeamsType0 | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.district import District
        from ..models.event_remap_teams_type_0 import EventRemapTeamsType0

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

        short_name: None | str
        short_name = self.short_name

        event_type_string = self.event_type_string

        week: int | None
        week = self.week

        address: None | str
        address = self.address

        postal_code: None | str
        postal_code = self.postal_code

        gmaps_place_id: None | str
        gmaps_place_id = self.gmaps_place_id

        gmaps_url: None | str
        gmaps_url = self.gmaps_url

        lat: float | None
        lat = self.lat

        lng: float | None
        lng = self.lng

        location_name: None | str
        location_name = self.location_name

        timezone: None | str
        timezone = self.timezone

        website: None | str
        website = self.website

        first_event_id: None | str
        first_event_id = self.first_event_id

        first_event_code: None | str
        first_event_code = self.first_event_code

        webcasts = []
        for webcasts_item_data in self.webcasts:
            webcasts_item = webcasts_item_data.to_dict()
            webcasts.append(webcasts_item)

        division_keys = self.division_keys

        parent_event_key: None | str
        parent_event_key = self.parent_event_key

        playoff_type: int | None
        playoff_type = self.playoff_type

        playoff_type_string: None | str
        playoff_type_string = self.playoff_type_string

        remap_teams: dict[str, Any] | None
        if isinstance(self.remap_teams, EventRemapTeamsType0):
            remap_teams = self.remap_teams.to_dict()
        else:
            remap_teams = self.remap_teams

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
                "short_name": short_name,
                "event_type_string": event_type_string,
                "week": week,
                "address": address,
                "postal_code": postal_code,
                "gmaps_place_id": gmaps_place_id,
                "gmaps_url": gmaps_url,
                "lat": lat,
                "lng": lng,
                "location_name": location_name,
                "timezone": timezone,
                "website": website,
                "first_event_id": first_event_id,
                "first_event_code": first_event_code,
                "webcasts": webcasts,
                "division_keys": division_keys,
                "parent_event_key": parent_event_key,
                "playoff_type": playoff_type,
                "playoff_type_string": playoff_type_string,
                "remap_teams": remap_teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district import District
        from ..models.event_remap_teams_type_0 import EventRemapTeamsType0
        from ..models.webcast import Webcast

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

        def _parse_short_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        short_name = _parse_short_name(d.pop("short_name"))

        event_type_string = d.pop("event_type_string")

        def _parse_week(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        week = _parse_week(d.pop("week"))

        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))

        def _parse_postal_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        postal_code = _parse_postal_code(d.pop("postal_code"))

        def _parse_gmaps_place_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gmaps_place_id = _parse_gmaps_place_id(d.pop("gmaps_place_id"))

        def _parse_gmaps_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gmaps_url = _parse_gmaps_url(d.pop("gmaps_url"))

        def _parse_lat(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lat = _parse_lat(d.pop("lat"))

        def _parse_lng(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        lng = _parse_lng(d.pop("lng"))

        def _parse_location_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        location_name = _parse_location_name(d.pop("location_name"))

        def _parse_timezone(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        timezone = _parse_timezone(d.pop("timezone"))

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        def _parse_first_event_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_event_id = _parse_first_event_id(d.pop("first_event_id"))

        def _parse_first_event_code(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_event_code = _parse_first_event_code(d.pop("first_event_code"))

        webcasts = []
        _webcasts = d.pop("webcasts")
        for webcasts_item_data in _webcasts:
            webcasts_item = Webcast.from_dict(webcasts_item_data)

            webcasts.append(webcasts_item)

        division_keys = cast(list[str], d.pop("division_keys"))

        def _parse_parent_event_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        parent_event_key = _parse_parent_event_key(d.pop("parent_event_key"))

        def _parse_playoff_type(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        playoff_type = _parse_playoff_type(d.pop("playoff_type"))

        def _parse_playoff_type_string(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        playoff_type_string = _parse_playoff_type_string(d.pop("playoff_type_string"))

        def _parse_remap_teams(data: object) -> EventRemapTeamsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                remap_teams_type_0 = EventRemapTeamsType0.from_dict(data)

                return remap_teams_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventRemapTeamsType0 | None, data)

        remap_teams = _parse_remap_teams(d.pop("remap_teams"))

        event = cls(
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
            short_name=short_name,
            event_type_string=event_type_string,
            week=week,
            address=address,
            postal_code=postal_code,
            gmaps_place_id=gmaps_place_id,
            gmaps_url=gmaps_url,
            lat=lat,
            lng=lng,
            location_name=location_name,
            timezone=timezone,
            website=website,
            first_event_id=first_event_id,
            first_event_code=first_event_code,
            webcasts=webcasts,
            division_keys=division_keys,
            parent_event_key=parent_event_key,
            playoff_type=playoff_type,
            playoff_type_string=playoff_type_string,
            remap_teams=remap_teams,
        )

        event.additional_properties = d
        return event

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
