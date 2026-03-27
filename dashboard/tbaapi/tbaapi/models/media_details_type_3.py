from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="MediaDetailsType3")


@_attrs_define
class MediaDetailsType3:
    """
    Attributes:
        model_created (datetime.datetime):
        model_description (None | str):
        model_image (str):
        model_name (str):
    """

    model_created: datetime.datetime
    model_description: None | str
    model_image: str
    model_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_created = self.model_created.isoformat()

        model_description: None | str
        model_description = self.model_description

        model_image = self.model_image

        model_name = self.model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model_created": model_created,
                "model_description": model_description,
                "model_image": model_image,
                "model_name": model_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model_created = isoparse(d.pop("model_created"))

        def _parse_model_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        model_description = _parse_model_description(d.pop("model_description"))

        model_image = d.pop("model_image")

        model_name = d.pop("model_name")

        media_details_type_3 = cls(
            model_created=model_created,
            model_description=model_description,
            model_image=model_image,
            model_name=model_name,
        )

        media_details_type_3.additional_properties = d
        return media_details_type_3

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
