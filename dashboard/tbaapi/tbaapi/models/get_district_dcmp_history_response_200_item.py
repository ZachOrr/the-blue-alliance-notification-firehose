from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award import Award
    from ..models.event import Event


T = TypeVar("T", bound="GetDistrictDCMPHistoryResponse200Item")


@_attrs_define
class GetDistrictDCMPHistoryResponse200Item:
    """
    Attributes:
        awards (list[Award] | Unset):
        event (Event | Unset):
    """

    awards: list[Award] | Unset = UNSET
    event: Event | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        awards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.awards, Unset):
            awards = []
            for awards_item_data in self.awards:
                awards_item = awards_item_data.to_dict()
                awards.append(awards_item)

        event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if awards is not UNSET:
            field_dict["awards"] = awards
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.award import Award
        from ..models.event import Event

        d = dict(src_dict)
        _awards = d.pop("awards", UNSET)
        awards: list[Award] | Unset = UNSET
        if _awards is not UNSET:
            awards = []
            for awards_item_data in _awards:
                awards_item = Award.from_dict(awards_item_data)

                awards.append(awards_item)

        _event = d.pop("event", UNSET)
        event: Event | Unset
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = Event.from_dict(_event)

        get_district_dcmp_history_response_200_item = cls(
            awards=awards,
            event=event,
        )

        get_district_dcmp_history_response_200_item.additional_properties = d
        return get_district_dcmp_history_response_200_item

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
