from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.regional_ranking_event_points_item import RegionalRankingEventPointsItem


T = TypeVar("T", bound="RegionalRanking")


@_attrs_define
class RegionalRanking:
    """Rank of a team in the regional pool.

    Attributes:
        team_key (str): TBA team key for the team.
        rank (int): Numerical rank of the team, 1 being top rank.
        point_total (int): Total district points for the team.
        rookie_bonus (int | Unset): Any points added to a team as a result of the rookie bonus.
        single_event_bonus (int | Unset): Additional points awarded in lieu of a second event, based on first event
            performance
        event_points (list[RegionalRankingEventPointsItem] | Unset): List of events that contributed to the point total
            for the team.
    """

    team_key: str
    rank: int
    point_total: int
    rookie_bonus: int | Unset = UNSET
    single_event_bonus: int | Unset = UNSET
    event_points: list[RegionalRankingEventPointsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_key = self.team_key

        rank = self.rank

        point_total = self.point_total

        rookie_bonus = self.rookie_bonus

        single_event_bonus = self.single_event_bonus

        event_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.event_points, Unset):
            event_points = []
            for event_points_item_data in self.event_points:
                event_points_item = event_points_item_data.to_dict()
                event_points.append(event_points_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_key": team_key,
                "rank": rank,
                "point_total": point_total,
            }
        )
        if rookie_bonus is not UNSET:
            field_dict["rookie_bonus"] = rookie_bonus
        if single_event_bonus is not UNSET:
            field_dict["single_event_bonus"] = single_event_bonus
        if event_points is not UNSET:
            field_dict["event_points"] = event_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.regional_ranking_event_points_item import RegionalRankingEventPointsItem

        d = dict(src_dict)
        team_key = d.pop("team_key")

        rank = d.pop("rank")

        point_total = d.pop("point_total")

        rookie_bonus = d.pop("rookie_bonus", UNSET)

        single_event_bonus = d.pop("single_event_bonus", UNSET)

        _event_points = d.pop("event_points", UNSET)
        event_points: list[RegionalRankingEventPointsItem] | Unset = UNSET
        if _event_points is not UNSET:
            event_points = []
            for event_points_item_data in _event_points:
                event_points_item = RegionalRankingEventPointsItem.from_dict(event_points_item_data)

                event_points.append(event_points_item)

        regional_ranking = cls(
            team_key=team_key,
            rank=rank,
            point_total=point_total,
            rookie_bonus=rookie_bonus,
            single_event_bonus=single_event_bonus,
            event_points=event_points,
        )

        regional_ranking.additional_properties = d
        return regional_ranking

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
