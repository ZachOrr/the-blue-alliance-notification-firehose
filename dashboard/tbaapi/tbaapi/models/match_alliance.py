from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchAlliance")


@_attrs_define
class MatchAlliance:
    """
    Attributes:
        score (int): Score for this alliance. Will be -1 for an unplayed match.
        team_keys (list[str]):
        surrogate_team_keys (list[str]): TBA team keys (eg `frc254`) of any teams playing as a surrogate.
        dq_team_keys (list[str]): TBA team keys (eg `frc254`) of any disqualified teams.
    """

    score: int
    team_keys: list[str]
    surrogate_team_keys: list[str]
    dq_team_keys: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        team_keys = self.team_keys

        surrogate_team_keys = self.surrogate_team_keys

        dq_team_keys = self.dq_team_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "score": score,
                "team_keys": team_keys,
                "surrogate_team_keys": surrogate_team_keys,
                "dq_team_keys": dq_team_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        score = d.pop("score")

        team_keys = cast(list[str], d.pop("team_keys"))

        surrogate_team_keys = cast(list[str], d.pop("surrogate_team_keys"))

        dq_team_keys = cast(list[str], d.pop("dq_team_keys"))

        match_alliance = cls(
            score=score,
            team_keys=team_keys,
            surrogate_team_keys=surrogate_team_keys,
            dq_team_keys=dq_team_keys,
        )

        match_alliance.additional_properties = d
        return match_alliance

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
