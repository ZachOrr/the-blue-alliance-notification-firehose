from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comp_level import CompLevel
from ..models.match_simple_winning_alliance import MatchSimpleWinningAlliance

if TYPE_CHECKING:
    from ..models.match_simple_alliances import MatchSimpleAlliances


T = TypeVar("T", bound="MatchSimple")


@_attrs_define
class MatchSimple:
    """
    Attributes:
        key (str): TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the
            year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER`
            is the match number in the competition level. A set number may append the competition level if more than one
            match in required per set.
        comp_level (CompLevel): The competition level the match was played at.
        set_number (int): The set number in a series of matches where more than one match is required in the match
            series.
        match_number (int): The match number of the match in the competition level.
        alliances (MatchSimpleAlliances): A list of alliances, the teams on the alliances, and their score.
        winning_alliance (MatchSimpleWinningAlliance): The color (red/blue) of the winning alliance. Will contain an
            empty string in the event of no winner, or a tie.
        event_key (str): Event key of the event the match was played at.
        time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from
            the published schedule.
        predicted_time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start
            time.
        actual_time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.
    """

    key: str
    comp_level: CompLevel
    set_number: int
    match_number: int
    alliances: MatchSimpleAlliances
    winning_alliance: MatchSimpleWinningAlliance
    event_key: str
    time: int | None
    predicted_time: int | None
    actual_time: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        comp_level = self.comp_level.value

        set_number = self.set_number

        match_number = self.match_number

        alliances = self.alliances.to_dict()

        winning_alliance = self.winning_alliance.value

        event_key = self.event_key

        time: int | None
        time = self.time

        predicted_time: int | None
        predicted_time = self.predicted_time

        actual_time: int | None
        actual_time = self.actual_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "comp_level": comp_level,
                "set_number": set_number,
                "match_number": match_number,
                "alliances": alliances,
                "winning_alliance": winning_alliance,
                "event_key": event_key,
                "time": time,
                "predicted_time": predicted_time,
                "actual_time": actual_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_simple_alliances import MatchSimpleAlliances

        d = dict(src_dict)
        key = d.pop("key")

        comp_level = CompLevel(d.pop("comp_level"))

        set_number = d.pop("set_number")

        match_number = d.pop("match_number")

        alliances = MatchSimpleAlliances.from_dict(d.pop("alliances"))

        winning_alliance = MatchSimpleWinningAlliance(d.pop("winning_alliance"))

        event_key = d.pop("event_key")

        def _parse_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        time = _parse_time(d.pop("time"))

        def _parse_predicted_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        predicted_time = _parse_predicted_time(d.pop("predicted_time"))

        def _parse_actual_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        actual_time = _parse_actual_time(d.pop("actual_time"))

        match_simple = cls(
            key=key,
            comp_level=comp_level,
            set_number=set_number,
            match_number=match_number,
            alliances=alliances,
            winning_alliance=winning_alliance,
            event_key=event_key,
            time=time,
            predicted_time=predicted_time,
            actual_time=actual_time,
        )

        match_simple.additional_properties = d
        return match_simple

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
