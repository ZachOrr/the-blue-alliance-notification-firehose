from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="APIStatusAppVersion")


@_attrs_define
class APIStatusAppVersion:
    """
    Attributes:
        min_app_version (int): Internal use - Minimum application version required to correctly connect and process
            data.
        latest_app_version (int): Internal use - Latest application version available.
    """

    min_app_version: int
    latest_app_version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_app_version = self.min_app_version

        latest_app_version = self.latest_app_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "min_app_version": min_app_version,
                "latest_app_version": latest_app_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_app_version = d.pop("min_app_version")

        latest_app_version = d.pop("latest_app_version")

        api_status_app_version = cls(
            min_app_version=min_app_version,
            latest_app_version=latest_app_version,
        )

        api_status_app_version.additional_properties = d
        return api_status_app_version

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
