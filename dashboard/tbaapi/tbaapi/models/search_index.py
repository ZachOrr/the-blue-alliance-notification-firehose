from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_index_events_item import SearchIndexEventsItem
    from ..models.search_index_teams_item import SearchIndexTeamsItem


T = TypeVar("T", bound="SearchIndex")


@_attrs_define
class SearchIndex:
    """
    Attributes:
        teams (list[SearchIndexTeamsItem]):
        events (list[SearchIndexEventsItem]):
    """

    teams: list[SearchIndexTeamsItem]
    events: list[SearchIndexEventsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "teams": teams,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_index_events_item import SearchIndexEventsItem
        from ..models.search_index_teams_item import SearchIndexTeamsItem

        d = dict(src_dict)
        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = SearchIndexTeamsItem.from_dict(teams_item_data)

            teams.append(teams_item)

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = SearchIndexEventsItem.from_dict(events_item_data)

            events.append(events_item)

        search_index = cls(
            teams=teams,
            events=events,
        )

        search_index.additional_properties = d
        return search_index

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
