from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        key (str): TBA team key with the format `frcXXXX` with `XXXX` representing the team number.
        team_number (int): Official team number issued by FIRST.
        nickname (str): Team nickname provided by FIRST.
        name (str): Official long name registered with FIRST.
        school_name (None | str): Name of team school or affilited group registered with FIRST.
        city (None | str): City of team derived from parsing the address registered with FIRST.
        state_prov (None | str): State of team derived from parsing the address registered with FIRST.
        country (None | str): Country of team derived from parsing the address registered with FIRST.
        address (None | str): Will be NULL, for future development.
        postal_code (None | str): Postal code from the team address.
        gmaps_place_id (None | str): Will be NULL, for future development.
        gmaps_url (None | str): Will be NULL, for future development.
        lat (float | None): Will be NULL, for future development.
        lng (float | None): Will be NULL, for future development.
        location_name (None | str): Will be NULL, for future development.
        website (None | str): Official website associated with the team.
        rookie_year (int | None): First year the team officially competed.
        motto (None | str): Team's motto or tagline.
    """

    key: str
    team_number: int
    nickname: str
    name: str
    school_name: None | str
    city: None | str
    state_prov: None | str
    country: None | str
    address: None | str
    postal_code: None | str
    gmaps_place_id: None | str
    gmaps_url: None | str
    lat: float | None
    lng: float | None
    location_name: None | str
    website: None | str
    rookie_year: int | None
    motto: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        team_number = self.team_number

        nickname = self.nickname

        name = self.name

        school_name: None | str
        school_name = self.school_name

        city: None | str
        city = self.city

        state_prov: None | str
        state_prov = self.state_prov

        country: None | str
        country = self.country

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

        website: None | str
        website = self.website

        rookie_year: int | None
        rookie_year = self.rookie_year

        motto: None | str
        motto = self.motto

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "team_number": team_number,
                "nickname": nickname,
                "name": name,
                "school_name": school_name,
                "city": city,
                "state_prov": state_prov,
                "country": country,
                "address": address,
                "postal_code": postal_code,
                "gmaps_place_id": gmaps_place_id,
                "gmaps_url": gmaps_url,
                "lat": lat,
                "lng": lng,
                "location_name": location_name,
                "website": website,
                "rookie_year": rookie_year,
                "motto": motto,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        team_number = d.pop("team_number")

        nickname = d.pop("nickname")

        name = d.pop("name")

        def _parse_school_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        school_name = _parse_school_name(d.pop("school_name"))

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

        def _parse_website(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        website = _parse_website(d.pop("website"))

        def _parse_rookie_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        rookie_year = _parse_rookie_year(d.pop("rookie_year"))

        def _parse_motto(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        motto = _parse_motto(d.pop("motto"))

        team = cls(
            key=key,
            team_number=team_number,
            nickname=nickname,
            name=name,
            school_name=school_name,
            city=city,
            state_prov=state_prov,
            country=country,
            address=address,
            postal_code=postal_code,
            gmaps_place_id=gmaps_place_id,
            gmaps_url=gmaps_url,
            lat=lat,
            lng=lng,
            location_name=location_name,
            website=website,
            rookie_year=rookie_year,
            motto=motto,
        )

        team.additional_properties = d
        return team

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
