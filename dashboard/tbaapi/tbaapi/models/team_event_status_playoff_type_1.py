from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comp_level import CompLevel
from ..models.team_event_status_playoff_type_1_status import TeamEventStatusPlayoffType1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wlt_record import WLTRecord


T = TypeVar("T", bound="TeamEventStatusPlayoffType1")


@_attrs_define
class TeamEventStatusPlayoffType1:
    """Playoff status for this team, may be null if the team did not make playoffs, or playoffs have not begun.

    Attributes:
        level (CompLevel | Unset): The competition level the match was played at.
        current_level_record (None | Unset | WLTRecord):
        record (None | Unset | WLTRecord):
        status (TeamEventStatusPlayoffType1Status | Unset): Current competition status for the playoffs.
        playoff_average (float | None | Unset): The average match score during playoffs. Year specific. May be null if
            not relevant for a given year.
    """

    level: CompLevel | Unset = UNSET
    current_level_record: None | Unset | WLTRecord = UNSET
    record: None | Unset | WLTRecord = UNSET
    status: TeamEventStatusPlayoffType1Status | Unset = UNSET
    playoff_average: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wlt_record import WLTRecord

        level: str | Unset = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        current_level_record: dict[str, Any] | None | Unset
        if isinstance(self.current_level_record, Unset):
            current_level_record = UNSET
        elif isinstance(self.current_level_record, WLTRecord):
            current_level_record = self.current_level_record.to_dict()
        else:
            current_level_record = self.current_level_record

        record: dict[str, Any] | None | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        elif isinstance(self.record, WLTRecord):
            record = self.record.to_dict()
        else:
            record = self.record

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        playoff_average: float | None | Unset
        if isinstance(self.playoff_average, Unset):
            playoff_average = UNSET
        else:
            playoff_average = self.playoff_average

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if current_level_record is not UNSET:
            field_dict["current_level_record"] = current_level_record
        if record is not UNSET:
            field_dict["record"] = record
        if status is not UNSET:
            field_dict["status"] = status
        if playoff_average is not UNSET:
            field_dict["playoff_average"] = playoff_average

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wlt_record import WLTRecord

        d = dict(src_dict)
        _level = d.pop("level", UNSET)
        level: CompLevel | Unset
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = CompLevel(_level)

        def _parse_current_level_record(data: object) -> None | Unset | WLTRecord:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_level_record_type_0 = WLTRecord.from_dict(data)

                return current_level_record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WLTRecord, data)

        current_level_record = _parse_current_level_record(d.pop("current_level_record", UNSET))

        def _parse_record(data: object) -> None | Unset | WLTRecord:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = WLTRecord.from_dict(data)

                return record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WLTRecord, data)

        record = _parse_record(d.pop("record", UNSET))

        _status = d.pop("status", UNSET)
        status: TeamEventStatusPlayoffType1Status | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TeamEventStatusPlayoffType1Status(_status)

        def _parse_playoff_average(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        playoff_average = _parse_playoff_average(d.pop("playoff_average", UNSET))

        team_event_status_playoff_type_1 = cls(
            level=level,
            current_level_record=current_level_record,
            record=record,
            status=status,
            playoff_average=playoff_average,
        )

        team_event_status_playoff_type_1.additional_properties = d
        return team_event_status_playoff_type_1

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
