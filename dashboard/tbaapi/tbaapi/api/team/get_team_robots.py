from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_team_robots_response_401 import GetTeamRobotsResponse401
from ...models.team_robot import TeamRobot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_key: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/{team_key}/robots".format(
            team_key=quote(str(team_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTeamRobotsResponse401 | list[TeamRobot] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TeamRobot.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetTeamRobotsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTeamRobotsResponse401 | list[TeamRobot]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamRobotsResponse401 | list[TeamRobot]]:
    """Gets a list of year and robot name pairs for each year that a robot name was provided. Will return
    an empty array if the team has never named a robot.

    Args:
        team_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamRobotsResponse401 | list[TeamRobot]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamRobotsResponse401 | list[TeamRobot] | None:
    """Gets a list of year and robot name pairs for each year that a robot name was provided. Will return
    an empty array if the team has never named a robot.

    Args:
        team_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamRobotsResponse401 | list[TeamRobot]
    """

    return sync_detailed(
        team_key=team_key,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    team_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamRobotsResponse401 | list[TeamRobot]]:
    """Gets a list of year and robot name pairs for each year that a robot name was provided. Will return
    an empty array if the team has never named a robot.

    Args:
        team_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamRobotsResponse401 | list[TeamRobot]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamRobotsResponse401 | list[TeamRobot] | None:
    """Gets a list of year and robot name pairs for each year that a robot name was provided. Will return
    an empty array if the team has never named a robot.

    Args:
        team_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamRobotsResponse401 | list[TeamRobot]
    """

    return (
        await asyncio_detailed(
            team_key=team_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
