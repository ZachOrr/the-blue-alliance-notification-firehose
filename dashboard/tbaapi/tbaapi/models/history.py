from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.award import Award
    from ..models.event import Event


T = TypeVar("T", bound="History")


@_attrs_define
class History:
    """
    Attributes:
        events (list[Event]):
        awards (list[Award]):
    """

    events: list[Event]
    awards: list[Award]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        awards = []
        for awards_item_data in self.awards:
            awards_item = awards_item_data.to_dict()
            awards.append(awards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "events": events,
                "awards": awards,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.award import Award
        from ..models.event import Event

        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        awards = []
        _awards = d.pop("awards")
        for awards_item_data in _awards:
            awards_item = Award.from_dict(awards_item_data)

            awards.append(awards_item)

        history = cls(
            events=events,
            awards=awards,
        )

        history.additional_properties = d
        return history

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
