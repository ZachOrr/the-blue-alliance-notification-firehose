from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_team_event_matches_simple_response_401 import GetTeamEventMatchesSimpleResponse401
from ...models.match import Match
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_key: str,
    event_key: str,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/team/{team_key}/event/{event_key}/matches/simple".format(
            team_key=quote(str(team_key), safe=""),
            event_key=quote(str(event_key), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTeamEventMatchesSimpleResponse401 | list[Match] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Match.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetTeamEventMatchesSimpleResponse401.from_dict(response.json())

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
) -> Response[Any | GetTeamEventMatchesSimpleResponse401 | list[Match]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_key: str,
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamEventMatchesSimpleResponse401 | list[Match]]:
    """Gets a short-form list of matches for the given team and event.

    Args:
        team_key (str):
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamEventMatchesSimpleResponse401 | list[Match]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        event_key=event_key,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_key: str,
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamEventMatchesSimpleResponse401 | list[Match] | None:
    """Gets a short-form list of matches for the given team and event.

    Args:
        team_key (str):
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamEventMatchesSimpleResponse401 | list[Match]
    """

    return sync_detailed(
        team_key=team_key,
        event_key=event_key,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    team_key: str,
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamEventMatchesSimpleResponse401 | list[Match]]:
    """Gets a short-form list of matches for the given team and event.

    Args:
        team_key (str):
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamEventMatchesSimpleResponse401 | list[Match]]
    """

    kwargs = _get_kwargs(
        team_key=team_key,
        event_key=event_key,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_key: str,
    event_key: str,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamEventMatchesSimpleResponse401 | list[Match] | None:
    """Gets a short-form list of matches for the given team and event.

    Args:
        team_key (str):
        event_key (str):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamEventMatchesSimpleResponse401 | list[Match]
    """

    return (
        await asyncio_detailed(
            team_key=team_key,
            event_key=event_key,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
