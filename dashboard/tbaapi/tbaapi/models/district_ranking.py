from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.district_ranking_event_points_item import DistrictRankingEventPointsItem


T = TypeVar("T", bound="DistrictRanking")


@_attrs_define
class DistrictRanking:
    """Rank of a team in a district.

    Attributes:
        team_key (str): TBA team key for the team.
        rank (int): Numerical rank of the team, 1 being top rank.
        rookie_bonus (int): Any points added to a team as a result of the rookie bonus.
        point_total (int): Total district points for the team.
        event_points (list[DistrictRankingEventPointsItem]): List of events that contributed to the point total for the
            team.
        adjustments (int | Unset): Any points adjustments applied to the team.
        other_bonus (int | Unset): Any other bonus points awarded to the team.
    """

    team_key: str
    rank: int
    rookie_bonus: int
    point_total: int
    event_points: list[DistrictRankingEventPointsItem]
    adjustments: int | Unset = UNSET
    other_bonus: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_key = self.team_key

        rank = self.rank

        rookie_bonus = self.rookie_bonus

        point_total = self.point_total

        event_points = []
        for event_points_item_data in self.event_points:
            event_points_item = event_points_item_data.to_dict()
            event_points.append(event_points_item)

        adjustments = self.adjustments

        other_bonus = self.other_bonus

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_key": team_key,
                "rank": rank,
                "rookie_bonus": rookie_bonus,
                "point_total": point_total,
                "event_points": event_points,
            }
        )
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if other_bonus is not UNSET:
            field_dict["other_bonus"] = other_bonus

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_ranking_event_points_item import DistrictRankingEventPointsItem

        d = dict(src_dict)
        team_key = d.pop("team_key")

        rank = d.pop("rank")

        rookie_bonus = d.pop("rookie_bonus")

        point_total = d.pop("point_total")

        event_points = []
        _event_points = d.pop("event_points")
        for event_points_item_data in _event_points:
            event_points_item = DistrictRankingEventPointsItem.from_dict(event_points_item_data)

            event_points.append(event_points_item)

        adjustments = d.pop("adjustments", UNSET)

        other_bonus = d.pop("other_bonus", UNSET)

        district_ranking = cls(
            team_key=team_key,
            rank=rank,
            rookie_bonus=rookie_bonus,
            point_total=point_total,
            event_points=event_points,
            adjustments=adjustments,
            other_bonus=other_bonus,
        )

        district_ranking.additional_properties = d
        return district_ranking

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
