from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_district_points_points import EventDistrictPointsPoints
    from ..models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers


T = TypeVar("T", bound="EventDistrictPoints")


@_attrs_define
class EventDistrictPoints:
    """
    Attributes:
        points (EventDistrictPointsPoints): Points gained for each team at the event. Stored as a key-value pair with
            the team key as the key, and an object describing the points as its value.
        tiebreakers (EventDistrictPointsTiebreakers | Unset): Tiebreaker values for each team at the event. Stored as a
            key-value pair with the team key as the key, and an object describing the tiebreaker elements as its value.
    """

    points: EventDistrictPointsPoints
    tiebreakers: EventDistrictPointsTiebreakers | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points = self.points.to_dict()

        tiebreakers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tiebreakers, Unset):
            tiebreakers = self.tiebreakers.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points": points,
            }
        )
        if tiebreakers is not UNSET:
            field_dict["tiebreakers"] = tiebreakers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_district_points_points import EventDistrictPointsPoints
        from ..models.event_district_points_tiebreakers import EventDistrictPointsTiebreakers

        d = dict(src_dict)
        points = EventDistrictPointsPoints.from_dict(d.pop("points"))

        _tiebreakers = d.pop("tiebreakers", UNSET)
        tiebreakers: EventDistrictPointsTiebreakers | Unset
        if isinstance(_tiebreakers, Unset):
            tiebreakers = UNSET
        else:
            tiebreakers = EventDistrictPointsTiebreakers.from_dict(_tiebreakers)

        event_district_points = cls(
            points=points,
            tiebreakers=tiebreakers,
        )

        event_district_points.additional_properties = d
        return event_district_points

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
