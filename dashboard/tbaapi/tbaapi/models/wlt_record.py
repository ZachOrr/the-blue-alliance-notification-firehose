from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="WLTRecord")


@_attrs_define
class WLTRecord:
    """A Win-Loss-Tie record for a team, or an alliance.

    Attributes:
        losses (int): Number of losses.
        wins (int): Number of wins.
        ties (int): Number of ties.
    """

    losses: int
    wins: int
    ties: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        losses = self.losses

        wins = self.wins

        ties = self.ties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "losses": losses,
                "wins": wins,
                "ties": ties,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        losses = d.pop("losses")

        wins = d.pop("wins")

        ties = d.pop("ties")

        wlt_record = cls(
            losses=losses,
            wins=wins,
            ties=ties,
        )

        wlt_record.additional_properties = d
        return wlt_record

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
