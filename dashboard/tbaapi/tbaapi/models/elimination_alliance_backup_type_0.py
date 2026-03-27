from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EliminationAllianceBackupType0")


@_attrs_define
class EliminationAllianceBackupType0:
    """Backup team called in, may be null.

    Attributes:
        in_ (str): Team key that was called in as the backup.
        out (str): Team key that was replaced by the backup team.
    """

    in_: str
    out: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_ = self.in_

        out = self.out

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in": in_,
                "out": out,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_ = d.pop("in")

        out = d.pop("out")

        elimination_alliance_backup_type_0 = cls(
            in_=in_,
            out=out,
        )

        elimination_alliance_backup_type_0.additional_properties = d
        return elimination_alliance_backup_type_0

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
