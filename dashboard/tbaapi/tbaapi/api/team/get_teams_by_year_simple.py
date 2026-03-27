from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_teams_by_year_simple_response_401 import GetTeamsByYearSimpleResponse401
from ...models.team_simple import TeamSimple
from ...types import UNSET, Response, Unset


def _get_kwargs(
    year: int,
    page_num: int,
    *,
    if_none_match: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_none_match, Unset):
        headers["If-None-Match"] = if_none_match

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/teams/{year}/{page_num}/simple".format(
            year=quote(str(year), safe=""),
            page_num=quote(str(page_num), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TeamSimple.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 401:
        response_401 = GetTeamsByYearSimpleResponse401.from_dict(response.json())

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
) -> Response[Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    year: int,
    page_num: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]]:
    """Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups
    of 500.

    Args:
        year (int):
        page_num (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]]
    """

    kwargs = _get_kwargs(
        year=year,
        page_num=page_num,
        if_none_match=if_none_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    year: int,
    page_num: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple] | None:
    """Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups
    of 500.

    Args:
        year (int):
        page_num (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]
    """

    return sync_detailed(
        year=year,
        page_num=page_num,
        client=client,
        if_none_match=if_none_match,
    ).parsed


async def asyncio_detailed(
    year: int,
    page_num: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Response[Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]]:
    """Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups
    of 500.

    Args:
        year (int):
        page_num (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]]
    """

    kwargs = _get_kwargs(
        year=year,
        page_num=page_num,
        if_none_match=if_none_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    year: int,
    page_num: int,
    *,
    client: AuthenticatedClient,
    if_none_match: str | Unset = UNSET,
) -> Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple] | None:
    """Gets a list of short form `Team_Simple` objects that competed in the given year, paginated in groups
    of 500.

    Args:
        year (int):
        page_num (int):
        if_none_match (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamsByYearSimpleResponse401 | list[TeamSimple]
    """

    return (
        await asyncio_detailed(
            year=year,
            page_num=page_num,
            client=client,
            if_none_match=if_none_match,
        )
    ).parsed
