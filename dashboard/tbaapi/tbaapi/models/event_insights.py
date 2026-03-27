from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_insights_playoff import EventInsightsPlayoff
    from ..models.event_insights_qual import EventInsightsQual


T = TypeVar("T", bound="EventInsights")


@_attrs_define
class EventInsights:
    """A year-specific event insight object expressed as a JSON string, separated in to `qual` and `playoff` fields. See
    also Event_Insights_2016, Event_Insights_2017, etc.

        Attributes:
            qual (EventInsightsQual | Unset): Inights for the qualification round of an event
            playoff (EventInsightsPlayoff | Unset): Insights for the playoff round of an event
    """

    qual: EventInsightsQual | Unset = UNSET
    playoff: EventInsightsPlayoff | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qual: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qual, Unset):
            qual = self.qual.to_dict()

        playoff: dict[str, Any] | Unset = UNSET
        if not isinstance(self.playoff, Unset):
            playoff = self.playoff.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qual is not UNSET:
            field_dict["qual"] = qual
        if playoff is not UNSET:
            field_dict["playoff"] = playoff

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_insights_playoff import EventInsightsPlayoff
        from ..models.event_insights_qual import EventInsightsQual

        d = dict(src_dict)
        _qual = d.pop("qual", UNSET)
        qual: EventInsightsQual | Unset
        if isinstance(_qual, Unset):
            qual = UNSET
        else:
            qual = EventInsightsQual.from_dict(_qual)

        _playoff = d.pop("playoff", UNSET)
        playoff: EventInsightsPlayoff | Unset
        if isinstance(_playoff, Unset):
            playoff = UNSET
        else:
            playoff = EventInsightsPlayoff.from_dict(_playoff)

        event_insights = cls(
            qual=qual,
            playoff=playoff,
        )

        event_insights.additional_properties = d
        return event_insights

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
