from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comp_level import CompLevel
from ..models.double_elim_round import DoubleElimRound
from ..models.elimination_alliance_status_status import EliminationAllianceStatusStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wlt_record import WLTRecord


T = TypeVar("T", bound="EliminationAllianceStatus")


@_attrs_define
class EliminationAllianceStatus:
    """
    Attributes:
        playoff_type (float | None): Playoff type, may be null.
        level (CompLevel): The competition level the match was played at.
        record (None | WLTRecord): W-L-T record for the alliance, may be null.
        current_level_record (None | WLTRecord): W-L-T record for the alliance at the current level, may be null.
        status (EliminationAllianceStatusStatus): Status of the alliance.
        playoff_average (float | None | Unset): Average match score during playoffs. Year specific. May be null.
        advanced_to_round_robin_finals (bool | Unset): Whether the alliance advanced to round robin finals.
        double_elim_round (DoubleElimRound | Unset): Double elimination round, if applicable.
        round_robin_rank (int | Unset): Rank in round robin play.
    """

    playoff_type: float | None
    level: CompLevel
    record: None | WLTRecord
    current_level_record: None | WLTRecord
    status: EliminationAllianceStatusStatus
    playoff_average: float | None | Unset = UNSET
    advanced_to_round_robin_finals: bool | Unset = UNSET
    double_elim_round: DoubleElimRound | Unset = UNSET
    round_robin_rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wlt_record import WLTRecord

        playoff_type: float | None
        playoff_type = self.playoff_type

        level = self.level.value

        record: dict[str, Any] | None
        if isinstance(self.record, WLTRecord):
            record = self.record.to_dict()
        else:
            record = self.record

        current_level_record: dict[str, Any] | None
        if isinstance(self.current_level_record, WLTRecord):
            current_level_record = self.current_level_record.to_dict()
        else:
            current_level_record = self.current_level_record

        status = self.status.value

        playoff_average: float | None | Unset
        if isinstance(self.playoff_average, Unset):
            playoff_average = UNSET
        else:
            playoff_average = self.playoff_average

        advanced_to_round_robin_finals = self.advanced_to_round_robin_finals

        double_elim_round: str | Unset = UNSET
        if not isinstance(self.double_elim_round, Unset):
            double_elim_round = self.double_elim_round.value

        round_robin_rank = self.round_robin_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playoff_type": playoff_type,
                "level": level,
                "record": record,
                "current_level_record": current_level_record,
                "status": status,
            }
        )
        if playoff_average is not UNSET:
            field_dict["playoff_average"] = playoff_average
        if advanced_to_round_robin_finals is not UNSET:
            field_dict["advanced_to_round_robin_finals"] = advanced_to_round_robin_finals
        if double_elim_round is not UNSET:
            field_dict["double_elim_round"] = double_elim_round
        if round_robin_rank is not UNSET:
            field_dict["round_robin_rank"] = round_robin_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wlt_record import WLTRecord

        d = dict(src_dict)

        def _parse_playoff_type(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        playoff_type = _parse_playoff_type(d.pop("playoff_type"))

        level = CompLevel(d.pop("level"))

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

        def _parse_current_level_record(data: object) -> None | WLTRecord:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_level_record_type_0 = WLTRecord.from_dict(data)

                return current_level_record_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WLTRecord, data)

        current_level_record = _parse_current_level_record(d.pop("current_level_record"))

        status = EliminationAllianceStatusStatus(d.pop("status"))

        def _parse_playoff_average(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        playoff_average = _parse_playoff_average(d.pop("playoff_average", UNSET))

        advanced_to_round_robin_finals = d.pop("advanced_to_round_robin_finals", UNSET)

        _double_elim_round = d.pop("double_elim_round", UNSET)
        double_elim_round: DoubleElimRound | Unset
        if isinstance(_double_elim_round, Unset):
            double_elim_round = UNSET
        else:
            double_elim_round = DoubleElimRound(_double_elim_round)

        round_robin_rank = d.pop("round_robin_rank", UNSET)

        elimination_alliance_status = cls(
            playoff_type=playoff_type,
            level=level,
            record=record,
            current_level_record=current_level_record,
            status=status,
            playoff_average=playoff_average,
            advanced_to_round_robin_finals=advanced_to_round_robin_finals,
            double_elim_round=double_elim_round,
            round_robin_rank=round_robin_rank,
        )

        elimination_alliance_status.additional_properties = d
        return elimination_alliance_status

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
