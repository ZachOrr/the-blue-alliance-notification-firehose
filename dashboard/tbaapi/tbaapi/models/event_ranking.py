from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.event_ranking_extra_stats_info_item import EventRankingExtraStatsInfoItem
    from ..models.event_ranking_rankings_item import EventRankingRankingsItem
    from ..models.event_ranking_sort_order_info_type_0_item import EventRankingSortOrderInfoType0Item


T = TypeVar("T", bound="EventRanking")


@_attrs_define
class EventRanking:
    """
    Attributes:
        rankings (list[EventRankingRankingsItem]): List of rankings at the event.
        extra_stats_info (list[EventRankingExtraStatsInfoItem]): List of special TBA-generated values provided in the
            `extra_stats` array for each item.
        sort_order_info (list[EventRankingSortOrderInfoType0Item] | None): List of year-specific values provided in the
            `sort_orders` array for each team.
    """

    rankings: list[EventRankingRankingsItem]
    extra_stats_info: list[EventRankingExtraStatsInfoItem]
    sort_order_info: list[EventRankingSortOrderInfoType0Item] | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rankings = []
        for rankings_item_data in self.rankings:
            rankings_item = rankings_item_data.to_dict()
            rankings.append(rankings_item)

        extra_stats_info = []
        for extra_stats_info_item_data in self.extra_stats_info:
            extra_stats_info_item = extra_stats_info_item_data.to_dict()
            extra_stats_info.append(extra_stats_info_item)

        sort_order_info: list[dict[str, Any]] | None
        if isinstance(self.sort_order_info, list):
            sort_order_info = []
            for sort_order_info_type_0_item_data in self.sort_order_info:
                sort_order_info_type_0_item = sort_order_info_type_0_item_data.to_dict()
                sort_order_info.append(sort_order_info_type_0_item)

        else:
            sort_order_info = self.sort_order_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rankings": rankings,
                "extra_stats_info": extra_stats_info,
                "sort_order_info": sort_order_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_ranking_extra_stats_info_item import EventRankingExtraStatsInfoItem
        from ..models.event_ranking_rankings_item import EventRankingRankingsItem
        from ..models.event_ranking_sort_order_info_type_0_item import EventRankingSortOrderInfoType0Item

        d = dict(src_dict)
        rankings = []
        _rankings = d.pop("rankings")
        for rankings_item_data in _rankings:
            rankings_item = EventRankingRankingsItem.from_dict(rankings_item_data)

            rankings.append(rankings_item)

        extra_stats_info = []
        _extra_stats_info = d.pop("extra_stats_info")
        for extra_stats_info_item_data in _extra_stats_info:
            extra_stats_info_item = EventRankingExtraStatsInfoItem.from_dict(extra_stats_info_item_data)

            extra_stats_info.append(extra_stats_info_item)

        def _parse_sort_order_info(data: object) -> list[EventRankingSortOrderInfoType0Item] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_order_info_type_0 = []
                _sort_order_info_type_0 = data
                for sort_order_info_type_0_item_data in _sort_order_info_type_0:
                    sort_order_info_type_0_item = EventRankingSortOrderInfoType0Item.from_dict(
                        sort_order_info_type_0_item_data
                    )

                    sort_order_info_type_0.append(sort_order_info_type_0_item)

                return sort_order_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EventRankingSortOrderInfoType0Item] | None, data)

        sort_order_info = _parse_sort_order_info(d.pop("sort_order_info"))

        event_ranking = cls(
            rankings=rankings,
            extra_stats_info=extra_stats_info,
            sort_order_info=sort_order_info,
        )

        event_ranking.additional_properties = d
        return event_ranking

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
