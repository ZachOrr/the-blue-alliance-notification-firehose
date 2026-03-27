from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wlt_record import WLTRecord


T = TypeVar("T", bound="TeamEventStatusRankRankingType0")


@_attrs_define
class TeamEventStatusRankRankingType0:
    """
    Attributes:
        matches_played (int | Unset): Number of matches played.
        qual_average (float | None | Unset): For some years, average qualification score. Can be null.
        sort_orders (list[float] | None | Unset): Ordered list of values used to determine the rank. See the
            `sort_order_info` property for the name of each value.
        record (None | Unset | WLTRecord):
        rank (int | None | Unset): Relative rank of this team.
        dq (int | None | Unset): Number of matches the team was disqualified for.
        team_key (str | Unset): TBA team key for this rank.
    """

    matches_played: int | Unset = UNSET
    qual_average: float | None | Unset = UNSET
    sort_orders: list[float] | None | Unset = UNSET
    record: None | Unset | WLTRecord = UNSET
    rank: int | None | Unset = UNSET
    dq: int | None | Unset = UNSET
    team_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wlt_record import WLTRecord

        matches_played = self.matches_played

        qual_average: float | None | Unset
        if isinstance(self.qual_average, Unset):
            qual_average = UNSET
        else:
            qual_average = self.qual_average

        sort_orders: list[float] | None | Unset
        if isinstance(self.sort_orders, Unset):
            sort_orders = UNSET
        elif isinstance(self.sort_orders, list):
            sort_orders = self.sort_orders

        else:
            sort_orders = self.sort_orders

        record: dict[str, Any] | None | Unset
        if isinstance(self.record, Unset):
            record = UNSET
        elif isinstance(self.record, WLTRecord):
            record = self.record.to_dict()
        else:
            record = self.record

        rank: int | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        dq: int | None | Unset
        if isinstance(self.dq, Unset):
            dq = UNSET
        else:
            dq = self.dq

        team_key = self.team_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matches_played is not UNSET:
            field_dict["matches_played"] = matches_played
        if qual_average is not UNSET:
            field_dict["qual_average"] = qual_average
        if sort_orders is not UNSET:
            field_dict["sort_orders"] = sort_orders
        if record is not UNSET:
            field_dict["record"] = record
        if rank is not UNSET:
            field_dict["rank"] = rank
        if dq is not UNSET:
            field_dict["dq"] = dq
        if team_key is not UNSET:
            field_dict["team_key"] = team_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wlt_record import WLTRecord

        d = dict(src_dict)
        matches_played = d.pop("matches_played", UNSET)

        def _parse_qual_average(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        qual_average = _parse_qual_average(d.pop("qual_average", UNSET))

        def _parse_sort_orders(data: object) -> list[float] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_orders_type_0 = cast(list[float], data)

                return sort_orders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[float] | None | Unset, data)

        sort_orders = _parse_sort_orders(d.pop("sort_orders", UNSET))

        def _parse_record(data: object) -> None | Unset | WLTRecord:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                record_type_0 = WLTRecord.from_dict(data)

                return record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WLTRecord, data)

        record = _parse_record(d.pop("record", UNSET))

        def _parse_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))

        def _parse_dq(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        dq = _parse_dq(d.pop("dq", UNSET))

        team_key = d.pop("team_key", UNSET)

        team_event_status_rank_ranking_type_0 = cls(
            matches_played=matches_played,
            qual_average=qual_average,
            sort_orders=sort_orders,
            record=record,
            rank=rank,
            dq=dq,
            team_key=team_key,
        )

        team_event_status_rank_ranking_type_0.additional_properties = d
        return team_event_status_rank_ranking_type_0

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
