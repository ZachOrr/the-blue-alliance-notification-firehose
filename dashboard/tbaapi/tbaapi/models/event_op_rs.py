from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_op_rs_ccwms import EventOPRsCcwms
    from ..models.event_op_rs_dprs import EventOPRsDprs
    from ..models.event_op_rs_oprs import EventOPRsOprs


T = TypeVar("T", bound="EventOPRs")


@_attrs_define
class EventOPRs:
    """OPR, DPR, and CCWM for teams at the event.

    Attributes:
        oprs (EventOPRsOprs | Unset): A key-value pair with team key (eg `frc254`) as key and OPR as value.
        dprs (EventOPRsDprs | Unset): A key-value pair with team key (eg `frc254`) as key and DPR as value.
        ccwms (EventOPRsCcwms | Unset): A key-value pair with team key (eg `frc254`) as key and CCWM as value.
    """

    oprs: EventOPRsOprs | Unset = UNSET
    dprs: EventOPRsDprs | Unset = UNSET
    ccwms: EventOPRsCcwms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oprs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oprs, Unset):
            oprs = self.oprs.to_dict()

        dprs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dprs, Unset):
            dprs = self.dprs.to_dict()

        ccwms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ccwms, Unset):
            ccwms = self.ccwms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oprs is not UNSET:
            field_dict["oprs"] = oprs
        if dprs is not UNSET:
            field_dict["dprs"] = dprs
        if ccwms is not UNSET:
            field_dict["ccwms"] = ccwms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_op_rs_ccwms import EventOPRsCcwms
        from ..models.event_op_rs_dprs import EventOPRsDprs
        from ..models.event_op_rs_oprs import EventOPRsOprs

        d = dict(src_dict)
        _oprs = d.pop("oprs", UNSET)
        oprs: EventOPRsOprs | Unset
        if isinstance(_oprs, Unset):
            oprs = UNSET
        else:
            oprs = EventOPRsOprs.from_dict(_oprs)

        _dprs = d.pop("dprs", UNSET)
        dprs: EventOPRsDprs | Unset
        if isinstance(_dprs, Unset):
            dprs = UNSET
        else:
            dprs = EventOPRsDprs.from_dict(_dprs)

        _ccwms = d.pop("ccwms", UNSET)
        ccwms: EventOPRsCcwms | Unset
        if isinstance(_ccwms, Unset):
            ccwms = UNSET
        else:
            ccwms = EventOPRsCcwms.from_dict(_ccwms)

        event_op_rs = cls(
            oprs=oprs,
            dprs=dprs,
            ccwms=ccwms,
        )

        event_op_rs.additional_properties = d
        return event_op_rs

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
