from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamEventStatusAllianceBackupType1")


@_attrs_define
class TeamEventStatusAllianceBackupType1:
    """Backup status, may be null.

    Attributes:
        out (str | Unset): TBA key for the team replaced by the backup.
        in_ (str | Unset): TBA key for the backup team called in.
    """

    out: str | Unset = UNSET
    in_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        out = self.out

        in_ = self.in_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if out is not UNSET:
            field_dict["out"] = out
        if in_ is not UNSET:
            field_dict["in"] = in_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        out = d.pop("out", UNSET)

        in_ = d.pop("in", UNSET)

        team_event_status_alliance_backup_type_1 = cls(
            out=out,
            in_=in_,
        )

        team_event_status_alliance_backup_type_1.additional_properties = d
        return team_event_status_alliance_backup_type_1

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
