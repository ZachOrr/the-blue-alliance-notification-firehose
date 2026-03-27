from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_event_status import TeamEventStatus


T = TypeVar("T", bound="GetEventTeamsStatusesResponse200")


@_attrs_define
class GetEventTeamsStatusesResponse200:
    """A key-value pair of `Team_Event_Status` objects with the event key as the key."""

    additional_properties: dict[str, None | TeamEventStatus] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_event_status import TeamEventStatus

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, TeamEventStatus):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_event_status import TeamEventStatus

        d = dict(src_dict)
        get_event_teams_statuses_response_200 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> None | TeamEventStatus:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = TeamEventStatus.from_dict(data)

                    return additional_property_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(None | TeamEventStatus, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_event_teams_statuses_response_200.additional_properties = additional_properties
        return get_event_teams_statuses_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> None | TeamEventStatus:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: None | TeamEventStatus) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
