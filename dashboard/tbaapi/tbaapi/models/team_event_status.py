from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_event_status_alliance import TeamEventStatusAlliance
    from ..models.team_event_status_playoff_type_1 import TeamEventStatusPlayoffType1
    from ..models.team_event_status_rank import TeamEventStatusRank


T = TypeVar("T", bound="TeamEventStatus")


@_attrs_define
class TeamEventStatus:
    """
    Attributes:
        qual (None | TeamEventStatusRank | Unset):
        alliance (None | TeamEventStatusAlliance | Unset):
        playoff (None | TeamEventStatusPlayoffType1 | Unset):
        alliance_status_str (str | Unset): An HTML formatted string suitable for display to the user containing the
            team's alliance pick status.
        playoff_status_str (str | Unset): An HTML formatter string suitable for display to the user containing the
            team's playoff status.
        overall_status_str (str | Unset): An HTML formatted string suitable for display to the user containing the
            team's overall status summary of the event.
        next_match_key (None | str | Unset): TBA match key for the next match the team is scheduled to play in at this
            event, or null.
        last_match_key (None | str | Unset): TBA match key for the last match the team played in at this event, or null.
        pit_location (None | str | Unset): The pit location for the team at this event, or null if not available.
    """

    qual: None | TeamEventStatusRank | Unset = UNSET
    alliance: None | TeamEventStatusAlliance | Unset = UNSET
    playoff: None | TeamEventStatusPlayoffType1 | Unset = UNSET
    alliance_status_str: str | Unset = UNSET
    playoff_status_str: str | Unset = UNSET
    overall_status_str: str | Unset = UNSET
    next_match_key: None | str | Unset = UNSET
    last_match_key: None | str | Unset = UNSET
    pit_location: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_event_status_alliance import TeamEventStatusAlliance
        from ..models.team_event_status_playoff_type_1 import TeamEventStatusPlayoffType1
        from ..models.team_event_status_rank import TeamEventStatusRank

        qual: dict[str, Any] | None | Unset
        if isinstance(self.qual, Unset):
            qual = UNSET
        elif isinstance(self.qual, TeamEventStatusRank):
            qual = self.qual.to_dict()
        else:
            qual = self.qual

        alliance: dict[str, Any] | None | Unset
        if isinstance(self.alliance, Unset):
            alliance = UNSET
        elif isinstance(self.alliance, TeamEventStatusAlliance):
            alliance = self.alliance.to_dict()
        else:
            alliance = self.alliance

        playoff: dict[str, Any] | None | Unset
        if isinstance(self.playoff, Unset):
            playoff = UNSET
        elif isinstance(self.playoff, TeamEventStatusPlayoffType1):
            playoff = self.playoff.to_dict()
        else:
            playoff = self.playoff

        alliance_status_str = self.alliance_status_str

        playoff_status_str = self.playoff_status_str

        overall_status_str = self.overall_status_str

        next_match_key: None | str | Unset
        if isinstance(self.next_match_key, Unset):
            next_match_key = UNSET
        else:
            next_match_key = self.next_match_key

        last_match_key: None | str | Unset
        if isinstance(self.last_match_key, Unset):
            last_match_key = UNSET
        else:
            last_match_key = self.last_match_key

        pit_location: None | str | Unset
        if isinstance(self.pit_location, Unset):
            pit_location = UNSET
        else:
            pit_location = self.pit_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qual is not UNSET:
            field_dict["qual"] = qual
        if alliance is not UNSET:
            field_dict["alliance"] = alliance
        if playoff is not UNSET:
            field_dict["playoff"] = playoff
        if alliance_status_str is not UNSET:
            field_dict["alliance_status_str"] = alliance_status_str
        if playoff_status_str is not UNSET:
            field_dict["playoff_status_str"] = playoff_status_str
        if overall_status_str is not UNSET:
            field_dict["overall_status_str"] = overall_status_str
        if next_match_key is not UNSET:
            field_dict["next_match_key"] = next_match_key
        if last_match_key is not UNSET:
            field_dict["last_match_key"] = last_match_key
        if pit_location is not UNSET:
            field_dict["pit_location"] = pit_location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_event_status_alliance import TeamEventStatusAlliance
        from ..models.team_event_status_playoff_type_1 import TeamEventStatusPlayoffType1
        from ..models.team_event_status_rank import TeamEventStatusRank

        d = dict(src_dict)

        def _parse_qual(data: object) -> None | TeamEventStatusRank | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qual_type_0 = TeamEventStatusRank.from_dict(data)

                return qual_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamEventStatusRank | Unset, data)

        qual = _parse_qual(d.pop("qual", UNSET))

        def _parse_alliance(data: object) -> None | TeamEventStatusAlliance | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alliance_type_0 = TeamEventStatusAlliance.from_dict(data)

                return alliance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamEventStatusAlliance | Unset, data)

        alliance = _parse_alliance(d.pop("alliance", UNSET))

        def _parse_playoff(data: object) -> None | TeamEventStatusPlayoffType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_team_event_status_playoff_type_1 = TeamEventStatusPlayoffType1.from_dict(data)

                return componentsschemas_team_event_status_playoff_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamEventStatusPlayoffType1 | Unset, data)

        playoff = _parse_playoff(d.pop("playoff", UNSET))

        alliance_status_str = d.pop("alliance_status_str", UNSET)

        playoff_status_str = d.pop("playoff_status_str", UNSET)

        overall_status_str = d.pop("overall_status_str", UNSET)

        def _parse_next_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        next_match_key = _parse_next_match_key(d.pop("next_match_key", UNSET))

        def _parse_last_match_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_match_key = _parse_last_match_key(d.pop("last_match_key", UNSET))

        def _parse_pit_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pit_location = _parse_pit_location(d.pop("pit_location", UNSET))

        team_event_status = cls(
            qual=qual,
            alliance=alliance,
            playoff=playoff,
            alliance_status_str=alliance_status_str,
            playoff_status_str=playoff_status_str,
            overall_status_str=overall_status_str,
            next_match_key=next_match_key,
            last_match_key=last_match_key,
            pit_location=pit_location,
        )

        team_event_status.additional_properties = d
        return team_event_status

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
