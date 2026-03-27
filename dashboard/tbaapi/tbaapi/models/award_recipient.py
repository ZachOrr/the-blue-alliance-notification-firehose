from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AwardRecipient")


@_attrs_define
class AwardRecipient:
    """An `Award_Recipient` object represents the team and/or person who received an award at an event.

    Attributes:
        team_key (None | str): The TBA team key for the team that was given the award. May be null.
        awardee (None | str): The name of the individual given the award. May be null.
    """

    team_key: None | str
    awardee: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_key: None | str
        team_key = self.team_key

        awardee: None | str
        awardee = self.awardee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_key": team_key,
                "awardee": awardee,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_team_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        team_key = _parse_team_key(d.pop("team_key"))

        def _parse_awardee(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        awardee = _parse_awardee(d.pop("awardee"))

        award_recipient = cls(
            team_key=team_key,
            awardee=awardee,
        )

        award_recipient.additional_properties = d
        return award_recipient

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
