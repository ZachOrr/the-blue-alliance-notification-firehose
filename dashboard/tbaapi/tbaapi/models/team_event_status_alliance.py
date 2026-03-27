from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_event_status_alliance_backup_type_1 import TeamEventStatusAllianceBackupType1


T = TypeVar("T", bound="TeamEventStatusAlliance")


@_attrs_define
class TeamEventStatusAlliance:
    """
    Attributes:
        number (int): Alliance number.
        pick (int): Order the team was picked in the alliance from 0-2, with 0 being alliance captain.
        name (None | str | Unset): Alliance name, may be null.
        backup (None | TeamEventStatusAllianceBackupType1 | Unset): Backup status, may be null.
    """

    number: int
    pick: int
    name: None | str | Unset = UNSET
    backup: None | TeamEventStatusAllianceBackupType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_event_status_alliance_backup_type_1 import TeamEventStatusAllianceBackupType1

        number = self.number

        pick = self.pick

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup: dict[str, Any] | None | Unset
        if isinstance(self.backup, Unset):
            backup = UNSET
        elif isinstance(self.backup, TeamEventStatusAllianceBackupType1):
            backup = self.backup.to_dict()
        else:
            backup = self.backup

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "pick": pick,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if backup is not UNSET:
            field_dict["backup"] = backup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_event_status_alliance_backup_type_1 import TeamEventStatusAllianceBackupType1

        d = dict(src_dict)
        number = d.pop("number")

        pick = d.pop("pick")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_backup(data: object) -> None | TeamEventStatusAllianceBackupType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_team_event_status_alliance_backup_type_1 = (
                    TeamEventStatusAllianceBackupType1.from_dict(data)
                )

                return componentsschemas_team_event_status_alliance_backup_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamEventStatusAllianceBackupType1 | Unset, data)

        backup = _parse_backup(d.pop("backup", UNSET))

        team_event_status_alliance = cls(
            number=number,
            pick=pick,
            name=name,
            backup=backup,
        )

        team_event_status_alliance.additional_properties = d
        return team_event_status_alliance

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
