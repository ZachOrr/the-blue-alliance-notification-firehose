from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TeamSimple")


@_attrs_define
class TeamSimple:
    """
    Attributes:
        key (str): TBA team key with the format `frcXXXX` with `XXXX` representing the team number.
        team_number (int): Official team number issued by FIRST.
        nickname (str): Team nickname provided by FIRST.
        name (str): Official long name registered with FIRST.
        city (None | str): City of team derived from parsing the address registered with FIRST.
        state_prov (None | str): State of team derived from parsing the address registered with FIRST.
        country (None | str): Country of team derived from parsing the address registered with FIRST.
    """

    key: str
    team_number: int
    nickname: str
    name: str
    city: None | str
    state_prov: None | str
    country: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        team_number = self.team_number

        nickname = self.nickname

        name = self.name

        city: None | str
        city = self.city

        state_prov: None | str
        state_prov = self.state_prov

        country: None | str
        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "team_number": team_number,
                "nickname": nickname,
                "name": name,
                "city": city,
                "state_prov": state_prov,
                "country": country,
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

        team_simple = cls(
            key=key,
            team_number=team_number,
            nickname=nickname,
            name=name,
            city=city,
            state_prov=state_prov,
            country=country,
        )

        team_simple.additional_properties = d
        return team_simple

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
