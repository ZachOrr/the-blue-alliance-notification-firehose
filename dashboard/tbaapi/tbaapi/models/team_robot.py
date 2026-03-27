from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TeamRobot")


@_attrs_define
class TeamRobot:
    """
    Attributes:
        year (int): Year this robot competed in.
        robot_name (str): Name of the robot as provided by the team.
        key (str): Internal TBA identifier for this robot.
        team_key (str): TBA team key for this robot.
    """

    year: int
    robot_name: str
    key: str
    team_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year = self.year

        robot_name = self.robot_name

        key = self.key

        team_key = self.team_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "year": year,
                "robot_name": robot_name,
                "key": key,
                "team_key": team_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        year = d.pop("year")

        robot_name = d.pop("robot_name")

        key = d.pop("key")

        team_key = d.pop("team_key")

        team_robot = cls(
            year=year,
            robot_name=robot_name,
            key=key,
            team_key=team_key,
        )

        team_robot.additional_properties = d
        return team_robot

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
