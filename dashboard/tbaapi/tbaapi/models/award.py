from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.award_recipient import AwardRecipient


T = TypeVar("T", bound="Award")


@_attrs_define
class Award:
    """
    Attributes:
        name (str): The name of the award as provided by FIRST. May vary for the same award type.
        award_type (int): Type of award given. See https://github.com/the-blue-alliance/the-blue-
            alliance/blob/main/src/backend/common/consts/award_type.py#L8
        event_key (str): The event_key of the event the award was won at.
        recipient_list (list[AwardRecipient]): A list of recipients of the award at the event. May have either a
            team_key or an awardee, both, or neither (in the case the award wasn't awarded at the event).
        year (int): The year this award was won.
    """

    name: str
    award_type: int
    event_key: str
    recipient_list: list[AwardRecipient]
    year: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        award_type = self.award_type

        event_key = self.event_key

        recipient_list = []
        for recipient_list_item_data in self.recipient_list:
            recipient_list_item = recipient_list_item_data.to_dict()
            recipient_list.append(recipient_list_item)

        year = self.year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "award_type": award_type,
                "event_key": event_key,
                "recipient_list": recipient_list,
                "year": year,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.award_recipient import AwardRecipient

        d = dict(src_dict)
        name = d.pop("name")

        award_type = d.pop("award_type")

        event_key = d.pop("event_key")

        recipient_list = []
        _recipient_list = d.pop("recipient_list")
        for recipient_list_item_data in _recipient_list:
            recipient_list_item = AwardRecipient.from_dict(recipient_list_item_data)

            recipient_list.append(recipient_list_item)

        year = d.pop("year")

        award = cls(
            name=name,
            award_type=award_type,
            event_key=event_key,
            recipient_list=recipient_list,
            year=year,
        )

        award.additional_properties = d
        return award

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
