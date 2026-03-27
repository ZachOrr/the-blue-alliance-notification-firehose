from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.elimination_alliance_backup_type_0 import EliminationAllianceBackupType0
    from ..models.elimination_alliance_status import EliminationAllianceStatus


T = TypeVar("T", bound="EliminationAlliance")


@_attrs_define
class EliminationAlliance:
    """
    Attributes:
        declines (list[str]): List of teams that declined the alliance.
        picks (list[str]): List of team keys picked for the alliance. First pick is captain.
        name (str | Unset): Alliance name.
        backup (EliminationAllianceBackupType0 | None | Unset): Backup team called in, may be null.
        status (EliminationAllianceStatus | Unset):
    """

    declines: list[str]
    picks: list[str]
    name: str | Unset = UNSET
    backup: EliminationAllianceBackupType0 | None | Unset = UNSET
    status: EliminationAllianceStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.elimination_alliance_backup_type_0 import EliminationAllianceBackupType0

        declines = self.declines

        picks = self.picks

        name = self.name

        backup: dict[str, Any] | None | Unset
        if isinstance(self.backup, Unset):
            backup = UNSET
        elif isinstance(self.backup, EliminationAllianceBackupType0):
            backup = self.backup.to_dict()
        else:
            backup = self.backup

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "declines": declines,
                "picks": picks,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if backup is not UNSET:
            field_dict["backup"] = backup
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.elimination_alliance_backup_type_0 import EliminationAllianceBackupType0
        from ..models.elimination_alliance_status import EliminationAllianceStatus

        d = dict(src_dict)
        declines = cast(list[str], d.pop("declines"))

        picks = cast(list[str], d.pop("picks"))

        name = d.pop("name", UNSET)

        def _parse_backup(data: object) -> EliminationAllianceBackupType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                backup_type_0 = EliminationAllianceBackupType0.from_dict(data)

                return backup_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EliminationAllianceBackupType0 | None | Unset, data)

        backup = _parse_backup(d.pop("backup", UNSET))

        _status = d.pop("status", UNSET)
        status: EliminationAllianceStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EliminationAllianceStatus.from_dict(_status)

        elimination_alliance = cls(
            declines=declines,
            picks=picks,
            name=name,
            backup=backup,
            status=status,
        )

        elimination_alliance.additional_properties = d
        return elimination_alliance

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
