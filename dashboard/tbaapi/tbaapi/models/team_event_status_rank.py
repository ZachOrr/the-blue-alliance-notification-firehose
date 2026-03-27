from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_event_status_rank_ranking_type_0 import TeamEventStatusRankRankingType0
    from ..models.team_event_status_rank_sort_order_info_type_0_item import TeamEventStatusRankSortOrderInfoType0Item


T = TypeVar("T", bound="TeamEventStatusRank")


@_attrs_define
class TeamEventStatusRank:
    """
    Attributes:
        num_teams (int | Unset): Number of teams ranked.
        ranking (None | TeamEventStatusRankRankingType0 | Unset):
        sort_order_info (list[TeamEventStatusRankSortOrderInfoType0Item] | None | Unset): Ordered list of names
            corresponding to the elements of the `sort_orders` array.
        status (str | Unset):
    """

    num_teams: int | Unset = UNSET
    ranking: None | TeamEventStatusRankRankingType0 | Unset = UNSET
    sort_order_info: list[TeamEventStatusRankSortOrderInfoType0Item] | None | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.team_event_status_rank_ranking_type_0 import TeamEventStatusRankRankingType0

        num_teams = self.num_teams

        ranking: dict[str, Any] | None | Unset
        if isinstance(self.ranking, Unset):
            ranking = UNSET
        elif isinstance(self.ranking, TeamEventStatusRankRankingType0):
            ranking = self.ranking.to_dict()
        else:
            ranking = self.ranking

        sort_order_info: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort_order_info, Unset):
            sort_order_info = UNSET
        elif isinstance(self.sort_order_info, list):
            sort_order_info = []
            for sort_order_info_type_0_item_data in self.sort_order_info:
                sort_order_info_type_0_item = sort_order_info_type_0_item_data.to_dict()
                sort_order_info.append(sort_order_info_type_0_item)

        else:
            sort_order_info = self.sort_order_info

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_teams is not UNSET:
            field_dict["num_teams"] = num_teams
        if ranking is not UNSET:
            field_dict["ranking"] = ranking
        if sort_order_info is not UNSET:
            field_dict["sort_order_info"] = sort_order_info
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_event_status_rank_ranking_type_0 import TeamEventStatusRankRankingType0
        from ..models.team_event_status_rank_sort_order_info_type_0_item import (
            TeamEventStatusRankSortOrderInfoType0Item,
        )

        d = dict(src_dict)
        num_teams = d.pop("num_teams", UNSET)

        def _parse_ranking(data: object) -> None | TeamEventStatusRankRankingType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ranking_type_0 = TeamEventStatusRankRankingType0.from_dict(data)

                return ranking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TeamEventStatusRankRankingType0 | Unset, data)

        ranking = _parse_ranking(d.pop("ranking", UNSET))

        def _parse_sort_order_info(data: object) -> list[TeamEventStatusRankSortOrderInfoType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_order_info_type_0 = []
                _sort_order_info_type_0 = data
                for sort_order_info_type_0_item_data in _sort_order_info_type_0:
                    sort_order_info_type_0_item = TeamEventStatusRankSortOrderInfoType0Item.from_dict(
                        sort_order_info_type_0_item_data
                    )

                    sort_order_info_type_0.append(sort_order_info_type_0_item)

                return sort_order_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TeamEventStatusRankSortOrderInfoType0Item] | None | Unset, data)

        sort_order_info = _parse_sort_order_info(d.pop("sort_order_info", UNSET))

        status = d.pop("status", UNSET)

        team_event_status_rank = cls(
            num_teams=num_teams,
            ranking=ranking,
            sort_order_info=sort_order_info,
            status=status,
        )

        team_event_status_rank.additional_properties = d
        return team_event_status_rank

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
