from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.regional_advancement_cmp_status import RegionalAdvancementCmpStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RegionalAdvancement")


@_attrs_define
class RegionalAdvancement:
    """Information about how a regional team qualified for FIRST Championship.

    Attributes:
        cmp (bool): Whether or not the team qualified for Championship.
        cmp_status (RegionalAdvancementCmpStatus):
        qualifying_event (str | Unset): The event key at which the team qualified
        qualifying_award_name (str | Unset): The name of the award which qualified the team
        qualifying_pool_week (int | Unset): Which week number's regional pool invitation the team got
    """

    cmp: bool
    cmp_status: RegionalAdvancementCmpStatus
    qualifying_event: str | Unset = UNSET
    qualifying_award_name: str | Unset = UNSET
    qualifying_pool_week: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cmp = self.cmp

        cmp_status = self.cmp_status.value

        qualifying_event = self.qualifying_event

        qualifying_award_name = self.qualifying_award_name

        qualifying_pool_week = self.qualifying_pool_week

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cmp": cmp,
                "cmp_status": cmp_status,
            }
        )
        if qualifying_event is not UNSET:
            field_dict["qualifying_event"] = qualifying_event
        if qualifying_award_name is not UNSET:
            field_dict["qualifying_award_name"] = qualifying_award_name
        if qualifying_pool_week is not UNSET:
            field_dict["qualifying_pool_week"] = qualifying_pool_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cmp = d.pop("cmp")

        cmp_status = RegionalAdvancementCmpStatus(d.pop("cmp_status"))

        qualifying_event = d.pop("qualifying_event", UNSET)

        qualifying_award_name = d.pop("qualifying_award_name", UNSET)

        qualifying_pool_week = d.pop("qualifying_pool_week", UNSET)

        regional_advancement = cls(
            cmp=cmp,
            cmp_status=cmp_status,
            qualifying_event=qualifying_event,
            qualifying_award_name=qualifying_award_name,
            qualifying_pool_week=qualifying_pool_week,
        )

        regional_advancement.additional_properties = d
        return regional_advancement

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
