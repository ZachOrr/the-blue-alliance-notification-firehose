from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.zebra_alliances import ZebraAlliances


T = TypeVar("T", bound="Zebra")


@_attrs_define
class Zebra:
    """
    Attributes:
        key (str): TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the
            year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER`
            is the match number in the competition level. A set number may be appended to the competition level if more than
            one match in required per set.
        times (list[float]): A list of relative timestamps for each data point. Each timestamp will correspond to the X
            and Y value at the same index in a team xs and ys arrays. `times`, all teams `xs` and all teams `ys` are
            guarenteed to be the same length.
        alliances (ZebraAlliances):
    """

    key: str
    times: list[float]
    alliances: ZebraAlliances
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        times = self.times

        alliances = self.alliances.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "times": times,
                "alliances": alliances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.zebra_alliances import ZebraAlliances

        d = dict(src_dict)
        key = d.pop("key")

        times = cast(list[float], d.pop("times"))

        alliances = ZebraAlliances.from_dict(d.pop("alliances"))

        zebra = cls(
            key=key,
            times=times,
            alliances=alliances,
        )

        zebra.additional_properties = d
        return zebra

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
