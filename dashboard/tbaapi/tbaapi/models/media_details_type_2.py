from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaDetailsType2")


@_attrs_define
class MediaDetailsType2:
    """
    Attributes:
        author_id (int):
        author_name (str):
        author_url (str):
        height (int | None):
        html (str):
        media_id (str):
        provider_name (str):
        provider_url (str):
        thumbnail_height (int):
        thumbnail_url (str):
        thumbnail_width (int):
        title (str):
        type_ (str):
        version (str):
        width (int):
    """

    author_id: int
    author_name: str
    author_url: str
    height: int | None
    html: str
    media_id: str
    provider_name: str
    provider_url: str
    thumbnail_height: int
    thumbnail_url: str
    thumbnail_width: int
    title: str
    type_: str
    version: str
    width: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author_id = self.author_id

        author_name = self.author_name

        author_url = self.author_url

        height: int | None
        height = self.height

        html = self.html

        media_id = self.media_id

        provider_name = self.provider_name

        provider_url = self.provider_url

        thumbnail_height = self.thumbnail_height

        thumbnail_url = self.thumbnail_url

        thumbnail_width = self.thumbnail_width

        title = self.title

        type_ = self.type_

        version = self.version

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author_id": author_id,
                "author_name": author_name,
                "author_url": author_url,
                "height": height,
                "html": html,
                "media_id": media_id,
                "provider_name": provider_name,
                "provider_url": provider_url,
                "thumbnail_height": thumbnail_height,
                "thumbnail_url": thumbnail_url,
                "thumbnail_width": thumbnail_width,
                "title": title,
                "type": type_,
                "version": version,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        author_id = d.pop("author_id")

        author_name = d.pop("author_name")

        author_url = d.pop("author_url")

        def _parse_height(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        height = _parse_height(d.pop("height"))

        html = d.pop("html")

        media_id = d.pop("media_id")

        provider_name = d.pop("provider_name")

        provider_url = d.pop("provider_url")

        thumbnail_height = d.pop("thumbnail_height")

        thumbnail_url = d.pop("thumbnail_url")

        thumbnail_width = d.pop("thumbnail_width")

        title = d.pop("title")

        type_ = d.pop("type")

        version = d.pop("version")

        width = d.pop("width")

        media_details_type_2 = cls(
            author_id=author_id,
            author_name=author_name,
            author_url=author_url,
            height=height,
            html=html,
            media_id=media_id,
            provider_name=provider_name,
            provider_url=provider_url,
            thumbnail_height=thumbnail_height,
            thumbnail_url=thumbnail_url,
            thumbnail_width=thumbnail_width,
            title=title,
            type_=type_,
            version=version,
            width=width,
        )

        media_details_type_2.additional_properties = d
        return media_details_type_2

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
