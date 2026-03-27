"""Contains all the data models used in inputs/outputs"""

from .api_status import APIStatus
from .api_status_app_version import APIStatusAppVersion
from .auto_charge_station_robot_2023 import AutoChargeStationRobot2023
from .auto_line_robot_2024 import AutoLineRobot2024
from .auto_robot_2018 import AutoRobot2018
from .award import Award
from .award_recipient import AwardRecipient
from .bay_2019 import Bay2019
from .bridge_state_2023 import BridgeState2023
from .comp_level import CompLevel
from .district import District
from .district_advancement import DistrictAdvancement
from .district_insight import DistrictInsight
from .district_insight_district_data import DistrictInsightDistrictData
from .district_insight_district_data_region_data_type_0 import DistrictInsightDistrictDataRegionDataType0
from .district_insight_region_data import DistrictInsightRegionData
from .district_insight_region_data_yearly_active_team_count import DistrictInsightRegionDataYearlyActiveTeamCount
from .district_insight_region_data_yearly_event_count import DistrictInsightRegionDataYearlyEventCount
from .district_insight_region_data_yearly_gained_teams import DistrictInsightRegionDataYearlyGainedTeams
from .district_insight_region_data_yearly_lost_teams import DistrictInsightRegionDataYearlyLostTeams
from .district_insight_team_data_type_0 import DistrictInsightTeamDataType0
from .district_insight_team_data_type_0_additional_property import DistrictInsightTeamDataType0AdditionalProperty
from .district_official_advancement_counts import DistrictOfficialAdvancementCounts
from .district_ranking import DistrictRanking
from .district_ranking_event_points_item import DistrictRankingEventPointsItem
from .double_elim_round import DoubleElimRound
from .elimination_alliance import EliminationAlliance
from .elimination_alliance_backup_type_0 import EliminationAllianceBackupType0
from .elimination_alliance_status import EliminationAllianceStatus
from .elimination_alliance_status_status import EliminationAllianceStatusStatus
from .end_game_charge_station_robot_2023 import EndGameChargeStationRobot2023
from .end_game_robot_2024 import EndGameRobot2024
from .end_game_robot_2025 import EndGameRobot2025
from .endgame_robot_2018 import EndgameRobot2018
from .endgame_robot_2019 import EndgameRobot2019
from .endgame_robot_2020 import EndgameRobot2020
from .endgame_robot_2022 import EndgameRobot2022
from .endgame_rung_is_level_2020 import EndgameRungIsLevel2020
from .event import Event
from .event_cop_rs import EventCOPRs
from .event_cop_rs_additional_property import EventCOPRsAdditionalProperty
from .event_district_points import EventDistrictPoints
from .event_district_points_points import EventDistrictPointsPoints
from .event_district_points_points_additional_property import EventDistrictPointsPointsAdditionalProperty
from .event_district_points_tiebreakers import EventDistrictPointsTiebreakers
from .event_district_points_tiebreakers_additional_property import EventDistrictPointsTiebreakersAdditionalProperty
from .event_insights import EventInsights
from .event_insights_2016 import EventInsights2016
from .event_insights_2017 import EventInsights2017
from .event_insights_2018 import EventInsights2018
from .event_insights_playoff import EventInsightsPlayoff
from .event_insights_qual import EventInsightsQual
from .event_op_rs import EventOPRs
from .event_op_rs_ccwms import EventOPRsCcwms
from .event_op_rs_dprs import EventOPRsDprs
from .event_op_rs_oprs import EventOPRsOprs
from .event_predictions import EventPredictions
from .event_ranking import EventRanking
from .event_ranking_extra_stats_info_item import EventRankingExtraStatsInfoItem
from .event_ranking_rankings_item import EventRankingRankingsItem
from .event_ranking_sort_order_info_type_0_item import EventRankingSortOrderInfoType0Item
from .event_remap_teams_type_0 import EventRemapTeamsType0
from .event_simple import EventSimple
from .get_district_advancement_response_200_type_1 import GetDistrictAdvancementResponse200Type1
from .get_district_advancement_response_401 import GetDistrictAdvancementResponse401
from .get_district_awards_response_401 import GetDistrictAwardsResponse401
from .get_district_dcmp_history_response_200_item import GetDistrictDCMPHistoryResponse200Item
from .get_district_dcmp_history_response_401 import GetDistrictDCMPHistoryResponse401
from .get_district_events_keys_response_401 import GetDistrictEventsKeysResponse401
from .get_district_events_response_401 import GetDistrictEventsResponse401
from .get_district_events_simple_response_401 import GetDistrictEventsSimpleResponse401
from .get_district_history_response_401 import GetDistrictHistoryResponse401
from .get_district_insights_response_401 import GetDistrictInsightsResponse401
from .get_district_rankings_response_401 import GetDistrictRankingsResponse401
from .get_district_teams_keys_response_401 import GetDistrictTeamsKeysResponse401
from .get_district_teams_response_401 import GetDistrictTeamsResponse401
from .get_district_teams_simple_response_401 import GetDistrictTeamsSimpleResponse401
from .get_districts_by_year_response_401 import GetDistrictsByYearResponse401
from .get_event_advancement_points_response_401 import GetEventAdvancementPointsResponse401
from .get_event_alliances_response_401 import GetEventAlliancesResponse401
from .get_event_awards_response_401 import GetEventAwardsResponse401
from .get_event_cop_rs_response_401 import GetEventCOPRsResponse401
from .get_event_district_points_response_401 import GetEventDistrictPointsResponse401
from .get_event_insights_response_401 import GetEventInsightsResponse401
from .get_event_match_timeseries_response_401 import GetEventMatchTimeseriesResponse401
from .get_event_matches_keys_response_401 import GetEventMatchesKeysResponse401
from .get_event_matches_response_401 import GetEventMatchesResponse401
from .get_event_matches_simple_response_401 import GetEventMatchesSimpleResponse401
from .get_event_op_rs_response_401 import GetEventOPRsResponse401
from .get_event_predictions_response_401 import GetEventPredictionsResponse401
from .get_event_rankings_response_401 import GetEventRankingsResponse401
from .get_event_response_401 import GetEventResponse401
from .get_event_simple_response_401 import GetEventSimpleResponse401
from .get_event_team_media_response_401 import GetEventTeamMediaResponse401
from .get_event_teams_keys_response_401 import GetEventTeamsKeysResponse401
from .get_event_teams_response_401 import GetEventTeamsResponse401
from .get_event_teams_simple_response_401 import GetEventTeamsSimpleResponse401
from .get_event_teams_statuses_response_200 import GetEventTeamsStatusesResponse200
from .get_event_teams_statuses_response_401 import GetEventTeamsStatusesResponse401
from .get_events_by_year_keys_response_401 import GetEventsByYearKeysResponse401
from .get_events_by_year_response_401 import GetEventsByYearResponse401
from .get_events_by_year_simple_response_401 import GetEventsByYearSimpleResponse401
from .get_insights_leaderboards_year_response_401 import GetInsightsLeaderboardsYearResponse401
from .get_insights_notables_year_response_401 import GetInsightsNotablesYearResponse401
from .get_match_response_401 import GetMatchResponse401
from .get_match_simple_response_401 import GetMatchSimpleResponse401
from .get_match_timeseries_response_200_item import GetMatchTimeseriesResponse200Item
from .get_match_timeseries_response_401 import GetMatchTimeseriesResponse401
from .get_match_zebra_response_401 import GetMatchZebraResponse401
from .get_regional_advancement_response_200_type_1 import GetRegionalAdvancementResponse200Type1
from .get_regional_advancement_response_401 import GetRegionalAdvancementResponse401
from .get_regional_champs_pool_points_response_401 import GetRegionalChampsPoolPointsResponse401
from .get_regional_rankings_response_401 import GetRegionalRankingsResponse401
from .get_search_index_response_401 import GetSearchIndexResponse401
from .get_status_response_401 import GetStatusResponse401
from .get_team_awards_by_year_response_401 import GetTeamAwardsByYearResponse401
from .get_team_awards_response_401 import GetTeamAwardsResponse401
from .get_team_districts_response_401 import GetTeamDistrictsResponse401
from .get_team_event_awards_response_401 import GetTeamEventAwardsResponse401
from .get_team_event_matches_keys_response_401 import GetTeamEventMatchesKeysResponse401
from .get_team_event_matches_response_401 import GetTeamEventMatchesResponse401
from .get_team_event_matches_simple_response_401 import GetTeamEventMatchesSimpleResponse401
from .get_team_event_status_response_401 import GetTeamEventStatusResponse401
from .get_team_events_by_year_keys_response_401 import GetTeamEventsByYearKeysResponse401
from .get_team_events_by_year_response_401 import GetTeamEventsByYearResponse401
from .get_team_events_by_year_simple_response_401 import GetTeamEventsByYearSimpleResponse401
from .get_team_events_keys_response_401 import GetTeamEventsKeysResponse401
from .get_team_events_response_401 import GetTeamEventsResponse401
from .get_team_events_simple_response_401 import GetTeamEventsSimpleResponse401
from .get_team_events_statuses_by_year_response_200 import GetTeamEventsStatusesByYearResponse200
from .get_team_events_statuses_by_year_response_401 import GetTeamEventsStatusesByYearResponse401
from .get_team_history_response_401 import GetTeamHistoryResponse401
from .get_team_matches_by_year_keys_response_401 import GetTeamMatchesByYearKeysResponse401
from .get_team_matches_by_year_response_401 import GetTeamMatchesByYearResponse401
from .get_team_matches_by_year_simple_response_401 import GetTeamMatchesByYearSimpleResponse401
from .get_team_media_by_tag_response_401 import GetTeamMediaByTagResponse401
from .get_team_media_by_tag_year_response_401 import GetTeamMediaByTagYearResponse401
from .get_team_media_by_year_response_401 import GetTeamMediaByYearResponse401
from .get_team_response_401 import GetTeamResponse401
from .get_team_robots_response_401 import GetTeamRobotsResponse401
from .get_team_simple_response_401 import GetTeamSimpleResponse401
from .get_team_social_media_response_401 import GetTeamSocialMediaResponse401
from .get_team_years_participated_response_401 import GetTeamYearsParticipatedResponse401
from .get_teams_by_year_keys_response_401 import GetTeamsByYearKeysResponse401
from .get_teams_by_year_response_401 import GetTeamsByYearResponse401
from .get_teams_by_year_simple_response_401 import GetTeamsByYearSimpleResponse401
from .get_teams_keys_response_401 import GetTeamsKeysResponse401
from .get_teams_response_401 import GetTeamsResponse401
from .get_teams_simple_response_401 import GetTeamsSimpleResponse401
from .hab_line_2019 import HabLine2019
from .history import History
from .hub_score_2026 import HubScore2026
from .init_line_robot_2020 import InitLineRobot2020
from .leaderboard_insight import LeaderboardInsight
from .leaderboard_insight_data import LeaderboardInsightData
from .leaderboard_insight_data_key_type import LeaderboardInsightDataKeyType
from .leaderboard_insight_data_rankings_item import LeaderboardInsightDataRankingsItem
from .match import Match
from .match_alliance import MatchAlliance
from .match_alliances import MatchAlliances
from .match_score_breakdown_2015 import MatchScoreBreakdown2015
from .match_score_breakdown_2015_alliance import MatchScoreBreakdown2015Alliance
from .match_score_breakdown_2015_coopertition import MatchScoreBreakdown2015Coopertition
from .match_score_breakdown_2016 import MatchScoreBreakdown2016
from .match_score_breakdown_2016_alliance import MatchScoreBreakdown2016Alliance
from .match_score_breakdown_2017 import MatchScoreBreakdown2017
from .match_score_breakdown_2017_alliance import MatchScoreBreakdown2017Alliance
from .match_score_breakdown_2018 import MatchScoreBreakdown2018
from .match_score_breakdown_2018_alliance import MatchScoreBreakdown2018Alliance
from .match_score_breakdown_2018_alliance_tba_game_data import MatchScoreBreakdown2018AllianceTbaGameData
from .match_score_breakdown_2019 import MatchScoreBreakdown2019
from .match_score_breakdown_2019_alliance import MatchScoreBreakdown2019Alliance
from .match_score_breakdown_2020 import MatchScoreBreakdown2020
from .match_score_breakdown_2020_alliance import MatchScoreBreakdown2020Alliance
from .match_score_breakdown_2022 import MatchScoreBreakdown2022
from .match_score_breakdown_2022_alliance import MatchScoreBreakdown2022Alliance
from .match_score_breakdown_2023 import MatchScoreBreakdown2023
from .match_score_breakdown_2023_alliance import MatchScoreBreakdown2023Alliance
from .match_score_breakdown_2023_alliance_auto_community import MatchScoreBreakdown2023AllianceAutoCommunity
from .match_score_breakdown_2023_alliance_auto_community_b_item import MatchScoreBreakdown2023AllianceAutoCommunityBItem
from .match_score_breakdown_2023_alliance_auto_community_m_item import MatchScoreBreakdown2023AllianceAutoCommunityMItem
from .match_score_breakdown_2023_alliance_auto_community_t_item import MatchScoreBreakdown2023AllianceAutoCommunityTItem
from .match_score_breakdown_2023_alliance_links_type_0_item import MatchScoreBreakdown2023AllianceLinksType0Item
from .match_score_breakdown_2023_alliance_links_type_0_item_nodes_item import (
    MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem,
)
from .match_score_breakdown_2023_alliance_links_type_0_item_row import MatchScoreBreakdown2023AllianceLinksType0ItemRow
from .match_score_breakdown_2023_alliance_teleop_community import MatchScoreBreakdown2023AllianceTeleopCommunity
from .match_score_breakdown_2023_alliance_teleop_community_b_item import (
    MatchScoreBreakdown2023AllianceTeleopCommunityBItem,
)
from .match_score_breakdown_2023_alliance_teleop_community_m_item import (
    MatchScoreBreakdown2023AllianceTeleopCommunityMItem,
)
from .match_score_breakdown_2023_alliance_teleop_community_t_item import (
    MatchScoreBreakdown2023AllianceTeleopCommunityTItem,
)
from .match_score_breakdown_2024 import MatchScoreBreakdown2024
from .match_score_breakdown_2024_alliance import MatchScoreBreakdown2024Alliance
from .match_score_breakdown_2025 import MatchScoreBreakdown2025
from .match_score_breakdown_2025_alliance import MatchScoreBreakdown2025Alliance
from .match_score_breakdown_2025_alliance_auto_reef import MatchScoreBreakdown2025AllianceAutoReef
from .match_score_breakdown_2025_alliance_teleop_reef import MatchScoreBreakdown2025AllianceTeleopReef
from .match_score_breakdown_2026 import MatchScoreBreakdown2026
from .match_score_breakdown_2026_alliance import MatchScoreBreakdown2026Alliance
from .match_simple import MatchSimple
from .match_simple_alliances import MatchSimpleAlliances
from .match_simple_winning_alliance import MatchSimpleWinningAlliance
from .match_timeseries_2018 import MatchTimeseries2018
from .match_videos_item import MatchVideosItem
from .match_winning_alliance import MatchWinningAlliance
from .media import Media
from .media_details_type_0 import MediaDetailsType0
from .media_details_type_1 import MediaDetailsType1
from .media_details_type_2 import MediaDetailsType2
from .media_details_type_3 import MediaDetailsType3
from .media_details_type_4 import MediaDetailsType4
from .media_details_type_5 import MediaDetailsType5
from .media_type import MediaType
from .mobility_robot_2023 import MobilityRobot2023
from .notables_insight import NotablesInsight
from .notables_insight_data import NotablesInsightData
from .notables_insight_data_entries_item import NotablesInsightDataEntriesItem
from .position_2016 import Position2016
from .pre_match_bay_2019 import PreMatchBay2019
from .reef_row_2025 import ReefRow2025
from .regional_advancement import RegionalAdvancement
from .regional_advancement_cmp_status import RegionalAdvancementCmpStatus
from .regional_ranking import RegionalRanking
from .regional_ranking_event_points_item import RegionalRankingEventPointsItem
from .robot_auto_2016_with_unknown import RobotAuto2016WithUnknown
from .robot_auto_2016_without_unknown import RobotAuto2016WithoutUnknown
from .robot_auto_2017 import RobotAuto2017
from .search_index import SearchIndex
from .search_index_events_item import SearchIndexEventsItem
from .search_index_teams_item import SearchIndexTeamsItem
from .stage_3_target_color_2020 import Stage3TargetColor2020
from .taxi_robot_2022 import TaxiRobot2022
from .team import Team
from .team_event_status import TeamEventStatus
from .team_event_status_alliance import TeamEventStatusAlliance
from .team_event_status_alliance_backup_type_1 import TeamEventStatusAllianceBackupType1
from .team_event_status_playoff_type_1 import TeamEventStatusPlayoffType1
from .team_event_status_playoff_type_1_status import TeamEventStatusPlayoffType1Status
from .team_event_status_rank import TeamEventStatusRank
from .team_event_status_rank_ranking_type_0 import TeamEventStatusRankRankingType0
from .team_event_status_rank_sort_order_info_type_0_item import TeamEventStatusRankSortOrderInfoType0Item
from .team_robot import TeamRobot
from .team_simple import TeamSimple
from .touchpad_2017 import Touchpad2017
from .tower_face_2016 import TowerFace2016
from .tower_robot_2026 import TowerRobot2026
from .webcast import Webcast
from .webcast_status import WebcastStatus
from .webcast_type import WebcastType
from .wlt_record import WLTRecord
from .zebra import Zebra
from .zebra_alliances import ZebraAlliances
from .zebra_team import ZebraTeam

