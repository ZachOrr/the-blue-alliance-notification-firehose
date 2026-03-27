from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.comp_level import CompLevel
from ..models.match_winning_alliance import MatchWinningAlliance

if TYPE_CHECKING:
    from ..models.match_alliances import MatchAlliances
    from ..models.match_score_breakdown_2015 import MatchScoreBreakdown2015
    from ..models.match_score_breakdown_2016 import MatchScoreBreakdown2016
    from ..models.match_score_breakdown_2017 import MatchScoreBreakdown2017
    from ..models.match_score_breakdown_2018 import MatchScoreBreakdown2018
    from ..models.match_score_breakdown_2019 import MatchScoreBreakdown2019
    from ..models.match_score_breakdown_2020 import MatchScoreBreakdown2020
    from ..models.match_score_breakdown_2022 import MatchScoreBreakdown2022
    from ..models.match_score_breakdown_2023 import MatchScoreBreakdown2023
    from ..models.match_score_breakdown_2024 import MatchScoreBreakdown2024
    from ..models.match_score_breakdown_2025 import MatchScoreBreakdown2025
    from ..models.match_score_breakdown_2026 import MatchScoreBreakdown2026
    from ..models.match_videos_item import MatchVideosItem


T = TypeVar("T", bound="Match")


@_attrs_define
class Match:
    """
    Attributes:
        key (str): TBA match key with the format `yyyy[EVENT_CODE]_[COMP_LEVEL]m[MATCH_NUMBER]`, where `yyyy` is the
            year, and `EVENT_CODE` is the event code of the event, `COMP_LEVEL` is (qm, ef, qf, sf, f), and `MATCH_NUMBER`
            is the match number in the competition level. A set number may be appended to the competition level if more than
            one match in required per set.
        comp_level (CompLevel): The competition level the match was played at.
        set_number (int): The set number in a series of matches where more than one match is required in the match
            series.
        match_number (int): The match number of the match in the competition level.
        alliances (MatchAlliances): A list of alliances, the teams on the alliances, and their score.
        winning_alliance (MatchWinningAlliance): The color (red/blue) of the winning alliance. Will contain an empty
            string in the event of no winner, or a tie.
        event_key (str): Event key of the event the match was played at.
        time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the scheduled match time, as taken from
            the published schedule.
        actual_time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of actual match start time.
        predicted_time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) of the TBA predicted match start
            time.
        post_result_time (int | None): UNIX timestamp (seconds since 1-Jan-1970 00:00:00) when the match result was
            posted.
        score_breakdown (MatchScoreBreakdown2015 | MatchScoreBreakdown2016 | MatchScoreBreakdown2017 |
            MatchScoreBreakdown2018 | MatchScoreBreakdown2019 | MatchScoreBreakdown2020 | MatchScoreBreakdown2022 |
            MatchScoreBreakdown2023 | MatchScoreBreakdown2024 | MatchScoreBreakdown2025 | MatchScoreBreakdown2026 | None):
            Score breakdown for auto, teleop, etc. points. Varies from year to year. May be null.
        videos (list[MatchVideosItem]): Array of video objects associated with this match.
    """

    key: str
    comp_level: CompLevel
    set_number: int
    match_number: int
    alliances: MatchAlliances
    winning_alliance: MatchWinningAlliance
    event_key: str
    time: int | None
    actual_time: int | None
    predicted_time: int | None
    post_result_time: int | None
    score_breakdown: (
        MatchScoreBreakdown2015
        | MatchScoreBreakdown2016
        | MatchScoreBreakdown2017
        | MatchScoreBreakdown2018
        | MatchScoreBreakdown2019
        | MatchScoreBreakdown2020
        | MatchScoreBreakdown2022
        | MatchScoreBreakdown2023
        | MatchScoreBreakdown2024
        | MatchScoreBreakdown2025
        | MatchScoreBreakdown2026
        | None
    )
    videos: list[MatchVideosItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.match_score_breakdown_2015 import MatchScoreBreakdown2015
        from ..models.match_score_breakdown_2016 import MatchScoreBreakdown2016
        from ..models.match_score_breakdown_2017 import MatchScoreBreakdown2017
        from ..models.match_score_breakdown_2018 import MatchScoreBreakdown2018
        from ..models.match_score_breakdown_2019 import MatchScoreBreakdown2019
        from ..models.match_score_breakdown_2020 import MatchScoreBreakdown2020
        from ..models.match_score_breakdown_2022 import MatchScoreBreakdown2022
        from ..models.match_score_breakdown_2023 import MatchScoreBreakdown2023
        from ..models.match_score_breakdown_2024 import MatchScoreBreakdown2024
        from ..models.match_score_breakdown_2025 import MatchScoreBreakdown2025
        from ..models.match_score_breakdown_2026 import MatchScoreBreakdown2026

        key = self.key

        comp_level = self.comp_level.value

        set_number = self.set_number

        match_number = self.match_number

        alliances = self.alliances.to_dict()

        winning_alliance = self.winning_alliance.value

        event_key = self.event_key

        time: int | None
        time = self.time

        actual_time: int | None
        actual_time = self.actual_time

        predicted_time: int | None
        predicted_time = self.predicted_time

        post_result_time: int | None
        post_result_time = self.post_result_time

        score_breakdown: dict[str, Any] | None
        if isinstance(self.score_breakdown, MatchScoreBreakdown2015):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2016):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2017):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2018):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2019):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2020):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2022):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2023):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2024):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2025):
            score_breakdown = self.score_breakdown.to_dict()
        elif isinstance(self.score_breakdown, MatchScoreBreakdown2026):
            score_breakdown = self.score_breakdown.to_dict()
        else:
            score_breakdown = self.score_breakdown

        videos = []
        for videos_item_data in self.videos:
            videos_item = videos_item_data.to_dict()
            videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "comp_level": comp_level,
                "set_number": set_number,
                "match_number": match_number,
                "alliances": alliances,
                "winning_alliance": winning_alliance,
                "event_key": event_key,
                "time": time,
                "actual_time": actual_time,
                "predicted_time": predicted_time,
                "post_result_time": post_result_time,
                "score_breakdown": score_breakdown,
                "videos": videos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_alliances import MatchAlliances
        from ..models.match_score_breakdown_2015 import MatchScoreBreakdown2015
        from ..models.match_score_breakdown_2016 import MatchScoreBreakdown2016
        from ..models.match_score_breakdown_2017 import MatchScoreBreakdown2017
        from ..models.match_score_breakdown_2018 import MatchScoreBreakdown2018
        from ..models.match_score_breakdown_2019 import MatchScoreBreakdown2019
        from ..models.match_score_breakdown_2020 import MatchScoreBreakdown2020
        from ..models.match_score_breakdown_2022 import MatchScoreBreakdown2022
        from ..models.match_score_breakdown_2023 import MatchScoreBreakdown2023
        from ..models.match_score_breakdown_2024 import MatchScoreBreakdown2024
        from ..models.match_score_breakdown_2025 import MatchScoreBreakdown2025
        from ..models.match_score_breakdown_2026 import MatchScoreBreakdown2026
        from ..models.match_videos_item import MatchVideosItem

        d = dict(src_dict)
        key = d.pop("key")

        comp_level = CompLevel(d.pop("comp_level"))

        set_number = d.pop("set_number")

        match_number = d.pop("match_number")

        alliances = MatchAlliances.from_dict(d.pop("alliances"))

        winning_alliance = MatchWinningAlliance(d.pop("winning_alliance"))

        event_key = d.pop("event_key")

        def _parse_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        time = _parse_time(d.pop("time"))

        def _parse_actual_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        actual_time = _parse_actual_time(d.pop("actual_time"))

        def _parse_predicted_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        predicted_time = _parse_predicted_time(d.pop("predicted_time"))

        def _parse_post_result_time(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        post_result_time = _parse_post_result_time(d.pop("post_result_time"))

        def _parse_score_breakdown(
            data: object,
        ) -> (
            MatchScoreBreakdown2015
            | MatchScoreBreakdown2016
            | MatchScoreBreakdown2017
            | MatchScoreBreakdown2018
            | MatchScoreBreakdown2019
            | MatchScoreBreakdown2020
            | MatchScoreBreakdown2022
            | MatchScoreBreakdown2023
            | MatchScoreBreakdown2024
            | MatchScoreBreakdown2025
            | MatchScoreBreakdown2026
            | None
        ):
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_0 = MatchScoreBreakdown2015.from_dict(data)

                return score_breakdown_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_1 = MatchScoreBreakdown2016.from_dict(data)

                return score_breakdown_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_2 = MatchScoreBreakdown2017.from_dict(data)

                return score_breakdown_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_3 = MatchScoreBreakdown2018.from_dict(data)

                return score_breakdown_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_4 = MatchScoreBreakdown2019.from_dict(data)

                return score_breakdown_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_5 = MatchScoreBreakdown2020.from_dict(data)

                return score_breakdown_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_6 = MatchScoreBreakdown2022.from_dict(data)

                return score_breakdown_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_7 = MatchScoreBreakdown2023.from_dict(data)

                return score_breakdown_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_8 = MatchScoreBreakdown2024.from_dict(data)

                return score_breakdown_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_9 = MatchScoreBreakdown2025.from_dict(data)

                return score_breakdown_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                score_breakdown_type_10 = MatchScoreBreakdown2026.from_dict(data)

                return score_breakdown_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                MatchScoreBreakdown2015
                | MatchScoreBreakdown2016
                | MatchScoreBreakdown2017
                | MatchScoreBreakdown2018
                | MatchScoreBreakdown2019
                | MatchScoreBreakdown2020
                | MatchScoreBreakdown2022
                | MatchScoreBreakdown2023
                | MatchScoreBreakdown2024
                | MatchScoreBreakdown2025
                | MatchScoreBreakdown2026
                | None,
                data,
            )

        score_breakdown = _parse_score_breakdown(d.pop("score_breakdown"))

        videos = []
        _videos = d.pop("videos")
        for videos_item_data in _videos:
            videos_item = MatchVideosItem.from_dict(videos_item_data)

            videos.append(videos_item)

        match = cls(
            key=key,
            comp_level=comp_level,
            set_number=set_number,
            match_number=match_number,
            alliances=alliances,
            winning_alliance=winning_alliance,
            event_key=event_key,
            time=time,
            actual_time=actual_time,
            predicted_time=predicted_time,
            post_result_time=post_result_time,
            score_breakdown=score_breakdown,
            videos=videos,
        )

        match.additional_properties = d
        return match

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
