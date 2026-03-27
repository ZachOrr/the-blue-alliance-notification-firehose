from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event import Event
from ...models.get_team_events_by_year_response_401 import GetTeamEventsByYearResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_key: str,
    year: int,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/{team_key}/events/{year}".format(
            team_key=quote(str(team_key), safe=""),
            year=quote(str(year), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTeamEventsByYearResponse401 | list[Event] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Event.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetTeamEventsByYearResponse401.from_dict(response.json())

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
) -> Response[Any | GetTeamEventsByYearResponse401 | list[Event]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_key: str,
    year: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamEventsByYearResponse401 | list[Event]]:
    """Gets a list of events this team has competed at in the given year.

    Args:
        team_key (str):
        year (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamEventsByYearResponse401 | list[Event]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        year=year,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_key: str,
    year: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamEventsByYearResponse401 | list[Event] | None:
    """Gets a list of events this team has competed at in the given year.

    Args:
        team_key (str):
        year (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamEventsByYearResponse401 | list[Event]
    """

    return sync_detailed(
        team_key=team_key,
        year=year,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    team_key: str,
    year: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamEventsByYearResponse401 | list[Event]]:
    """Gets a list of events this team has competed at in the given year.

    Args:
        team_key (str):
        year (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamEventsByYearResponse401 | list[Event]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        year=year,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_key: str,
    year: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamEventsByYearResponse401 | list[Event] | None:
    """Gets a list of events this team has competed at in the given year.

    Args:
        team_key (str):
        year (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamEventsByYearResponse401 | list[Event]
    """

    return (
        await asyncio_detailed(
            team_key=team_key,
            year=year,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
