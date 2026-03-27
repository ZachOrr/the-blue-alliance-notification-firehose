from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ZebraTeam")


@_attrs_define
class ZebraTeam:
    """
    Attributes:
        team_key (str): The TBA team key for the Zebra MotionWorks data.
        xs (list[float]): A list containing doubles and nulls representing a teams X position in feet at the
            corresponding timestamp. A null value represents no tracking data for a given timestamp.
        ys (list[float]): A list containing doubles and nulls representing a teams Y position in feet at the
            corresponding timestamp. A null value represents no tracking data for a given timestamp.
    """

    team_key: str
    xs: list[float]
    ys: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_key = self.team_key

        xs = self.xs

        ys = self.ys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_key": team_key,
                "xs": xs,
                "ys": ys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_key = d.pop("team_key")

        xs = cast(list[float], d.pop("xs"))

        ys = cast(list[float], d.pop("ys"))

        zebra_team = cls(
            team_key=team_key,
            xs=xs,
            ys=ys,
        )

        zebra_team.additional_properties = d
        return zebra_team

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
