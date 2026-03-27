from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webcast_status import WebcastStatus
from ..models.webcast_type import WebcastType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Webcast")


@_attrs_define
class Webcast:
    """
    Attributes:
        type_ (WebcastType): Type of webcast, typically descriptive of the streaming provider.
        channel (str): Type specific channel information. May be the YouTube stream, or Twitch channel name. In the case
            of iframe types, contains HTML to embed the stream in an HTML iframe.
        date (None | str | Unset): The date for the webcast in `yyyy-mm-dd` format. May be null.
        file (None | str | Unset): File identification as may be required for some types. May be null.
        status (WebcastStatus | Unset): The online status of the webcast, fetched from the streaming provider's API. May
            be null if not available.
        stream_title (None | str | Unset): The title of the stream from the streaming provider. May be null.
        viewer_count (int | None | Unset): The current viewer count from the streaming provider. May be null.
    """

    type_: WebcastType
    channel: str
    date: None | str | Unset = UNSET
    file: None | str | Unset = UNSET
    status: WebcastStatus | Unset = UNSET
    stream_title: None | str | Unset = UNSET
    viewer_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        channel = self.channel

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        stream_title: None | str | Unset
        if isinstance(self.stream_title, Unset):
            stream_title = UNSET
        else:
            stream_title = self.stream_title

        viewer_count: int | None | Unset
        if isinstance(self.viewer_count, Unset):
            viewer_count = UNSET
        else:
            viewer_count = self.viewer_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "channel": channel,
            }
        )
        if date is not UNSET:
            field_dict["date"] = date
        if file is not UNSET:
            field_dict["file"] = file
        if status is not UNSET:
            field_dict["status"] = status
        if stream_title is not UNSET:
            field_dict["stream_title"] = stream_title
        if viewer_count is not UNSET:
            field_dict["viewer_count"] = viewer_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = WebcastType(d.pop("type"))

        channel = d.pop("channel")

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))

        _status = d.pop("status", UNSET)
        status: WebcastStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebcastStatus(_status)

        def _parse_stream_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stream_title = _parse_stream_title(d.pop("stream_title", UNSET))

        def _parse_viewer_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        viewer_count = _parse_viewer_count(d.pop("viewer_count", UNSET))

        webcast = cls(
            type_=type_,
            channel=channel,
            date=date,
            file=file,
            status=status,
            stream_title=stream_title,
            viewer_count=viewer_count,
        )

        webcast.additional_properties = d
        return webcast

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
