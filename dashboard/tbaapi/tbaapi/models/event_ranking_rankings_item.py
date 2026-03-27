from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.wlt_record import WLTRecord


T = TypeVar("T", bound="EventRankingRankingsItem")


@_attrs_define
class EventRankingRankingsItem:
    """
    Attributes:
        matches_played (int): Number of matches played by this team.
        qual_average (int | None): The average match score during qualifications. Year specific. May be null if not
            relevant for a given year.
        extra_stats (list[float]): Additional special data on the team's performance calculated by TBA.
        sort_orders (list[float]): Additional year-specific information. See parent `sort_order_info` for details.
        record (None | WLTRecord):
        rank (int): The team's rank at the event as provided by FIRST.
        dq (int): Number of times disqualified.
        team_key (str): The team with this rank.
    """

    matches_played: int
    qual_average: int | None
    extra_stats: list[float]
    sort_orders: list[float]
    record: None | WLTRecord
    rank: int
    dq: int
    team_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wlt_record import WLTRecord

        matches_played = self.matches_played

        qual_average: int | None
        qual_average = self.qual_average

        extra_stats = self.extra_stats

        sort_orders = self.sort_orders

        record: dict[str, Any] | None
        if isinstance(self.record, WLTRecord):
            record = self.record.to_dict()
        else:
            record = self.record

        rank = self.rank

        dq = self.dq

        team_key = self.team_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches_played": matches_played,
                "qual_average": qual_average,
                "extra_stats": extra_stats,
                "sort_orders": sort_orders,
                "record": record,
                "rank": rank,
                "dq": dq,
                "team_key": team_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wlt_record import WLTRecord

        d = dict(src_dict)
        matches_played = d.pop("matches_played")

        def _parse_qual_average(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        qual_average = _parse_qual_average(d.pop("qual_average"))

        extra_stats = cast(list[float], d.pop("extra_stats"))

        sort_orders = cast(list[float], d.pop("sort_orders"))

        def _parse_record(data: object) -> None | WLTRecord:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = WLTRecord.from_dict(data)

                return record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WLTRecord, data)

        record = _parse_record(d.pop("record"))

        rank = d.pop("rank")

        dq = d.pop("dq")

        team_key = d.pop("team_key")

        event_ranking_rankings_item = cls(
            matches_played=matches_played,
            qual_average=qual_average,
            extra_stats=extra_stats,
            sort_orders=sort_orders,
            record=record,
            rank=rank,
            dq=dq,
            team_key=team_key,
        )

        event_ranking_rankings_item.additional_properties = d
        return event_ranking_rankings_item

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