__all__ = (
    "APIStatus",
    "APIStatusAppVersion",
    "AutoChargeStationRobot2023",
    "AutoLineRobot2024",
    "AutoRobot2018",
    "Award",
    "AwardRecipient",
    "Bay2019",
    "BridgeState2023",
    "CompLevel",
    "District",
    "DistrictAdvancement",
    "DistrictInsight",
    "DistrictInsightDistrictData",
    "DistrictInsightDistrictDataRegionDataType0",
    "DistrictInsightRegionData",
    "DistrictInsightRegionDataYearlyActiveTeamCount",
    "DistrictInsightRegionDataYearlyEventCount",
    "DistrictInsightRegionDataYearlyGainedTeams",
    "DistrictInsightRegionDataYearlyLostTeams",
    "DistrictInsightTeamDataType0",
    "DistrictInsightTeamDataType0AdditionalProperty",
    "DistrictOfficialAdvancementCounts",
    "DistrictRanking",
    "DistrictRankingEventPointsItem",
    "DoubleElimRound",
    "EliminationAlliance",
    "EliminationAllianceBackupType0",
    "EliminationAllianceStatus",
    "EliminationAllianceStatusStatus",
    "EndGameChargeStationRobot2023",
    "EndgameRobot2018",
    "EndgameRobot2019",
    "EndgameRobot2020",
    "EndgameRobot2022",
    "EndGameRobot2024",
    "EndGameRobot2025",
    "EndgameRungIsLevel2020",
    "Event",
    "EventCOPRs",
    "EventCOPRsAdditionalProperty",
    "EventDistrictPoints",
    "EventDistrictPointsPoints",
    "EventDistrictPointsPointsAdditionalProperty",
    "EventDistrictPointsTiebreakers",
    "EventDistrictPointsTiebreakersAdditionalProperty",
    "EventInsights",
    "EventInsights2016",
    "EventInsights2017",
    "EventInsights2018",
    "EventInsightsPlayoff",
    "EventInsightsQual",
    "EventOPRs",
    "EventOPRsCcwms",
    "EventOPRsDprs",
    "EventOPRsOprs",
    "EventPredictions",
    "EventRanking",
    "EventRankingExtraStatsInfoItem",
    "EventRankingRankingsItem",
    "EventRankingSortOrderInfoType0Item",
    "EventRemapTeamsType0",
    "EventSimple",
    "GetDistrictAdvancementResponse200Type1",
    "GetDistrictAdvancementResponse401",
    "GetDistrictAwardsResponse401",
    "GetDistrictDCMPHistoryResponse200Item",
    "GetDistrictDCMPHistoryResponse401",
    "GetDistrictEventsKeysResponse401",
    "GetDistrictEventsResponse401",
    "GetDistrictEventsSimpleResponse401",
    "GetDistrictHistoryResponse401",
    "GetDistrictInsightsResponse401",
    "GetDistrictRankingsResponse401",
    "GetDistrictsByYearResponse401",
    "GetDistrictTeamsKeysResponse401",
    "GetDistrictTeamsResponse401",
    "GetDistrictTeamsSimpleResponse401",
    "GetEventAdvancementPointsResponse401",
    "GetEventAlliancesResponse401",
    "GetEventAwardsResponse401",
    "GetEventCOPRsResponse401",
    "GetEventDistrictPointsResponse401",
    "GetEventInsightsResponse401",
    "GetEventMatchesKeysResponse401",
    "GetEventMatchesResponse401",
    "GetEventMatchesSimpleResponse401",
    "GetEventMatchTimeseriesResponse401",
    "GetEventOPRsResponse401",
    "GetEventPredictionsResponse401",
    "GetEventRankingsResponse401",
    "GetEventResponse401",
    "GetEventsByYearKeysResponse401",
    "GetEventsByYearResponse401",
    "GetEventsByYearSimpleResponse401",
    "GetEventSimpleResponse401",
    "GetEventTeamMediaResponse401",
    "GetEventTeamsKeysResponse401",
    "GetEventTeamsResponse401",
    "GetEventTeamsSimpleResponse401",
    "GetEventTeamsStatusesResponse200",
    "GetEventTeamsStatusesResponse401",
    "GetInsightsLeaderboardsYearResponse401",
    "GetInsightsNotablesYearResponse401",
    "GetMatchResponse401",
    "GetMatchSimpleResponse401",
    "GetMatchTimeseriesResponse200Item",
    "GetMatchTimeseriesResponse401",
    "GetMatchZebraResponse401",
    "GetRegionalAdvancementResponse200Type1",
    "GetRegionalAdvancementResponse401",
    "GetRegionalChampsPoolPointsResponse401",
    "GetRegionalRankingsResponse401",
    "GetSearchIndexResponse401",
    "GetStatusResponse401",
    "GetTeamAwardsByYearResponse401",
    "GetTeamAwardsResponse401",
    "GetTeamDistrictsResponse401",
    "GetTeamEventAwardsResponse401",
    "GetTeamEventMatchesKeysResponse401",
    "GetTeamEventMatchesResponse401",
    "GetTeamEventMatchesSimpleResponse401",
    "GetTeamEventsByYearKeysResponse401",
    "GetTeamEventsByYearResponse401",
    "GetTeamEventsByYearSimpleResponse401",
    "GetTeamEventsKeysResponse401",
    "GetTeamEventsResponse401",
    "GetTeamEventsSimpleResponse401",
    "GetTeamEventsStatusesByYearResponse200",
    "GetTeamEventsStatusesByYearResponse401",
    "GetTeamEventStatusResponse401",
    "GetTeamHistoryResponse401",
    "GetTeamMatchesByYearKeysResponse401",
    "GetTeamMatchesByYearResponse401",
    "GetTeamMatchesByYearSimpleResponse401",
    "GetTeamMediaByTagResponse401",
    "GetTeamMediaByTagYearResponse401",
    "GetTeamMediaByYearResponse401",
    "GetTeamResponse401",
    "GetTeamRobotsResponse401",
    "GetTeamsByYearKeysResponse401",
    "GetTeamsByYearResponse401",
    "GetTeamsByYearSimpleResponse401",
    "GetTeamSimpleResponse401",
    "GetTeamsKeysResponse401",
    "GetTeamSocialMediaResponse401",
    "GetTeamsResponse401",
    "GetTeamsSimpleResponse401",
    "GetTeamYearsParticipatedResponse401",
    "HabLine2019",
    "History",
    "HubScore2026",
    "InitLineRobot2020",
    "LeaderboardInsight",
    "LeaderboardInsightData",
    "LeaderboardInsightDataKeyType",
    "LeaderboardInsightDataRankingsItem",
    "Match",
    "MatchAlliance",
    "MatchAlliances",
    "MatchScoreBreakdown2015",
    "MatchScoreBreakdown2015Alliance",
    "MatchScoreBreakdown2015Coopertition",
    "MatchScoreBreakdown2016",
    "MatchScoreBreakdown2016Alliance",
    "MatchScoreBreakdown2017",
    "MatchScoreBreakdown2017Alliance",
    "MatchScoreBreakdown2018",
    "MatchScoreBreakdown2018Alliance",
    "MatchScoreBreakdown2018AllianceTbaGameData",
    "MatchScoreBreakdown2019",
    "MatchScoreBreakdown2019Alliance",
    "MatchScoreBreakdown2020",
    "MatchScoreBreakdown2020Alliance",
    "MatchScoreBreakdown2022",
    "MatchScoreBreakdown2022Alliance",
    "MatchScoreBreakdown2023",
    "MatchScoreBreakdown2023Alliance",
    "MatchScoreBreakdown2023AllianceAutoCommunity",
    "MatchScoreBreakdown2023AllianceAutoCommunityBItem",
    "MatchScoreBreakdown2023AllianceAutoCommunityMItem",
    "MatchScoreBreakdown2023AllianceAutoCommunityTItem",
    "MatchScoreBreakdown2023AllianceLinksType0Item",
    "MatchScoreBreakdown2023AllianceLinksType0ItemNodesItem",
    "MatchScoreBreakdown2023AllianceLinksType0ItemRow",
    "MatchScoreBreakdown2023AllianceTeleopCommunity",
    "MatchScoreBreakdown2023AllianceTeleopCommunityBItem",
    "MatchScoreBreakdown2023AllianceTeleopCommunityMItem",
    "MatchScoreBreakdown2023AllianceTeleopCommunityTItem",
    "MatchScoreBreakdown2024",
    "MatchScoreBreakdown2024Alliance",
    "MatchScoreBreakdown2025",
    "MatchScoreBreakdown2025Alliance",
    "MatchScoreBreakdown2025AllianceAutoReef",
    "MatchScoreBreakdown2025AllianceTeleopReef",
    "MatchScoreBreakdown2026",
    "MatchScoreBreakdown2026Alliance",
    "MatchSimple",
    "MatchSimpleAlliances",
    "MatchSimpleWinningAlliance",
    "MatchTimeseries2018",
    "MatchVideosItem",
    "MatchWinningAlliance",
    "Media",
    "MediaDetailsType0",
    "MediaDetailsType1",
    "MediaDetailsType2",
    "MediaDetailsType3",
    "MediaDetailsType4",
    "MediaDetailsType5",
    "MediaType",
    "MobilityRobot2023",
    "NotablesInsight",
    "NotablesInsightData",
    "NotablesInsightDataEntriesItem",
    "Position2016",
    "PreMatchBay2019",
    "ReefRow2025",
    "RegionalAdvancement",
    "RegionalAdvancementCmpStatus",
    "RegionalRanking",
    "RegionalRankingEventPointsItem",
    "RobotAuto2016WithoutUnknown",
    "RobotAuto2016WithUnknown",
    "RobotAuto2017",
    "SearchIndex",
    "SearchIndexEventsItem",
    "SearchIndexTeamsItem",
    "Stage3TargetColor2020",
    "TaxiRobot2022",
    "Team",
    "TeamEventStatus",
    "TeamEventStatusAlliance",
    "TeamEventStatusAllianceBackupType1",
    "TeamEventStatusPlayoffType1",
    "TeamEventStatusPlayoffType1Status",
    "TeamEventStatusRank",
    "TeamEventStatusRankRankingType0",
    "TeamEventStatusRankSortOrderInfoType0Item",
    "TeamRobot",
    "TeamSimple",
    "Touchpad2017",
    "TowerFace2016",
    "TowerRobot2026",
    "Webcast",
    "WebcastStatus",
    "WebcastType",
    "WLTRecord",
    "Zebra",
    "ZebraAlliances",
    "ZebraTeam",
)
